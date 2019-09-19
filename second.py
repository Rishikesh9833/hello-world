import pkg.mex
import requests

print(pkg.mex.square(10))


from pkg.mex import square
#1
from pkg import square
#2
from pkg import *
print(square(10))
#3
from pkg import cube
print (cube(10))

print(requests.__version__)

import csv
f = open("data/iris.csv","rt")#Read and Text
lines = f.readlines()
f.close()

#or
with open("data/iris.csv","rt") as f :
    rd = csv.reader(f)
    rows = list(rd)
    
#[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'], ['5.1', '3.5', '1.4', '0.2', 'Iris-setosa'], ['4.9', '3.0', '1.4', '0.2', 'Iris-setosa'], ['4.7', '3.2', '1.3', '0.2', 'Iris-setosa'], ['4.6', '3.1', '1.5', '0.2', 'Iris-setosa']]
    
headers = rows[0]
rows=rows[1:]
rowsd=[]
for sl,sw,pl,pw,n in rows :
    rowsd.append([float(sl),float(sw),float(pl),float(pw),n])

print(rowsd)

#unique data
un=set()
for sl,sw,pl,pw,n in rows :
    un.add(n)
#or
un = {r[-1] for r in rowsd}

#
ed={}
for n in un:
    el =[]
    for sl,sw,pl,pw,name in rowsd:
        if n == name:
            el.append(sl)
    ed[n]={'max':max(el),'sum':sum(el),'min':min(el)}
    
ed['Iris-setosa']['min']


ed={}
for n in un:
    edd={}
    for i,fe in enumerate(headers[:-1]):
        el =[]
        for r in rowsd:
            if r[-1] == n:
                el.append(r[i])
        edd[fe]={'max':max(el),'sum':sum(el),'min':min(el)}
    ed[n]=edd

from sqlite3 import connect
con = connect("iris.db")
cur = con.cursor() 
cur.execute("""
create table if not exists iris(sl double,sw double,pl double,pw double,name string)
""")   
for r in rowsd:
    con.execute("insert into iris values(?,?,?,?,?)",r)

con.commit()
r=cur.execute("select name,max(sl) from iris group by name")
results = list(r.fetchall())
print(results)    

#Reguler Exp
import re
s1 = "Hello World"
sp = e"\w+"
re.findall(sp,s1)#['Hello','World']
re.findall(r"Hello\s+\W+)",s1)# ['World']
d="2019-12-12"
sp=r"\d\d\d\d-\d\d-\d\d"
re.findall(sp,d)#['2019-12-12']
re.findall(r"\w\w","ABCD")#['AB','CD'] 
re.findall(r"(?=(\w\w))","ABCD")#['AB','BC','CD']

s2 = "A,B:C;D" 
sp.split(",")#['A','B:C;D']
re.split(r",|:|;",s2)#['A','B','C','D']
re.sub("World","Earth",s1)
s4 = "The world world is round round"
re.sub(r"(\w+)\s+\1",r"\1",s4)#The world is round   
 # System info in Python

import subprocess as S
commond ='systeminfo'
proc = S.Popen(commond,shell=True,stdout=S.PIPE,stderr=S.STDOUT,universal_newlines=True )
out,err = proc.communicate()
out[0:10]  

hots = re.findall(r"KB([\w-]+)",out)
    
#HTTP Automation
import requests as r
res = r.get("http://httpbin.org/get")
res.json()

# Parse Json
import json
with open("data/example.json","rt")as f:
    obj = json.load(f)
el=[]
for emp in obj:
    el.append(emp['empId'])
print(el)
    

el =[]
for emp in obj:
    if emp['details']['isAlive']==True:
        for ph in emp['details']['phoneNumbers']:
            if ph['type'] == 'office':
                el.append(ph['number'])
            

import xml.etree.ElementTree as ET
tr = ET.parse("data/example.xml")
r = tr.getroot()
r.tag       # data
r.attrib    #{}
r.text      #'\n
xp ="./country/rank"
nn = r.findall(xp)
rl =[]
for n in nn:
    rl.append(int(n.text))

rl
    
    
    
    
    
    
    
    












