CXXFLAGS = -g -std=c++11
DEBBUGFLAGS = -fsanitize=address -fsanitize=leak -fsanitize=undefined

all: main.x

%.o: %.cpp
	g++ -c $(CXXFLAGS) $(DEBBUGFLAGS) $^

main.x: main.o factorial.o
	g++ $^ $(CXXFLAGS) $(DEBBUGFLAGS) -o $@

############################################################

test: test_factorial.x test_catch2.x test_googletest.x
#	./$<

test_factorial.x: test_factorial.o factorial.o
	g++ $^ $(CXXFLAGS) $(DEBBUGFLAGS) -o $@

test_catch2.x: test_catch2.o factorial.o
	g++ $^ -o $@

test_googletest.x: test_googletest.o factorial.o
	g++ $^ -o $@


clean:
	rm -f *.x *.o a.out
