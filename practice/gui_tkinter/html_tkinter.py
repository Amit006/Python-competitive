#c:\python3.4\python.exe
import cgi
import cgitab
import mysql.connector
  

cgitab.enable(display=1, logdir=None, context=5, format="html")
form = cgi.FieldStorage()
Fname = form.getvalue('f')
print('Content-type: text/html')
print('location: ../python_cgi/first.html?t=99')