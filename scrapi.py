print("loading...")
import requests
INFO = "lol wut"
wanna = "yes"
if "y" in input("Use a preset? "):
  datType = input("What type of data do you want? 1: User 2: Project ")
  if "1" in datType:
    INFO = "/users/" + input("What is your username? ")
  elif "2" in datType:
    INFO = "/projects/" + input("insert a Project ID: ")
  else:
    INFO = input("Please insert parameters ")
else:
  INFO = input("Please insert the parameters ")
url = 'https://api.scratch.mit.edu' + INFO
print()
print("url: \"" + url + "\"")
bar = requests.get(url, allow_redirects = False)
print()
print(bar.text)
print()
print("done!")
