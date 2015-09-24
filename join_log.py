#! /usr/bin/env python
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

dict1 = {}
dict2 = {}
dir="./"

f = open(dir+'/'+file1,'r')
for line in f:
   time,thread,searcher,latency=line.split(" ")
   key = time + "." + thread
   dict1[key]=int(latency)
f.close()

f = open(dir+'/'+file2,'r')
for line in f:
   time,thread,searcher,latency=line.split(" ")
   key = time + "." + thread
   dict2[key]=int(latency)
f.close()

for k, v in dict1.iteritems():
	v2 = 0
	if(dict2.has_key(k)):
          v2  = dict2[k]
        else:
	  second,ms,thread = k.split(".")
	  for i in range(-26,0):
            _ms = int(ms) + (i+1)
            _ms = '%0*d' % (3, _ms)
	    k1 = second + "." + str(_ms) + "." + thread
	    if(dict2.has_key(k1)):
              v2 = dict2[k1]
	      break
	if (v2 > 0):
	  diff = v - v2
	  print k,v,v2,diff
