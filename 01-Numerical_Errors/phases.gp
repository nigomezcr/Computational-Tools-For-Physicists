set terminal pdf
set output "phases_cpp.pdf"

set title "Input phases vs atan"
set xlabel "input phi"
set ylabel "atan(y/x)"

p 'phases.txt' u 1:7 t "" w l lt 4
