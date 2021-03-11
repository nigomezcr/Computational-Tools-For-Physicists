/* C++ program to test underflow and overflow*/
#include <iostream>
#include <cstdlib>



int main(int argc, char *argv[])
{
    // argc : count number of arguments in command line
    // argv : save the values of those arguments
    std::cout.precision(15);
    std::cout.setf(std::ios::scientific);


    double under = 1.0, over = 1.0;
    int N = std::atoi(argv[1]); //transforms char -> int
    //std::cout << N << "\n";
    for (int ii = 0; ii < N; ii++) //For N = 1074 returns 0 and inf
    {
        under /= 2.0;
        over  *= 2.0;
        std::cout << ii
                  << "\t" << under
                  << "\t" << over
                  << "\n";
    } 

    return 0;
}
