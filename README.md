<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 7.6.2.1 (Windows)"/>
	<meta name="created" content="2023-12-05T15:05:22.578000000"/>
	<meta name="changed" content="2023-12-05T16:07:22.272000000"/>
	<style type="text/css">
		@page { size: 21cm 29.7cm; margin: 2cm }
		p { line-height: 115%; margin-bottom: 0.25cm; background: transparent }
	</style>
</head>
<body lang="ru-RU" link="#000080" vlink="#800000" dir="ltr"><p lang="en-US" style="line-height: 100%; margin-bottom: 0cm">
1. <span lang="ru-RU">Установка скрипта на хост
с Клиппером.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">Создаем
директорию</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">mkdir
scripts</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">Копируем
в нее файл скрипта chopper_plot.py<br/>
Переходим
в директорию scripts</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">cd
scripts</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">Выдаем
разрешение на запуск </span>
</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">chmod
+x chopper_plot.py<br/>
<br/>
Устанавливаем необходимые
библиотеки<br/>
pip install pandas numpy tqdm plotly
natsort<br/>
</span><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">2.
Установка макроса в Клиппер.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">Копируем
файл chopper_tune.cfg для портала на 2-х моторах
stepper_x и stepper_y или chopper_tune_awd.cfg, если у вас
конфигурация портала с 4-мя двигателями
stepper_x, stepper_x1, stepper_y, stepper_y1.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">Прописываем
файл в </span>printer.cfg</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm">[include
chopper_tune_awd.cfg]</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">3.
Подключаем акселерометр.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">4.
Калибровка.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">4.1.
Определяем «рябые» скорости.<br/>
В консоли
Клиппера водим команду</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">DUMP_TMC
STEPPER=stepper_x REGISTER=chopconf</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">В
ответ получаем текущие параметры
чоппера.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">CHOPCONF:
224181f8 toff=8 hstrt=7 hend=3 tbl=3 tpfd=4 mres=2(64usteps) dedge=1 </span>
</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU"><br/>
Запускаем
макрос с вашими текущими параметрами
чоппера, которые выдал дамп и скоростью
от от 20 до 150 мм/с. </span>
</p>
<p style="line-height: 100%; margin-bottom: 0cm">Пример:</p>
<p style="line-height: 100%; margin-bottom: 0cm">CHOPPER_TUNE_AWD
CURRENT_MIN_mA=2000 CURRENT_MAX_mA=2000 TBL_MIN=0 TBL_MAX=0
TOFF_MIN=8 TOFF_MAX=8 HSTRT_HEND_MAX=10 MIN_HSTRT=7 MAX_HSTRT=7
MIN_HEND=3 MAX_HEND=3 MIN_SPEED=20 MAX_SPEED=150 TRAVEL_DISTANCE=150
ITERATIONS=1</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">Голова
принтера совершит прогоны на заданных
скоростях с шагом 1мм/с.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">В
начале выполнения макроса в консоли
будет текст с командой вида </span>
</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">&quot;Use
the following command to process the generated files: python3
chopper_plot.py --current_min=2000 --current_max=2000 --tbl_min=0
--tbl_max=0 --toff_min=8 --toff_max=8 --hstrt_hend_max=10
--min_hstrt=5 --max_hstrt=5 --min_hend=5 --max_hend=5 --min_speed=20
--max_speed=150 --iterations=1.&quot;</span></p>
<p style="line-height: 100%; margin-bottom: 0cm">Лучше ее
успеть скопировать — она пригодится
для построения графика.</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">После
завершения работы макроса в директории
/<span lang="en-US">tmp/ </span>появятся файлы <span lang="en-US">csv
</span>с данными акселерометра под каждый
прогон  головы.</p>
<p style="line-height: 100%; margin-bottom: 0cm">Эти файлы
нужно обработать с помощью скрипта.</p>
<p style="line-height: 100%; margin-bottom: 0cm">В консоли
Клиппера вводим команду, которую
скопировали в начале работы макроса.</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">python3
chopper_plot.py --current_min=2000 --current_max=2000 --tbl_min=0
--tbl_max=0 --toff_min=8 --toff_max=8 --hstrt_hend_max=10
--min_hstrt=7 --max_hstrt=7 --min_hend=3 --max_hend=3 --min_speed=20
--max_speed=150 --iterations=1</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">Скачиваем
из директории /</span>tmp/ <span lang="ru-RU">файл
interactive_plot.html и открываем его в браузере.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><img src="guide_ru_html_be9b002b6ba5f593.gif" name="Image1" align="left" width="643" height="368" border="0"/>
<br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">На графике
будет обычно 2 пика. На скорости около
50мм/с и 100мм/с. Это «рябые» скорости.</p>
<p style="line-height: 100%; margin-bottom: 0cm">Нам нужна
меньшая из этих скоростей. Например,
55мм/с.</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm">Удаляем все
файлы из директории /<span lang="en-US">tmp/</span></p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm">4.2.
<span lang="ru-RU">Запускаем макрос для перебора
всех вариантов чоппера на выбранной
ранее скорости.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">CHOPPER_TUNE_AWD
CURRENT_MIN_mA=2000 CURRENT_MAX_mA=2000 TBL_MIN=0 TBL_MAX=</span>3<span lang="ru-RU">
TOFF_MIN=</span>2<span lang="ru-RU"> TOFF_MAX=8 HSTRT_HEND_MAX=10
MIN_HSTRT=</span>0<span lang="ru-RU"> MAX_HSTRT=7 MIN_HEND=</span>2<span lang="ru-RU">
MAX_HEND=</span>15<span lang="ru-RU"> MIN_SPEED=</span>55<span lang="ru-RU">
MAX_SPEED=</span>55<span lang="ru-RU"> TRAVEL_DISTANCE=150
ITERATIONS=1</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">Сбор
данных будет проходить около 2 часов.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">После
окончания работы макроса запускаем
скрипт, с параметрами из консоли. В нашем
примере это:</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">python3
chopper_plot.py --current_min=2000 --current_max=2000 --tbl_min=0
--tbl_max=3 --toff_min=2 --toff_max=8 --hstrt_hend_max=10
--min_hstrt=0 --max_hstrt=7 --min_hend=2 --max_hend=15 --min_speed=55
--max_speed=55 --iterations=1</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">Получаем
график вида </span>
</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU"><br/>
В<img src="guide_ru_html_9929da4901f57105.gif" name="Image2" align="left" width="643" height="384" border="0"/>

этом примере минимальные вибрации при
</span>tbl=0 <span lang="ru-RU">и </span>toff=8.<span lang="ru-RU">
Увеличиваем эту область.</span></p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"> 
</p>
<p lang="en-US" style="line-height: 100%; margin-bottom: 0cm"><span lang="ru-RU">В<img src="guide_ru_html_d88ec45bc0faafec.gif" name="Image3" align="left" width="643" height="365" border="0"/>
ыбираем
вариант чоппера с минимальным значением
магнитуды - это искомые параметры
чоппера.<br/>
Можно повторить процедуру
с меньшими вариациями чоппера, например,
только </span>tbl=0 <span lang="ru-RU">и </span>toff=8<span lang="ru-RU">
и перебрать</span> hstrt<span lang="ru-RU"> и</span> hend,<span lang="ru-RU">
но с большим количеством повторений</span>
iterations.<span lang="ru-RU"> В этом случае график
будет построен по средним результатам,
чтобы уменьшить влияние механики на
показания.</span></p>
</body>
</html>
