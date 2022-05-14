#monte carlo methods
import math
from random import randint, random
from time import time
prob=0
c_yes=0
c_no=0
num=10000000
for i in range(num):
    x=0
    y=0
    flag=0
    for j in range(10):
        if (x>(-50) and x<50) and (y>200 and y<300):
            flag=1
            break
        else:
            if (x<-1000 or x>1000) or (y<-1000 or y>1000):
                flag=2
            angle = randint(0,360)
            x+=250* math.cos(angle)
            y+=250* math.sin(angle)
            flag=0

    if flag==1:
        c_yes+=1
    else:
        c_no+=1

prob=c_yes/num
print(prob) 

