set term pdf
set out "gnuplot_sum.pdf"

set xlabel "n max"
set ylabel "|Sumup - Sumdown|"
set key left top

p 'sum.txt' u 1:2 t "Data" w lp lt 2 pt 3 ps 1.5