import requests 
import sys 

l = open("usr/share/wordlist/rockyou.txt").read() 
directories = l.splitlines()

for dir in directories:
    c = f"http://{sys.argv[1]}/{dir}.html" 
    #takes user input [ip]
    r = requests.get(c)
    if r.status_code==404: 
        pass
    else:
        print("Valid directory:" ,c)
