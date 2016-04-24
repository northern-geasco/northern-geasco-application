#!/bin/bash

echo "Specify destination path for Snake Antivirus: "
read path
destination=pwd
if [[ -d $path ]]; then
    nowpath=`pwd`
    cd $path
    mkdir "SnakeAntivirus"
    cd $nowpath
    cp -av "../lib/" "$path/SnakeAntivirus/lib"
    cp -av "../data/" "$path/SnakeAntivirus/data"
    echo "virsig.cfg_path=$destination/data/virsig.cfg\nlog_path=$destination/data/event.log\nvirsig_database_strings=http://www.nlnetlabs.nl/downloads/antivirus/antivirus/virussignatures.strings" >> $destination/data/config.cfg
    cp -av "../antivirus.py" "$path/SnakeAntivirus/"
    cp -av "run.sh" "$path/SnakeAntivirus/"
    echo "Snake Antivirus was installed"
else
    echo "$path is not valid"
    echo "Snake Antivirus was not installed"
    exit 1
fi
