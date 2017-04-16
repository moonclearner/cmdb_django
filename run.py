import os
#  import commands


#  os.system('python manage.py runserver 127.0.0.1:8080')

out = os.popen('dir')
print out.read()
out = os.popen('python manage.py runserver 127.0.0.1:8080')
print out.read()


# commands only excute bash cmd not python command
#  output = commands.getoutput('python manage.py runserver 127.0.0.1:8080')
#  print output
