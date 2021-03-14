/* Complex numbers and functions in c++ */
#include<iostream>
#include<complex>
#include<iomanip>
#include<cmath>

using namespace std::complex_literals;

int main(int arcg, char **argv)
{
  std::cout << std::fixed << std::setprecision(2);

  //Decare complex numbers
  std::complex<double> z , e, ln, root;
  double arctan;

  //Declare norm and phase
  double r;
  double phi;

  std::cout << "phi" << "\t" << "x" << "\t" << "y" << "\t"
            << "    e^z    " << "\t" << "   ln(z)   " << "\t"
            << "   sqrt(z) " << "\t" << " atan(y/x)   " << "\n";

  std::cout << "---------------------------------------------------------------------------------" << '\n';
  //Loop over phases
  for(phi = -4*M_PI; phi <= 4*M_PI; phi+= M_PI_4 )
  {
  //Assign a value to it
  r = 2;
  z = r*exp(1i * phi);

  //Compute real and imaginary parts
  double x = real(z);
  double y = imag(z);

  //Compute some complex functions
  e = exp(z);
  ln = log(z);
  root = sqrt(z);
  arctan = std::atan(y/x);

  std::cout << phi << "\t" << x << "\t" << y << "\t" << e << "\t" << ln << "\t"<< root << "\t" << arctan << "\n";

  }

  return 0;
}
