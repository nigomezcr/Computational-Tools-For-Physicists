# Computational-Tools-For-Physicists

Taken from prof. Oquendo's lectures on Computational Tools for Physicists in Universidad Nacional de Colombia: https://iluvatar.bitbucket.io/HerrComp/#orgcbd4a91

## 1 Numerical Errors

Survey of examples of most common numerical errors in scientific computing:
* Overflow and underflow
* Precision limit
* Subtractive cancelation
* Multiplicative errors

plus some handling of complex numbers.

## 2 Makefiles

Use of makefiles or bash scripts to make automatic compilation, running and compiling. Use as

> make

or

> make *instruction*

For use in a different folder:

> make -f $HOME/path/to/Makefile


## 3 Installing Program

Examples of programs installed from source.

### Compiling of installed libraries
In c++, compiling with g++, use:

> g++ -I $HOME/local/include -L $HOME/local/bin/filename.cpp -llibname

if the header are in $HOME/local/include and the libraries are in $HOME/local/bin

### Using spack

To see available programs use

> spack list

install a program with

> spack install *prog*

Use also 

> spack info *prog*

to know about different versions and general information of the program.
Load program with

> spack load *prog*


## 4 Debugging

### Using debuggers
Examples of codes to debug with some useful tool. In c++: gdb; in python: pydb.
Notes: *Debugging* is **identifying** and **correcting** the cause of an error.
Using a debugger in c++ (gdb):
* When compiling use -g
* Launch debugger in terminal: gdb ./file.executable
* Some comands:
  * run: starts executable
  * continue: continues stopped program
  * finish: continues until the end of a subroutine
  * step: single steps line by line
  * next: single steps but doesn't step into subroutines
  * print: displays contents of a known data object
  * display: like print but shows updates every step
  * where: show stack trace or function calls
  * up down: allows to move up/down on the stack
  * break: sets break point indicated by file name+line or function
  * watch: sets a conditional break point.
  * delete: removes display or break points.
  * list: shows the code.
  * Ctrl+d: quit
* Launch debugger with user interface: gdb --tui ./file.executable
* Launch debugger on emacs: ESC-x -> gdb --> ESC-x --> dgb-many
* * Ctrl+x-o: move between windows

More infor on: https://bitbucket.org/iluvatar/scientific-computing-part-01/wiki/browse/Debugging

### Using flags

**Sanitizers**:

Use them during compilation as 

> g++ -fsanitize=___

* address: verifies that we're not reading memory addresses that we shouldn't read.
* leak: detects memory leaks

**Valgrinds**:

Use them while running as 

> valgrind ____  ./file.executable

* --tool=memcheck: detects memory errors
* --leak-check=full
* --track-origins=yes

## 5 Unit Testing

Allows to ensure that a given software behaves in the correct way, at least for the cases one is testing.
