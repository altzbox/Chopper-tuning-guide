import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import argparse
import plotly.express as px
import plotly.offline as pyo
from natsort import natsorted

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process CSV files and calculate median magnitudes.')
    parser.add_argument('--current_min', type=int, required=True, help='Minimum value for current')
    parser.add_argument('--current_max', type=int, required=True, help='Maximum value for current')
    parser.add_argument('--tbl_min', type=int, required=True, help='Minimum value for tbl')
    parser.add_argument('--tbl_max', type=int, required=True, help='Maximum value for tbl')
    parser.add_argument('--toff_min', type=int, required=True, help='Minimum value for toff')
    parser.add_argument('--toff_max', type=int, required=True, help='Maximum value for toff')
    parser.add_argument('--hstrt_hend_max', type=int, required=True, help='Maximum value for hstrt_hend_max')
    parser.add_argument('--min_hstrt', type=int, required=True, help='Minimum value for min_hstrt')
    parser.add_argument('--max_hstrt', type=int, required=True, help='Maximum value for max_hstrt')
    parser.add_argument('--min_hend', type=int, required=True, help='Minimum value for min_hend')
    parser.add_argument('--max_hend', type=int, required=True, help='Maximum value for max_hend')
    parser.add_argument('--min_speed', type=int, required=True, help='Minimum value for speed')
    parser.add_argument('--max_speed', type=int, required=True, help='Maximum value for speed')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations for speed cycle')
    return parser.parse_args()

def calculate_static_measures(file_path, trim_percentage=0.2):
    data = pd.read_csv(file_path, delimiter=',')
    trim_size = int(trim_percentage * len(data))
    trimmed_data = data.iloc[trim_size:-trim_size]
    static_median_x = trimmed_data['accel_x'].median()
    static_median_y = trimmed_data['accel_y'].median()
    static_median_z = trimmed_data['accel_z'].median()
    return static_median_x, static_median_y, static_median_z

def main():
    args = parse_arguments()
    directory_path = '/tmp'
    csv_files = sorted([f for f in os.listdir(directory_path) if f.startswith('adxl') and f.endswith('.csv') and f != 'adxl345-stand_still.csv'])
    parameters_list = []
    
    for current in range(args.current_min, args.current_max + 1):
        for tbl in range(args.tbl_min, args.tbl_max + 1):
            for toff in range(args.toff_min, args.toff_max + 1):
                for hstrt in range(args.min_hstrt, args.max_hstrt + 1):
                    for hend in range(args.min_hend, args.max_hend + 1):
                        if hstrt + hend <= args.hstrt_hend_max:
                            for speed in range(args.min_speed, args.max_speed + 1):
                                for _ in range(args.iterations):
                                    parameters = f"current={current}_tbl={tbl}_toff={toff}_hstrt={hstrt}_hend={hend}_speed={speed}"
                                    parameters_list.append(parameters)

    if len(csv_files) != len(parameters_list):
        print(f"Warning: The number of CSV files ({len(csv_files)}) does not match the expected number of combinations based on the provided parameters ({len(parameters_list)}).")
        print("Please check your input and try again.")
        return

    results = []
    static_median_x, static_median_y, static_median_z = calculate_static_measures(os.path.join(directory_path, 'adxl345-stand_still.csv'))

    for csv_file, parameters in tqdm(zip(csv_files, parameters_list), desc='Processing CSV files', total=len(csv_files)):
        file_path = os.path.join(directory_path, csv_file)
        data = pd.read_csv(file_path, delimiter=',')
        data['accel_x'] -= static_median_x
        data['accel_y'] -= static_median_y
        data['accel_z'] -= static_median_z
        trim_size = int(0.2 * len(data))
        data = data.iloc[trim_size:-trim_size]
        data['magnitude'] = np.sqrt(data['accel_x']**2 + data['accel_y']**2 + data['accel_z']**2)
        median_magnitude = data['magnitude'].median()
        current_toff = int(parameters.split('_')[2].split('=')[1])
        results.append({'file_name': csv_file, 'median_magnitude': median_magnitude, 'parameters': parameters, 'toff': current_toff})

    results_df = pd.DataFrame(results)
    results_csv_path = '/tmp/median_magnitudes.csv'
    results_df.to_csv(results_csv_path, index=False)

    grouped_results = results_df.groupby('parameters')['median_magnitude'].mean().reset_index()
    sorted_indices = natsorted(range(len(grouped_results)), key=lambda i: grouped_results['parameters'].iloc[i])
    grouped_results = grouped_results.iloc[sorted_indices]

    # Add a 'toff' column based on the 'parameters' column
    grouped_results['toff'] = grouped_results['parameters'].apply(lambda x: int(x.split('_')[2].split('=')[1]))

    grouped_results_csv_path = '/tmp/grouped_median_magnitudes.csv'
    grouped_results.to_csv(grouped_results_csv_path, index=False)

    print(f'Saved grouped results to: {grouped_results_csv_path}')

    toff_colors = ['#12B57F', '#9DB512', '#DF8816', '#1297B5', '#5912B5', '#B51284', '#127D0C', '#DC143C', '#2F4F4F']

    fig = px.bar(grouped_results, x='median_magnitude', y='parameters', color='toff', title='Median Magnitude vs. Parameters',
                 color_discrete_map={str(i): toff_colors[i] for i in range(9)},
                 color_continuous_scale=toff_colors)
    fig.update_layout(xaxis_title='Median Magnitude', yaxis_title='Parameters')
    fig.update_layout(coloraxis_showscale=False)
    plot_html_path = '/tmp/interactive_plot.html'
    pyo.plot(fig, filename=plot_html_path, auto_open=False)

    print(f'Access the interactive plot at: {plot_html_path}')



if __name__ == "__main__":
    main()
