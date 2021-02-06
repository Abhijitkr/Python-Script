#!C:\Users\Abhijit\AppData\Local\Programs\Python\Python39/python
print("Content-Type: text/html")
print()
import cgi, os
print("<link rel='stylesheet' href='style.css'>")
form = cgi.FieldStorage()

file_name = form.getvalue("file_name")
input_path = form.getvalue("input_path")
search = os.walk(input_path)

caseInSensitive = form.getvalue("CIS")
# caseSensitive = form.getvalue("CS")

file_found = False

print("<h1>Search Result</h1><hr>")

for path, folder, files in search:
    for f in files:
        if(caseInSensitive):
            if (file_name.lower() == f.lower()):
                file_found = True
                print("<p class='file_name'>", f,"</p> found in <p class='path'>", path, "</p><br/>")
        else:        
            if (file_name == f):
                    file_found = True
                    print("<p class='file_name'>", f,"</p> found in <p class='path'>", path, "</p><br/>")
                
if (not file_found):
    print('<h2 class="not_found">File not found!</h2>')

