# CS2302: PasswordCracking
CS 2302 Data Structures: MW 1:30PM - 2:50PM <br />
**Author:** Stephanie Galvan <br />
**Assignment:** Lab 1 - Password Cracking <br />
**Instructor:** Diego Aguirre <br />
**TA:** Gerardo <br />
**Date of last modification:** September 8, 2019 <br />
**Purpose:** Given a file containing users, salt values, and hashed passwords, create a recursive method that uses brute force to generate all users passwords. <br />

(From lab description): <br />
  *The file is divided as username,salt value, hashed password <br />
  *The passwords only contain numbers (length range is 3-7) <br />
  *Can only have up to two nested loops inside the function <br />
  *Use the provided method [hashlib.sha256()] to find the solution  <br />
  *Implementation of test cases <br />
  *This program runs in Python 3.7 (originally coded in pycharm) <br />
  
  Discuss- Time Complexity: <br />
   Since this program is meant to use brute force to find passwords from a file, there are four main concerns: <br />
    1. Calculation of combinations <br />
    2. Nested for loops <br />
    3. Calling an additional method <br />
    4. Recursive call <br />
    However, it is possible to determine the best and worst cases of the program: <br />
    1. Best cases: <br />
     * When an invalid parameter is passed (because the program will immeadiately return and end the function) <br />
     2. Worst cases: <br />
     * Regular run with the initial parameter of 3 (here's the calculations  in which first the combinations of lenght n are calculated and compared to each 100 lines of the file) <br />
     First call (parameter = 3): [10! * 10! * 10!] * 100 <br />
     Second call (parameter = 4): [10! * 10! * 10! * 10!] * 100 <br />
     Third call (parameter = 5): [10! * 10! * 10! * 10! * 10!] * 100 <br />
     Fourth call (parameter = 6): [10! * 10! * 10! * 10! * 10! * 10!] * 100 <br /> 
     Last call (parameter = 6): [10! * 10! * 10! * 10! * 10! * 10! * 10!] * 100 <br />
     The addition of the numbers above refer to the total number of needed iterations
 
     
