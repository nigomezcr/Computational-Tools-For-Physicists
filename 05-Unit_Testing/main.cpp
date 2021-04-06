#include <iostream>
#include <cstdlib>
#include "factorial.hpp"

// main
int main(int argc, char **argv)
{
    int n = std::atoi(argv[1]);
    std::cout << "Factorial of " << n << " is : " << factorial(n) << "\n";
    return 0;
}
