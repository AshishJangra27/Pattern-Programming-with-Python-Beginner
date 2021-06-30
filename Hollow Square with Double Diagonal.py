# Author: Ashish Jangra from Teenage Coder

num = 3
lvl = num - 2

print("* "*(num+2))

for i in range(lvl):
    print("* " + " "*(i) + "*" + " "*(2*(lvl-i)+1) + "*" + " "*i + " *")

print("*" + " "*num + "*" + " "*num + "*")

for i in range(lvl-1,-1,-1):
    print("* " + " "*(i) + "*" + " "*(2*(lvl-i)+1) + "*" + " "*i + " *")
    
print("* "*(num+2))