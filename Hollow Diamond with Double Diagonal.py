# Author: Ashish Jangra from Teenage Coder

num = 8
lvl = num - 2

print(" "*(num-1) + "*")

for i in range(lvl):
    print((lvl-i)*" " + "*" + " "*i + "*" + " "*i + "*")
    
print("* "*num)

for i in range(lvl-1, -1 , -1):
    print((lvl-i)*" " + "*" + " "*i + "*" + " "*i + "*")
    
print(" "*(num-1) + "*")