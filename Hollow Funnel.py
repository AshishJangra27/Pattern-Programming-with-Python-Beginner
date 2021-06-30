# Author: Ashish Jangra from Teenage Coder

num = 7
lvl = num - 2

print("* "*num)

for i in range(lvl):
    print(" "*(i+1) + "*" + " "*(2*(lvl-i)-1) + "*" )
    
print(" "*(num-1) + "*")     

for i in range(lvl-1,-1,-1):
    print(" "*(i+1) + "*" + " "*(2*(lvl-i)-1) + "*" )
    
print("* "*num)