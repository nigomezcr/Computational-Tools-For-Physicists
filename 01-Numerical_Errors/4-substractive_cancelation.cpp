/* Exploration to the subtractive cancelation in the solutions of ax^2 + bx + c = 0 */
#include<iostream>
#include <cmath>

double x1(double a, double b, double c);
double x2(double a, double b, double c);
double xp1(double a, double b, double c);
double xp2(double a, double b, double c);

int main(int argc, char **argv)
{
	std::cout.precision(15);
	std::cout.setf(std::ios::scientific);
	double a, b, c;
	a = 1;
	b = 1;

	std::cout << "Solutions to the quadratic equation with a=" << a << ", b=" << b << ", c=10^(-n) "<< '\n';
	std::cout << "n" << '\t'
						<< "   	   x_1      " << '\t'
						<< "   	   x_2      " << '\t'
						<< "   	   x'_1     " << '\t'
						<< "   	   x'_2     " << '\n';
	int N = 10;

	for(int n = 1; n<= N; n++)
	{
		c = std::pow(10,-n);


		std::cout << n << '\t'
							<< x1(a,b,c) << '\t'
		 					<< x2(a,b,c) << '\t'
		 					<< xp1(a,b,c) << '\t'
		 					<< xp2(a,b,c) << '\n';
	}

	std::cout << "Most precise solutions: x'_1 & x_2 " << '\n';
	return 0;
}


double x1(double a, double b, double c)
{
	return (-b + std::sqrt(b*b -4*a*c))/(2*a);
}

double x2(double a, double b, double c)
{
	return (-b - std::sqrt(b*b -4*a*c))/(2*a);
}

double xp1(double a, double b, double c)
{
	return -2*c/(b+std::sqrt(b*b - 4*a*c));
}

double xp2(double a, double b, double c)
{
	return -2*c/(b-std::sqrt(b*b - 4*a*c));
}
