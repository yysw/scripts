#! /usr/bin/env python
import sys


index = -1
index1 = -1
find = False
file = sys.argv[1]
num = 0
line_num = 0
with open(file,'r') as f:
    for line in f:
        line_num+=1
        index = line.find('"match_type">CA_')
        index1 = line.find('publish_time')
        if (index > 0):
            num = line_num
            find = True
            #print line
        if (find and index1 > 0 and ((line_num - num) == 5)):
            start = line.find('">')
            print line[(start+2):(start+12)]
            find = False
f.close()
