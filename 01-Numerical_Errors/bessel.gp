set terminal pdf
set output "bessel_cpp.pdf"

set title "Multiplicative errors"
set logscale y
set xlabel "l"
set ylabel "j_l (x = 1)"

p 'bessel.txt' u 1:4 t "" w p ps 2
