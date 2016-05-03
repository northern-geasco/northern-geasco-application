Snake-Antivirus
==============
A simple antivirus written in Python in which can scan files.

How to Install
--------------
1. Enter scripts/ directory
   - `cd scripts/`
2. run bash install.sh or ./install.sh
   - `bash install.sh`
3. Follow the directions of the install.sh program
4. Edit the antivirus.py file and change the `configlocal` variable to the destination of the config.cfg file starting from the root or / if you are on a Linux machine, and if you are on a DOS machine than you can do it from the root or \ of the system.
   - `vim antivirus.py` or `nano antivirus.py`
   - `configlocal = "<Location of SnakeAntivirus starting from the root or />"`
5. Run run.sh in the SnakeAntivirus directory.
   - `bash run.sh` or `./run.sh`

Future Ideas
------------
- [ ] Go into directory after directory and scan files inside of them (Please help, anybody!)
- [X] Delete infected files
- [X] Quarantine infected files (Removed this option, because there was no point in quarantining the file.)
- [ ] Scan memory usage for viruses that attack only when program is started
- [ ] Create a GUI interface for my software

Insperation
-----------
I have always wanted to make an antivirus, but at the time I was only fluint in Perl. After learning some Python, I found an antivirus called [Candy-Software]. I loved it, but, I felt as if I was stealing from the programmer who made it. So, I challenged myself to build my own antivirus from scratch but only Python.

Disclaimer
----------
This antivirus is still under development. The system is unstable still, so I am not responsible for any broken computers if this software does something to your computer. And, this software is not a stand alone antivurs, yet.

Version
-------
1.0.4

License
-------
[Owen Donckers]

[here]:https://github.com/odonckers/Snake-Antivirus/wiki
[Candy-Software]:https://github.com/iskernel/candy-antivirus
[Owen Donckers]:https://github.com/odonckers/Snake-Antivirus/blob/master/LICENSE.md
