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

    words  = sys.argv[1]
    print words
    words = words.decode('utf8').encode('gbk')
    i = 0
    gbkstr = []
    while (i < len(words)):
        gbkstr.append('\%s' % (ord(words[i])))
        i += 1
    print ''.join(gbkstr)
    

if __name__ == '__main__':
  main()
