#!/usr/bin/python

# Simple script to carve session payload (contents) and save to dump
# file. Script written for the Forensics #WAP Challenge 14 ....
# Challenge: http://pentesteracademylab.appspot.com/lab/webapp/forensics/2
#
# Usage: 
#	(1) Extract the TCP Stream using Wireshark or TCPFlow
#	(2) python carver_wap14.py stream
#	(3) use Linux 'cat' command to concatenate all dumps together
# 
# Written by: 	Ali Al-Shemery
# Site:			http://www.binary-zone.com/
#
#
# If you want to play, then choose PentesterAcademy.com ;)
# Thanks to Vivek for his great work
#

import sys

f = open(sys.argv[1],"rb")
s = str(f.read())
f.close()

findme = "octet-stream"

indx = s.find(findme)
if (s[indx+12] + s[indx+13]) == end:
	print "endline found"
	newIndx = indx + len(findme) + 4

endIndx = s.find("\r\n", newIndx)

mylist = list(s)
x = str("".join(mylist[newIndx:endIndx]))

fName = raw_input("Please enter a file name for your dump: ")
f2 = open(fName, "wb")
f2.write(x)
f2.close()
print "END"
