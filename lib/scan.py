#!/usr/bin/python

def scan():
	safe = 0

	filename = ""
	while filename == "":
		filename = raw_input( "File/Directory to Scan: " )

	for line in open( "data/virsig.cfg", "r" ):
		virname, virsig = line.split('=')

		for fileline in open(filename):
			if fileline == virsig:
				print '\033[91m' + "[Infected by %s]" + '\033[0m' + " %s" % (virname, filename)
			else:
				safe += 1
				if safe == 1781:
					print '\033[92m' + "[Clean]" + '\033[0m' + " %s" % filename
