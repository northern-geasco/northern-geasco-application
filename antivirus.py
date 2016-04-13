#!/usr/bin/python
import lib
import sys

while True:
	select = raw_input("Antivirus 1.0 Snake\n[a] Start Scan\n[x] Exit\nSelection: ")
	
	if select == "a":
		filename = ""
		while filename == "":
			filename = raw_input( "File/Directory to Scan: " )
		lib.scan(filename)
		continue
	elif select == "x":
		sys.exit(0)
	else:
		print "Incorrect selection"
		continue
