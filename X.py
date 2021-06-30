# Author: Ashish Jangra from Teenage Coder

num = 2
lvl = num - 1

for i in range(lvl):
    print(" "*(i) + "*" + " "*(2*(lvl-i) + 1) + "*")
    
print(" "*(num) + "*")

for i in range(lvl-1,-1,-1):
    print(" "*(i) + "*" + " "*(2*(lvl-i) + 1) + "*")