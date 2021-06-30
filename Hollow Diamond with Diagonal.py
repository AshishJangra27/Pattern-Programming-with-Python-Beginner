# Author: Ashish Jangra from Teenage Coder

num = 4

lvl = num - 2

print(" " * (num-1) + "*")

for i in range(lvl):
    print(" " * (lvl-i) + "*" + " "*(2*i +1) + "*")
    
print("* " * (num))

for i in range(lvl-1,-1,-1):
    print(" " * (lvl-i) + "*" + " "*(2*i +1) + "*")
    
print(" " * (num-1) + "*")