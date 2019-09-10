# CS 2302 Data Structures: MW 1:30PM - 2:50PM
# Author: Stephanie Galvan
# Assignment: Lab 1 - Password Cracking
# Instructor: Diego Aguirre
# TA: Gerardo
# Date of last modification: September 9, 2019
# Purpose: Given a file containing users, salt values, and hashed passwords, create a recursive method 
#          that uses brute force to generate all users passwords. 

import hashlib
import time

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def find_password(password):
    with open("password_file.txt") as f:
        for curr_line in f:
            # Split the file by users, salt values, and hashlines
            elements = curr_line.split(",")
            # Get the hashline of the corresponding user
            hashline = elements[2].replace('\n', '')
            # Create a new hashline with the password provided and the corresponding user salt value
            new_hashline = hash_with_sha256(password + str(elements[1]))
            # Print the user and password if the real password was found
            if new_hashline == hashline:
                print(elements[0] + ': ' + password)


def get_combination(size, comb):
    # Once a combination of size n is found, call find_password
    if size == 0:
        find_password(comb)
    else:
        # Create combination by using digits from 0-9
        for digit in range(0, 10):
            new_comb = comb
            new_comb += str(digit)
            get_combination(size - 1, new_comb)


def hack_file(start, end):
    # Check parameter's data type
    if not isinstance(start, int) or not isinstance(end, int):
        print('Invalid input. Please try again')
        return
    if start < 3 or end > 7:
        print('Invalid input. Please try again')
        return
    for size in range(start, end + 1):
        get_combination(size, '')


def test_cases():
    # Invalid data types
    start = time.time()
    hack_file(3.0, 7.0)
    end = time.time()
    print('Running time for invalid data type:', end - start, 'seconds\n')
    # Small starting size
    start = time.time()
    hack_file(2, 7)
    end = time.time()
    print('Running time for invalid data type:', end - start, 'seconds\n')
    # Large end size
    start = time.time()
    hack_file(3, 8)
    end = time.time()
    print('Running time for invalid data type:', end - start, 'seconds\n')


def main():
    # Normal run of the program
    start = time.time()
    hack_file(3, 7)
    end = time.time()
    print('Running time for normal run: ', end - start, 'seconds\n')
    test_cases()


main()
