# You are free to use this program in any situation, private or public. In public situations, you should provide credit.

print("")
INFO = ""  # impossible value
import sys
import time
print("credit:")
print("Code made by ScolderCreations. API made by the Scratch Team."
      )  # don't remove this
print("loading...")
import requests  # NOTE: you'll need to install the module before running the script, otherwise this whole script is useless to you.


def test():
	requests.get("https://api.scratch.mit.edu", allow_redirects=False)


for i in range(1, 5):
	test()
wanna = "yes"  # prevents program from instantly ending
INFO2 = ""
TRUE = ""


def updinf(type, parameter, extra):
	INFO2 = "https://api.scratch.mit.edu"
	print("parameters: " + extra + parameter)
	TRUE = f"{INFO2}{extra}{parameter}"
	return (TRUE)


datType = input("What type of data do you want? 1: User 2: Project ")
if "1" in datType:
	INFO = "/users/" + input("What is the username? ")
	datType = input(
	    "Data? 1: Studio List 2: Project List 3: Followers 4: Favorites 5: General "
	)  # additional user data
	if "1" in datType:
		INFO = updinf("users", "/studios/curate/", INFO)
	elif "2" in datType:
		INFO = updinf("users", "/projects/", INFO)
	elif "3" in datType:
		INFO = updinf("users", "/followers/", INFO)
	elif "4" in datType:
		INFO = updinf("users", "/favorites/", INFO)
	elif "5" in datType:
		INFO = updinf("users", "/", INFO)
	else:
		print("...")
		print("You IDIOT.")
		updinf("users", "/", INFO)
		print()
elif "2" in datType:
	INFO = "https://api.scratch.mit.edu/projects/" + input("insert a Project ID: ")
else:
	INFO = input("Please insert parameters ")
if input("Any extra parameters? y/n ") == "y":
	INFO += input("Custom paramaters: ")
print("loading url " + INFO)
url = INFO
print()
print("url: \"" + url + "\"")
bar = requests.get(url, allow_redirects=False)
print()

print("What will you do with the contents? 1: Print 2: Download 3: Cancel")
whoops = input()
if "1" in whoops:
	print(bar.text)
elif "2" in whoops:
	open("apidata" + str(time.time())  + '.txt', 'wb').write(bar.content)
else:
    pass
print()
print("done!")
print()
