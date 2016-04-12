#!/usr/bin/python
import lib
import sys

while True:
	menu = "Antivirus 1.0 Snake\n[a] Start Scan\n[x] Exit\nSelection: "
	select = raw_input(menu)

	if select == "a":
		filename = ""
		while filename == "":
			filename = raw_input( "File/Directory to Scan: " )
		lib.scan(filename, "/Users/odonckers/Documents/Hacking/Python/Snake-Software/data/virsig.cfg")
		continue
	elif select == "x":
		sys.exit(0)
	else:
		print "Incorrect selection"
		continue
