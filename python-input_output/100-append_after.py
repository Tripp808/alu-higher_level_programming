#!/usr/bin/python3
"""Module that inserts a line of text to a file, after each line containing a specific string"""

def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file, after each line containing a specific string"""
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

if __name__ == '__main__':
    # Testing the function
    append_after("c", "Python is cool!\n", "file = c is fun!\n")
    append_after("nop", "Python is cool!\n", "file = Nop, nothing here Really nothing \n")
    append_after("c_is_fun", "Python is cool!\n", "file = Here c is fun Holberton School c is fun c is fun We are Holberton c is fun\n")
    append_after("big_text", "Python", "file = Big text\n")
    append_after("non_existent_file", "Python", "file = Non-existent file\n")
