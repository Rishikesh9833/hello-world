import sys

# a = sys.argv[1]
# b = sys.argv[2]
# c = int(a) + int(b)
# print("a=",a,"b=",b,"c=",c)

a = 1
print(type(a))
f = 1.2
b = True
s = "Hello"
rs=r"Hello"
s= 'Hello'
s="""Hello
world"""

rs="\n"
print(len(rs))
rs=r"\n"
print(len(rs))

print(s)
print(type(s))

if a>= 1:
    print(a)
elif a < 1:
    print(a)
else:
    print(a)
    
    
#####################################

s = "OK"
lst = [1,2,3]
set1 = {1,2,3}
d= {'ok':1,'nok':2}
#length
print(len(s),len(lst),len(set1),len(d))
#empty
es ="" # immutable
el=[] # mutable, duplicates allow, insertaion ordered
es = set()# mutable, Opposite of list
ed ={} #mutable
et=() #immutable 

# type
print(type(es),type(el),type(es),type(ed),type(et))

# membership chceking
"O" in s #Boolen
"O" not in s #Boolen
1 in lst #does 1 exist in list
1 in set1
"Ok" in d # doses key ok exist in d

#Comparision
s == "OK", s !="NOK"
lst ==[1,2]
(1,2)==(2,1)
{1,1,1,2,3}=={1,2,3}

#itertor
s="OK"
for e in s:
    print(e)#O K
    
for e in lst:
    print(e)

for e in set1:
    print(e)

for k in d:
    print(k,d[k])

#accessing
lst=[1,2,3,4]
s="HELLO"
lst[0], s[0]
lst[-1], s[-1]
lst[-4],s[-5]

#slicing
lst[0:4:1]# start:end:Step #[1,2,3,4]
lst[:],s[:] #([1,2,3,4],'HELLO')
lst[::-1],s[::-1]#reverse ([4,3,2,1],'OLLEH')
s[::2],lst[::2]

set1= {1,2,3}
set1[0]#Error

lst.append(20)
set1.add(20)


#dict
d ={'ok':1,'nok':2}
d['ok']
d['new']= 20
d['ok']=20
d.keys()
d.values()
print(d.items())

#map pattern
lst =[3,5,2,4]
el =[]
for e inlst:
    el.append(e*e)
print(el)#squaring each ele
#or
el=[e*e for e in lst]#future
#with filter

el=[]
for e in lst:
    if e%2 ==0:
        el.append(e*e)
print(el)

#or 
el =[e*e for e in lst e%2 ==0] 



#input = list, otuput = set
es=set()
for w in lst:
    es.add(e*e)
#or
es ={e*e for e in lst}

# input = list , output = dict

ed={}
for e in lst:
    ed[e] = e*e
#or
ed ={e:e*e for e in lst}


lst(enumerate(['a','b']))
#[(0,'a'),(1,'b')]
lst = list(zip([''a,'b]))
#

lst = list(zip(['a','b'],[10,20],['X','Y']))
print(lst)


input='ABCDEF1234567890'
el[]
for f,s in zip(input[::2],input[1::2])
    el.append(int(f+s,base=16))
sum(el)%255 

# OR
sum(int(f+s,base=16) for f,s in zip(input[::2],input[1::2]) )%255   
#Function
def add(x,y):
    return x+y
    
add(1,2)     #positional arug
add(y=2,x=3) # keywordbased arug passing
add(2,y=3)   #mix restriction:posiional comes first


def add2(x,y=20)
    return x+y

add2(2)     # 22
add2(2,y=30)# 32


#Assignment
a,b=1,2
a,b = b,a
a,*b,c =1,2,3,4
a,b,c #(1,[2,3],4)

def add3(*args):
    s=0
    for e in args:
        s+=e%2
    return s

add3()
add3(1,2,3,4)
lst[1,2,3,4]
add3(lst[0],lst[1],lst[2],lst[3])
#or
add3(*lst)


#scope (Local, Global, BuiltIn)

s = 'OK'
len = 23
a = 2+3
a = len(s)+3 #error as len veriable clash with len menthod

del len
a= len(s)+ 3 # 5 

import random
el =[]
for i in rang(10)
    el.append(random.randint(10,100))
print(el)

#Or

el =[random.randint(10,100) for i in rang(10)]

#sorting
s = sorted(el)#normal sorting

s=sorted(el, reverse=True)#reverse sorting

lws['a','D','XZ','aaa','c']
sorted(lws)#alphabetial ordered sorting

def p(a):
    return len(a)
 
sorted(lws,key=p) #length base sorting
sorted(lws,key= lambda e: len(e)) # lambda base sorting

d = {'india'=2,'usa'=1}
sorted(d)# alphabetial sorting

def p(k):
    return d[k]
    
sorted(d,key=p)#value base sorting
#or
sorted(d,key=lambda k:d[k])# lambda value base sorting


    























    
