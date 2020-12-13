import os

file_name = raw_input("Enter the File name to be searched: ")
input_path = raw_input("Enter the path to search for the file: ")

search = os.walk(input_path)

#t = 'r"{}"'.format(input_path)
# file_name = "test.py"
# search = os.walk(r"C:\Users\Abhijit\Desktop")

file_found = False

for path, folder, files  in search:
    if (file_name in files):
        file_found = True
        print file_name,"found in", path

if (not file_found):
    print "File not found"

