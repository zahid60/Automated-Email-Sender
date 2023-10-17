import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

# Replace 'Your Mail' with your Gmail email address
# Replace 'Your password' with your Gmail password
ob.login('Your Mail', 'Your password')

subject = "Test python"
body = "I love python"
message = "Subject:{}\n\n{}".format(subject, body)

listadd = ['zshanto300@gmail.com', 'zahidhasan9960@gmail.com']

# Replace 'Your Mail' with your Gmail email address
ob.sendmail('Your Mail', listadd, message)

print("Send Mail")
ob.quit()
