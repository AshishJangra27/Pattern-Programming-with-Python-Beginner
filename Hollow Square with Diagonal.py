# Author: Ashish Jangra from Teenage Coder

num = 8
lvl = num - 2

print("* "*num)

for i in range(lvl):
    
    print("*" + " "*((2*i)+1) + "*" + " "*((2*(lvl - i - 1))+1) + "*")

print("* "*num)