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
						infectedsel = raw_input("What would you like to do with the infected file?\n[a] Remove file\n[b] Quarantine file\n[c] Nothing\nSelection: ")
						if infectedsel == "a":
							os.remove(fileline)
							print "File successfully removed!"
						elif infectedsel == "b":
							for qfile in open(fileline, 'w+'):
								qfile.write("#/%s\n" % qfile)
							print "File successfully quarantined!"
						elif infectedsel == "c":
							print "Moving on."
					elif filecontent != re.match('\Q\E\s*', virsigs):
						safedir += 1
						if safedir == 1781:
							print '\033[92m' + "[Clean]" + '\033[0m' + " %s" % fileline 
							safedir = 0
	elif os.path.isdir(filename) == False:
		safefile = 0
		for fileline in open(filename):
			for line in open(virsigdes[1], "r"):
				virname, virsigs = line.split('=')
				if fileline == re.match('\Q\E\s*', virsigs):
					print '\033[91m' + "[Infected by %s]" + '\033[0m' + " %s" % (virname, filename)
					infectedsel = raw_input("What would you like to do with the infected file?\n[a] Remove file\n[b] Quarantine file\n[c] Nothing\nSelection: ")
					if infectedsel == "a":
						os.remove(fileline)
						print "File successfully removed!"
					elif infectedsel == "b":
						for qfile in open(fileline, 'w+'):
							qfile.write("#/%s\n" % qfile)
						print "File successfully quarantined!"
					elif infectedsel == "c":
						print "Moving on."
				elif fileline != re.match('\Q\E\s*', virsigs):
					safefile += 1
					if safefile == 1781:
						print '\033[92m' + "[Clean]" + '\033[0m' + " %s" % filename
	else:
		print '\033[94m' + "[Can't Open]" + '\033[0m' + " %s" % filename
