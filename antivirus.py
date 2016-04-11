#!/usr/bin/python

def detect():
	safe = 0

	filename = ""
	while filename == "":
		filename = raw_input( "File/Directory to Scan: " )

        for line in open( "virsig.cfg", "r" ):
		virname, virsig = line.split('=')

                for fileline in open(filename):
                        if fileline == virsig:
                                print "[Infected by %s] %s" % (virname, filename)
                        else:
				safe += 1
				if safe == 1781:
					print "[Clean] %s" % filename

menu = "Antivirus 1.0 Snake Engine\n[a] Start Scan\nSelection: "
select = raw_input(menu)
if select == "a":
        detect()
