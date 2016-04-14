#!/usr/bin/python
import lib
import sys

configlocal = "/Users/odonckers/Dropbox/Github/Snake-Antivirus/data/config.cfg"

while True:
	select = raw_input("Antivirus 1.0 Snake\n[a] Start Scan\n[b] See Scan Log\n[x] Exit\nSelection: ")
	
	if select == "a":
		filename = ""
		while filename == "":
			filename = raw_input( "File/Directory to Scan: " )
		lib.scan(filename, configlocal)
		
		lib.ended('write', configlocal)
		
		continue
	elif select == "b":
		lib.ended('get', configlocal)
		
		continue
	elif select == "x":
		sys.exit(0)
	else:
		print "Incorrect selection"
		
		continue
