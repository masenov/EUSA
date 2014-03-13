EUSA
====

The software was written using:

Django - 1.6.2 final
Python - 2.7.5 final


Tested on:

Ubuntu - 13.10
Chrome - 33.0.1750.149

How to setup:

1)Download the code
2)Go to EUSA/mysite/mysite/ and open settings.py
3)Edit:

  EMAIL_HOST              = 'smtp.gmail.com'
  EMAIL_HOST_USER         = 'sender@email.com'               #enter username for your email
  EMAIL_HOST_PASSWORD     = 'password'                       #enter password for your email
  EMAIL_PORT              = 587
  EMAIL_USE_TLS           = True
  
  So they match the settings of your email, you are going to use to send feedback.
4) In the same file edit "ADMINS" at the bottom so it sends the emails to all the admins you wish
5)Go to the parent directory(EUSA/mysite) and open a terminal windows there
6)Type
  $ python manage.py syncdb
7)Create admin user when prompted
8)Type
  $ python manage.py runserver
9) Go to:
  http://127.0.0.1:8000/polls/ - main website
  http://127.0.0.1:8000/admin/ - admin panel
