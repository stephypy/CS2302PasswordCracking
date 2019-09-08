# CS 2302 Data Structures: MW 1:30PM - 2:50PM
# Author: Stephanie Galvan
# Assignment: Lab 1 - Password Cracking
# Instructor: Diego Aguirre
# TA: Gerardo
# Date of last modification: September 8, 2019
# Purpose:

import hashlib
import itertools


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def hack_password(pass_length):
    # Create all the possible combinations of the following digits of n length
    num_combination = list(itertools.product(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], repeat=pass_length))
    # List that will contain corresponding passwords for users
    passwords = []
    # Check parameter's data type
    if not isinstance(pass_length, int):
      print('Invalid data type: Only pass integers between 3 and 7 (inclusive)')
      return
    # Password will be at least 3 digits long and at most 7 digits long
    if pass_length < 3 or pass_length > 7:
        return passwords.sort
    for i in num_combination:
        with open("password_file.txt") as f:
            for curr_line in f:
                elements = curr_line.split(",")
                hash_element = elements[2].replace('\n', '')
                curr_num = ''.join(i)
                hashline = hash_with_sha256(curr_num + str(elements[1]))
                if hashline == hash_element:
                    passwords.append(elements[0] + ': ' + curr_num)
    passwords += hack_password(pass_length + 1)


def test_cases():
    # Pass a higher parameter than expected:
    hack_password(8)
    
    #Pass a lower parameter than expected:
    hack_password(0)
    
    #Pass an invalid parameter i.e.: a string, boolean, etc
    hack_password('hello')
  
  
def main():
    # Test cases:
    test_cases()
    # Normal run of the program:
    hack_password(3)


main()
