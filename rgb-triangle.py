#!/usr/bin/python3

from random import choice, randint

side_len = randint(5, 10) # Length of bottom row of triangle
char_set = ['R', 'G', 'B']
bottom_row = [choice(char_set) for i in range(side_len)]


def find_next_char(char1, char2):
    if char1 == char2:
        return char1

    list_of_chars = [char for char in char_set] # Can't use list_of_chars = char_set due to Pass By Object Reference nature of Python
    list_of_chars.remove(char1)
    list_of_chars.remove(char2)

    return list_of_chars[0]


def print_triangle(triangle):
    for i in range(len(triangle)):
        print(" " * (len(triangle) - i), end="") # Add spaces before each row to make triangle isoceles and symmetric
        print(" ".join(triangle[i]))


triangle = []
current_row = bottom_row
while(len(current_row) > 1):
    next_row = []
    for i in range(len(current_row) - 1): # Don't go to last element, otherwise list index out of range on next line
        next_char = find_next_char(current_row[i], current_row[i+1])
        next_row.append(next_char)
    current_row = next_row # Update row
    triangle.append(current_row)

triangle = triangle[::-1] # Swap rows so smallest first
print_triangle(triangle)
