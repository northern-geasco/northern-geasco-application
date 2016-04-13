Snake-Antivirus
==============
A simple antivirus written in Python in which can scan files. (Antivirus still under development.)

Install
-------
- vim (or another type of file editor) data/config.cfg
  - Edit the virsig\_path variable to the destination of the file starting from the / of the system.
- vim (or another type of file editor) antivirus.py
  - change the destination for the config.cfg file on the 12th line.
- And finally enjoy!

Future Ideas
------------
- [ ] Go into directory after directory and scan files inside of them
- [ ] Quarantine infected files
- [ ] Scan memory usage for viruses that attack only when program is started
- [ ] Create a GUI interface for my software

Insperation
-----------
I have always wanted to make an antivirus, but at the time I was only fluint in Perl. After learning some Python, I found an antivirus called [Candy-Software]. I loved it, but, I felt as if I was stealing from the programmer who made it. So, I challenged myself to build my own antivirus from scratch but only Python.

Version
-------
1.0

License
-------
[Owen Donckers]

[Candy-Software]:https://github.com/iskernel/candy-antivirus
[Owen Donckers]:https://github.com/odonckers/Snake-Antivirus/blob/master/LICENSE.md
