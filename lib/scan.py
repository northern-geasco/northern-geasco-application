#!/usr/bin/python
import re
import os

def scan(filename, virsigdes):
	if os.path.isdir(filename) == True:
		safedir = 0
		os.chdir(filename)
		for fileline in os.listdir(os.getcwd()):
			if os.path.isdir(fileline) == True:
				print '\033[94m' + "[Can't Open Directorys]" + '\033[0m' + " %s" % fileline
			elif os.path.exists(fileline) == True: 
				filecontent = open(fileline)
				for line in open(virsigdes):
					virname, virsigs = line.split('=')
					if filecontent == re.match('\Q\E\s*', virsigs):
						print '\033[91m' + "[Infected by %s]" % virname + '\033[0m' + " %s" % fileline
					elif filecontent != re.match('\Q\E\s*', virsigs):
						safedir += 1
						if safedir == 1781:
							print '\033[92m' + "[Clean]" + '\033[0m' + " %s" % fileline 
	elif os.path.exists(filename) == True:
		safefile = 0
		for fileline in open(filename):
			for line in open("data/virsig.cfg", "r"):
				virname, virsigs = line.split('=')
				if fileline == re.match('\Q\E\s*', virsigs):
					print '\033[91m' + "[Infected by %s]" + '\033[0m' + " %s" % (virname, filename)
				elif fileline != re.match('\Q\E\s*', virsigs):
					safefile += 1
					if safefile == 1781:
						print '\033[92m' + "[Clean]" + '\033[0m' + " %s" % filename
	else:
		print '\033[94m' + "[Can't Open]" + '\033[0m' + " %s" % filename
