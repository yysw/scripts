#! /usr/bin/env python
mb_latency_dic = {}
mb_url_dic = {}
up_latency_dic = {}
serving_latency_dic = {}
res_count_dic = {}
ad_count_dic = {}
dir='formated.data/'

total=0
miss=0
f = open(dir+'serving.latency','r')
for line in f:
   req,ccode,serving_latency=line.split()
   if (req.find("[null]")>-1):
       continue
   k,v=serving_latency.split("=")
   kc,vc=ccode.split("=")
   #if(vc=="mb_blending"):
   #if(vc=="mb_ucp"):
   serving_latency_dic[req+vc]=int(v)
f.close()

f = open(dir+'adCount','r')
for line in f:
   req,ccode,ad_count=line.split()
   if (req.find("[null]")>-1):
       continue
   k,v=ad_count.split("=")
   kc,vc=ccode.split("=")
   ad_count_dic[req+vc]=int(v)
f.close()

f = open(dir+'res.count','r')
for line in f:
   req,ccode,res_count=line.split()
   if (req.find("[null]")>-1):
       continue
   k,v=res_count.split("=")
   kc,vc=ccode.split("=")
   res_count_dic[req+vc]=int(v)
f.close()

f = open(dir+'mb.latency','r')
for line in f:
   req,ccode,mb_latency=line.split()
   if (req.find("[null]")>-1):
       continue
   k,v=mb_latency.split("=")
   kc,vc=ccode.split("=")
   mb_latency_dic[req+vc]=int(v)
f.close()

f = open(dir+'mb.url','r')
for line in f:
    headerIndex=line.find("mb.headers")
    linePart=line[0:headerIndex-1]
    mb_headers=line[(headerIndex):]
    req,ccode,mb_url=linePart.split()
    if (req.find("[null]")>-1):
       continue
    url=mb_url[(mb_url.find("=")+1):]
    kc,vc=ccode.split("=")
    #headers=mb_headers[(mb_headers.find("mb.headers")):]
    mb_url_dic[req+vc]=url+' '+ mb_headers

f.close()

f = open(dir+'up.latency','r')
for line in f:
   req,ccode,up_latency=line.split()
   if (req.find("[null]")>-1):
       continue
   k,v=up_latency.split("=")
   kc,vc=ccode.split("=")
   up_latency_dic[req+vc]=int(v)

f.close()

#print '(request id)  ','serving.latency  ','mb.latency  ','(serving.latency - mb.latency)','up.latency  ', '(bucket id) ','mb.url  '
#print '#########################k,serving,mb,diff,up,adCount,resCount,bk,url#########################'

for k, v in serving_latency_dic.iteritems():
        serving = serving_latency_dic[k]
        if(mb_latency_dic.has_key(k)):
          mb = mb_latency_dic[k]
        else:
          continue; 
        diff = serving - mb
        if(mb_url_dic.has_key(k)):
           url = mb_url_dic[k]
           i=url.find("bk=")
           if(i>-1):
               bk = url[(i+3):(i+6)]
           else:
               bk = '--'
        else:
          continue
        if(ad_count_dic.has_key(k)):
            adCount = ad_count_dic[k]
        else:
            adCount = '--'
        if (res_count_dic.has_key(k)):
            resCount = res_count_dic[k]
        else:
            resCount = '--'
        if (up_latency_dic.has_key(k)):
          up = up_latency_dic[k]
        else:
          up = '--'
        print k,serving,mb,diff,up,adCount,resCount,bk,mb_url_dic[k].strip()

#print "miss:",miss,"total:", total,"miss rate:",float(miss)/float(total)*100
