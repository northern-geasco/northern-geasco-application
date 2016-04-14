#!/bin/bash

if [ ! -f "antivirus.py" ]; then
	cd ../
	if [ ! -f "antivirus.py" ]; then
		echo "Unable to locate antivirus.py"
	fi
fi

default_dir=`pwd`

python antivirus.py
