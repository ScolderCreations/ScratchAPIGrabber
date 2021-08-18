# You are free to use this program in any situation, private or public. In public situations, you should provide credit.

print("loading...")
import sys
print("credit:")
print("Code made by ScolderCreations. API made by the Scratch Team.") # don't remove this
print()
import requests # NOTE: you'll need to install this module first
INFO = "lol wut" # impossible value
wanna = "yes" # prevents program from instantly ending

def updinf(parameter):
  INFO = INFO + parameter

if "preset" in webargumen: # preset argument
  datType = input("What type of data do you want? 1: User 2: Project ") 
  if "1" in datType:
    INFO = "/users/" + input("What is your username? ")
    datType = input("Data? 1: Studio List 2: Project List 3: Followers 4: Favorites 5: General ") # additional user data
    if "1" in datType:
      updinf("/studios/curate/")
    elif "2" in datType:
      updinf("/projects/")
    elif "3" in datType:
      updinf("/followers/")
    elif "4" in datType:
      updinf("/favorites/")
    elif "5" in datType:
      updinf("/")
    else:
      print("...")
      print("You IDIOT.")
      updinf("/")
      print()
  elif "2" in datType:
    INFO = "/projects/" + input("insert a Project ID: ")
  else:
    INFO = input("Please insert parameters ")
elif "y" in input("Use a preset? "): # nonpreset argument
  datType = input("What type of data do you want? 1: User 2: Project ")
  if "1" in datType:
    INFO = "/users/" + input("What is your username? ") + "/"
  elif "2" in datType:
    INFO = "/projects/" + input("insert a Project ID: ") + "/"
  else:
    INFO = input("Please insert parameters ")
else:
  INFO = input("Please insert the parameters ")
if input("Any extra parameters? y/n ") = "y":
  updinf(input("Custom paramaters: "))
url = 'https://api.scratch.mit.edu' + INFO
print()
print("url: \"" + url + "\"")
bar = requests.get(url, allow_redirects = False)
print()
print(bar.text)
print()
print("done!")
