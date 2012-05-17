#!/usr/bin/python

# Author: Jeff Cai
#
# This script is for tranverting svr4 package names to ips packages name
# in one spec file.
# Input: 
#        1. spec file xxx.spec
#        2. mapping file
# Output:
#        1. new spec file xxx.spec.new
#

import sys
import re
import string
import os

if len(sys.argv) < 2:
   print "Usage: transform.py [spec-file-name]"
   sys.exit(0)

# Read mapping file

dict = {}
try:
  rf = open("svr4-ips-namemapping")
except:
  print "Error: Can not open name mapping file svr4-ips-namemapping"
  sys.exit(0)

print "Reading the mapping file svr4-ips-namemapping..."

for line in rf:
   entries = re.split("[\t ]+", line)
   svr4name = string.strip(entries[0])
   ipsname = string.strip(entries[1])
   dict[svr4name] = ipsname
rf.close()

specfile = sys.argv[1]

pat1="Requires:"
pat2="BuildRequires:"
prog1 = re.compile(pat1, re.I)
prog2 = re.compile(pat2, re.I)

try:
    rf = open(specfile)
except:
    print "Error: can not open the file " + specfile
    sys.exit(0)

try:
    wf = open(specfile + ".new", "w")
except:
    print "Error: can not open the file " + specfile + ".new for writing"
    sys.exit(0)

lnCnt = 0
nlnCnt = 0

for line in rf:
    if prog1.match(line) or prog2.match(line):
         entries = re.split(":", line)
         svr4_name=string.strip(entries[1])
         if svr4_name in dict:
            wf.write("%s:       %s\n" % (entries[0], dict[svr4_name]))
            print "transverting %s to %s" % (svr4_name, dict[svr4_name])
            lnCnt = lnCnt + 1
         else:
            print "not found mapping for %s" % svr4_name
            nlnCnt = nlnCnt + 1
            wf.write(line)
    else:
        wf.write(line)

rf.close()
wf.close()

print
print "Finished"
print "Transverted %d lines" % lnCnt
print "%d lines mapping not found" % nlnCnt
