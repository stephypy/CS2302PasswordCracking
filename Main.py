# CS 2302 Data Structures: MW 1:30PM - 2:50PM
# Author: Stephanie Galvan
# Assignment: Lab 1 - Password Cracking
# Instructor: Diego Aguirre
# TA: Gerardo
# Date of last modification: September 8, 2019
# Purpose: Given a file containing users, salt values, and hashed passwords, create a recursive method 
#          that uses brute force to generate all users passwords. 

import hashlib
import itertools

# Provided function for hashing
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def hack_password(pass_length):
    # List that will contain corresponding passwords for users
    passwords = []
    # Check parameter's data type
    if not isinstance(pass_length, int):
        print('Invalid data type: Only pass integers between 3 and 7 (inclusive)')
        return
    # Password will be at least 3 digits long and at most 7 digits long
    if pass_length < 3 or pass_length > 7:
        passwords.sort()
        return passwords
    # Create all the possible combinations of the following digits of n length
    num_combination = list(itertools.product(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], repeat=pass_length))
    # Keep count of the file lines
    count = 0
    # It will iterate each num_combination of length pass_length through each line in the file
    for i in num_combination:
        with open("password_file.txt") as f:
            for curr_line in f:
                count += 1
                elements = curr_line.split(",")
                # This is the corresponding hashed line of the current line
                hash_element = elements[2].replace('\n', '')
                # This is a possible password for the user at current line
                curr_num = ''.join(i)
                # Call method to hash the possible password plus salt value
                hashline = hash_with_sha256(curr_num + str(elements[1]))
                # When a password is found, add it to the list of passwords
                if hashline == hash_element:
                    passwords.append(elements[0] + ': ' + curr_num)
                # At the end of the file, make a recursive call by incrementing the length of pass_length
                if count ==  100:
                    passwords += hack_password(pass_length + 1
    passwords.sort()
    return passwords


def test_cases():
    # Pass a higher parameter than expected:
    higher = hack_password(8)
    print(higher)
    print('')
    # Pass a lower parameter than expected:
    lower = hack_password(0)
    print(lower)
    print('')
    # Pass an invalid parameter i.e.: a string, float, etc
    print(hack_password(4.5))
    print('')
  
  
def main():
    # Test cases:
    test_cases()
    # Normal run of the program:
    print(hack_password(3))


main()
