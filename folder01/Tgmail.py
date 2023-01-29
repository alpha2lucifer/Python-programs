import smtplib # ~~~ITS THE LIBRARY TO SEND MAILS~~~
'~~~~~~~~~~~~~~~~~~~~~'
s = smtplib.SMTP('smtp.gmail.com', 587) # ~~~ITS THE LIBRARY'S GMAIL AND AUTHENTICATION CODE~~~
'~~~~~~~~~~~~~~~~~~~~~'
s.starttls() # ~~~IT STARTS THE MAIN FUNCTION~~~
'~~~~~~~~~~~~~~~~~~~~~'
Myemail = input(" ") # ~~~ENTER YOUR EMAIL~~~
'~~~~~~~~~~~~~~~~~~~~~'
Mypassword = input(" ") # ~~~ENTER YOUR PASSWORD~~~
'~~~~~~~~~~~~~~~~~~~~~'
Receiversemail = input(" ") # ~~~EMAIL ID OF RECEIVER~~~
'~~~~~~~~~~~~~~~~~~~~~'
s.login(Myemail, Mypassword)
'~~~~~~~~~~~~~~~~~~~~~'
message = "My message" # ~~~TYPE MESSAGE YOU WANT TO SEND~~~
'~~~~~~~~~~~~~~~~~~~~~'
s.sendmail(Myemail, Receiversemail, message)
'~~~~~~~~~~~~~~~~~~~~~'
s.quit() # ~~~IT ENDS THE MAIN FUNCTION~~~
