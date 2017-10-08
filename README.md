# nagwa-floating-point-arithematic

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. While Decimal Fraction is in base 10.

0.125 is 1/10 + 2/ 100 + 5/1000
0.125 is 0/2 + 0/4 + 1/8

The decimal floating-points numbers are only approximated to binary floating-points.

Representation error refers to the fact that some (most, actually) decimal fractions cannot be represented exactly as binary (base 2) fractions. This is the chief reason why Python (or Perl, C, C++, Java, Fortran, and many others) often won’t display the exact decimal number you expect.

The problem is that most decimals can’t be represented as a binary fraction. For example 0.1 has an infinite representation in binary format. So computers take a significant number of 

Similar to the representation of 1/3 in base-10.

This is the problem in general. Other programming languages as well as Python use different ways to approach this, including only displaying the number to 17 binary places, other round.

One of the glaring cases is .1 + .1 +.1 != .3, and since the .1 can’t get any closer to 1/10, and .3 can’t get any closer to 1/3, even using the rounding function won’t make a difference.

Almost all machines today use IEEE-754 floating point arithmetic, and almost all platforms map Python floats to IEEE-754 “double precision”. 754 doubles contain 53 bits of precision, so on input the computer strives to convert 0.1 to the closest fraction it can of the form J/2**N where J is an integer containing exactly 53 bits. 

Usually people use string formatting options to format floating point in the appropriate format.

Also Python offers a decimal module for high-precision and accounting applications. Their Moto is that “Floating point arithmetic and rounding should work as people learn it in schools”

Also Fractions module offers accurate representation when it comes to fractions, and Numpy offers multiple approaches to the rounding issues and the errors.

Also math.fsum function which helps mitigate loss-of-precision during summation. It tracks “lost digits” as values are added onto a running total. That can make a difference in overall accuracy so that the errors do not accumulate to the point where they affect the final total.
 

Useful Links:
* Floating Point Arithmetic: https://docs.python.org/3/tutorial/floatingpoint.html
* Decimal Module: https://docs.python.org/3/library/decimal.html
* Fractions Module: https://docs.python.org/3/library/fractions.html#module-fractions
* What Every Computer Scientist should know about Floating points: http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
* IEEE-754 Standard: https://en.wikipedia.org/wiki/IEEE_754#Basic_formats
* Is Floating Point Math Broken: https://stackoverflow.com/questions/588004/is-floating-point-math-broken
