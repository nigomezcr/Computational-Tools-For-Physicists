# This is a commentary
# @: target
# ^: all dependencies
# <: first dependency

CXX = g++
CXXFLAGS = -O2 -g -std=c++11

all: run

%.x: 1-%.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

%.txt: %.x
	./$< > $@

run: make.sh
	@echo "running makefile"
	bash $<

python_plot.pdf: plot.py sum.txt
	python3 $<

gnuplot_plot.pdf: plot.gp sum.txt
	gnuplot $<

clean:
	rm -f a.out *.x *.txt *~