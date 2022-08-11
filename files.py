import os
import os.path
f = open("1.txt").read()
d = os.listdir("1")
for i in d:
    g = open(i).read()
    for j in g:
       if ord(j)>=127:
           print(i)
           break




