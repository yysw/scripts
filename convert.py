#!/usr/bin/python -tt
import re
import codecs
import sys

def gbk2unicode(match):
  if match:
    str = match.group(1)
#    print str
    strs = str.replace('\\',' ').split()
    i = 0
    words = []
    while (i < len(strs)):
      word = chr(int(strs[i]))  + chr(int(strs[i+1]))
      words.append(word.decode('gbk'))
      i += 2
    word = ''.join(words)
#    print word
    return word
  
def main():
    if len(sys.argv) != 2:
        print "usage: convert.py filename"
        sys.exit(1)

    filename = sys.argv[1]
    f = open(filename,'rU')
    text = f.read()
    converted = re.sub(r'((\\\d\d\d){2,})', gbk2unicode, text)
    f.close()

    print converted
    out = codecs.open(filename+".converted",'w', 'utf-8')
    out.write(converted);
    out.close()

if __name__ == '__main__':
  main()
