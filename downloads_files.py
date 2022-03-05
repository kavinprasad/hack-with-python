import requests

def download(url):
  get_response = requests.get(url)
  file_name = url.split("/")[-1]
  with open(file_name, "wb") as out_file:
    out_file.write(get_response.content)
  
download ("https://www.audi.com/content/dam/gbp2/experience-audi/audi-sport/audi-racing-models/r8-lms-gt4/2020/1920x840_1920x840_CROPPED_R8RWD25657-B-R.jpg")


