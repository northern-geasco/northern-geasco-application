#!/usr/bin/python
import re
import os

def scan(filename, configlocal):
	config = open(configlocal, "r").read().split('\n')
	virsigdes = config[0].split('=')
	if os.path.isdir(filename) == True:
		safedir = 0
		os.chdir(filename)
		for fileline in os.listdir(os.getcwd()):
			if os.path.isdir(fileline) == True:
				print '\033[94m' + "[Can't Open Directorys]" + '\033[0m' + " %s" % fileline
			elif os.path.exists(fileline) == True: 
				filecontent = open(fileline)
				for line in open(virsigdes[1]):
					virname, virsigs = line.split('=')
					if filecontent == re.match('\Q\E\s*', virsigs):
						print '\033[91m' + "[Infected by %s]" % virname + '\033[0m' + " %s" % fileline
						ynremove = raw_input("Would you like to remove the file? (y/n) ")
						if ynremove == "y" or ynremove == "Y":
							os.remove(fileline)
						else:
							print "Moving On"
					elif filecontent != re.match('\Q\E\s*', virsigs):
						safedir += 1
						if safedir == 1781:
							print '\033[92m' + "[Clean]" + '\033[0m' + " %s" % fileline 
							safedir = 0
	elif os.path.exists(filename) == True:
		safefile = 0
		for fileline in open(filename):
			for line in open(virsigdes[1], "r"):
				virname, virsigs = line.split('=')
				if fileline == re.match('\Q\E\s*', virsigs):
					print '\033[91m' + "[Infected by %s]" + '\033[0m' + " %s" % (virname, filename)
					ynremove = raw_input("Would you like to remove the file? (y/n) ")
					if ynremove == "y" or ynremove == "Y":
						os.remove(fileline)
					else:
						print "Moving On"
				elif fileline != re.match('\Q\E\s*', virsigs):
					safefile += 1
					if safefile == 1781:
						print '\033[92m' + "[Clean]" + '\033[0m' + " %s" % filename
						safefile = 0
	else:
		print '\033[94m' + "[Can't Open]" + '\033[0m' + " %s" % filename
