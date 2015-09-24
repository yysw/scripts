#!/usr/bin/python -tt

import xml.etree.ElementTree as ET
import codecs
import sys
import re

def main():
    filename = sys.argv[1]
    tree = ET.parse(filename)
    root = tree.getroot()
    datatypes = {}

    for d in root.iter('DATATYPE'):
        datatypes[d.get('ID')] = d.get('TypeName')

    for r in root.iter('REGION'):
        print r.get('ID'), r.get('RegionName') 

    outfile = re.sub(r'\.\w+','',filename) + ".txt"
    f = codecs.open(outfile, 'w','utf-8')
    for t in root.iter('TABLE'):
        f.write('Tablename:' +  t.get('Tablename') + '\n')
        for col in t.iter("COLUMN"):
            if (col.get('PrimaryKey') == '1'):
                line = '%15s%10s%40s%30s\n' % (col.get('ColName'), datatypes[col.get('idDatatype')], col.get('Comments'), 'PrimaryKey')
            else:
                line = '%15s%10s%40s\n' % (col.get('ColName'), datatypes[col.get('idDatatype')], col.get('Comments'))
            f.write(line)
        f.write('\n')
    f.close()

if __name__ == '__main__':
    main()
