#! /usr/bin/env python
import sys
import os


file = sys.argv[1]
dir = sys.argv[2] + "/"

if not os.path.exists(dir):
    os.makedirs(dir)

fp = open(dir+"P","w")
ff = open(dir+"F","w")
fut = open(dir+"Ut","w")
fui = open(dir+"Ui","w")
fud = open(dir+"Ud","w")
fmt = open(dir+"Mt","w")
fma = open(dir+"Ma","w")
fmo = open(dir+"Mo","w")
fmv = open(dir+"Mv","w")
fms = open(dir+"Ms","w")
fmp = open(dir+"Mp","w")

def getValue(line, char):
    value = ''
    length = len(char)
    index = line.find(char + ':')
    if (index >= 0):
        part = line[index:]
        ispace = part.find(',')
        if(ispace >= 0):
            value = part[(length+1):ispace] + '\n'
        else:
            value = part[(length+1):] + '\n'
    return value
    
with open(file,'r') as f:
    for line in f:
        P = getValue(line,'P')
        fp.write(P)

        F = getValue(line,'F')
        ff.write(F)

        ut = getValue(line,'Ut')
        fut.write(ut)

        ui = getValue(line,'Ui')
        fui.write(ui)

        ud = getValue(line,'Ud')
        fud.write(ud)

        mt = getValue(line,'Mt')
        fmt.write(mt)

        ma = getValue(line,'Ma')
        fma.write(ma)

        mo = getValue(line,'Mo')
        fmo.write(mo)

        mv = getValue(line,'Mv')
        fmv.write(mv)

        ms = getValue(line,'Ms')
        fms.write(ms)

        mp = getValue(line,'Mp')
        fmp.write(mp)
fp.close()
ff.close()
fut.close()
fui.close()
fud.close()
fmt.close()
fma.close()
fmo.close()
fmv.close()
fms.close()
fmp.close()

