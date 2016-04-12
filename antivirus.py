#!/usr/bin/python
import lib

menu = "Antivirus 1.0 Snake Engine\n[a] Start Scan\nSelection: "
select = raw_input(menu)
if select == "a":
        lib.scan()
