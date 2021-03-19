/* Exploration of multiplicative errors using Bessel functions */
#include <iostream>
#include <cmath>

typedef float number;

number myBessel(number l, number x);

int main(int argc, char **argv)
{
  std::cout.precision(7);
  std::cout.setf(std::ios::scientific);
  number x = 1;

  int L=25;
  std::cout << "  n  " << '\t'
            << "my Bessel(n," << x << ")" << '\t'
            << "  j(n," << x << ")  " << '\n';
  for(number n = 23; n >= 0; n--)
  {
  std::cout << n << '\t' << myBessel(n,x)  << '\t'  <<  std::sph_bessel(n,x) << '\n';
  }


}

number myBessel(number l, number x)
{
  unsigned L = 25;
  number JL = std::sph_bessel(L,x);
  number JL1 = std::sph_bessel(L+1,x);
  number J;


  for(int ll = L; ll >= l+1; ll--)
  {
    J = (2*(ll) + 1)*JL/x - JL1;
    JL1 = JL;
    JL = J;
  }
  return J;

}
