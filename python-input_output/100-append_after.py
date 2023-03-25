def append_after(filename="", search_string="", new_string=""):
    # Open the file for reading and writing using with statement
    with open(filename, mode='r+', encoding='utf-8') as f:
        # Read the contents of the file into a list
        lines = f.readlines()

        # Loop over the lines and find the lines containing the search string
        for i in range(len(lines)):
            if search_string in lines[i]:
                # Insert the new string after the line containing the search string
                lines.insert(i+1, new_string)

        # Write the modified contents back to the file
        f.seek(0)
        f.writelines(lines)
