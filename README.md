# HW3P1
EECS 349 HW 3 Part 1

Q1)The new executable is in the folder as CRACKME_Y.EXE

Q2)
1)The serial for Stephen is 18011

2)Yujie: 17866
Shifu: 17715
Yiming: 17793

3)To get the given serial for a name you convert the name to upper case.  Then you add up the ascii values of all of the letters.  Then you XOR the sum with 1234h (4660 in decimal).  Then take the result of that and XOR with 5678h (22136 in decimal).  The result of this will be the serial for the given name.  I made a python program that generates the serial for a given name it is in the repo as name.py.