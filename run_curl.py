#! /usr/bin/env python
import sys
import time
import os

file=sys.argv[1]
f = open(file,'r')
for line in f:
    params=line.split()
    paramNum=len(params)
    url=params[0]
    ip=params[1]
    if(paramNum == 3):
        cookie=params[2]
        cmd='curl -i "'+url+'" -H "X-Forwarded-For: '+ip+'"'+' -H "Cookie: '+cookie+'"'
    else:
        cmd='curl -i "'+url+'" -H "X-Forwarded-For: '+ip+'"'
    print 'command:',cmd
    output = os.popen(cmd).read()
    print output

    time.sleep(0.1)
f.close()
