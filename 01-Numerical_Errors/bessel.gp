set terminal pdf
set output "bessel_cpp.pdf"

set title "Multiplicative errors"
set logscale y
set xlabel "l"
set ylabel "j_l (x = 1)"

p 'bessel.txt' u 1:2 t "My bessel" w p ps 2, '' u 1:3 t "std bessel" w l lt 2 lw 2
