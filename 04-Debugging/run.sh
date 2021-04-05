echo which file do you want to run?
echo Select 1 or 2
read n
if [ $n -eq 2 ]
then	
	echo with valgrind or sanitizers? write v or s
	read tool
	if [ $tool == 's' ]
	then
		echo compiling 2-example-II.cpp
		g++ -g -fsanitize=address -fsanitize=leak 2-example-II.cpp
		echo running...
		./a.out	
	elif [ $tool == 'v' ]
	then
		echo compiling 2-example-II.cpp
		g++ -g 2-example-II.cpp
		echo running...
		valgrind --tool=memcheck --leak-check=full --track-origins=yes ./a.out 
	fi
elif [ $n -eq 1 ]
then
	echo compiling 1-example-I.cpp
	g++ -g -fsanitize=address -fsanitize=leak 1-example-I.cpp
	echo running...
	./a.out	
fi
