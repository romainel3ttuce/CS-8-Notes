Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
11 + 56
67
23 - 54
-31
4 * 5
20
8 / 4
2.0
8 / 5
1.6

# This is a comment. Whatever comes after the # is not executed.
# 3 + 4

# Float stands for "floating-point number"
# Floating-point numbers are approximations to real numbers.
# Division (/) produces a float.
type(3)
<class 'int'>
type(3.0)
<class 'float'>
8 / 4
2.0
8 // 4
2
# // is integer division. It produces an int.
8 // 5
1
8 % 5
3
# % is modulo (remainder).
4 + 5 * 3
19
(4 + 5) * 3
27
# ** is exponentiation
2 ** 5 # 2 to the power of 5
32

# ARITHMETIC OPERATOR PRECEDENCE:
# Order of precedence (highest to lowest)
# **
# - (negation)
# *, /, //, %
# + (addition), - (substraction)

4 + 5 * 3
19
4 + (5 * 3)
19
(4 + 5) * 3
27
5 + 2 ** 3 * 5
45
5 + ((2 ** 3) * 5)
45
5 - -2
7
5 - --2
3
5 - -------------2
7
5 -------------2
3

# BASIC ERRORS:
2 * * 5
SyntaxError: invalid syntax
3 +
SyntaxError: invalid syntax
4 + 5) * 4
SyntaxError: unmatched ')'
4 / 0
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    4 / 0
ZeroDivisionError: division by zero

# BUILT-IN FUNCTIONS:
type(45)
<class 'int'>
type(56.2342)
<class 'float'>
min(34, 12)
12
min(12, 45, 76)
12
max(12, 45, 76)
76
max(34.25, 564.34)
564.34
max(34.25, 564)
564
>>> abs(-56)
56
>>> abs(-453.234)
453.234
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> abs(34)
34
>>> help(pow)
Help on built-in function pow in module builtins:

pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> pow(2, 5) # 2 ** 5
32
>>> pow(2, 5, 3) # (2 ** 5) % 3
2
>>> help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

>>> round(4.56789)
5
>>> round(4.56789, 3)
4.568
