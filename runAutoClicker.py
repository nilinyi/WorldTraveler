import os
import urllib2
import json
import time

# def checkConnected():
# 	try:
# 		response = urllib2.urlopen("http://192.168.131.45/", timeout = 1)
# 		return json.load(response)
# 	except urllib2.URLError as e:
# 		print e.reason

def clickAction():
	os.system("./autoClicker -x 242 -y 670")
	os.system("./autoClicker -x 242 -y 720")
	time.sleep(1)
	print "clicking!!"

def start():
	while True:
		# if checkConnected() != None:
			clickAction()

start()