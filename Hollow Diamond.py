# Author: Ashish Jangra from Teenage Coder

num = 10

lvl = num - 1

print(" "*num + "*")

for i in range(lvl):
    print(" " * (lvl - i) + '*' + (" " * ((2*i)+1)) + "*")
    
for i in range(lvl, -1, -1):
    print(" " * (lvl - i) + '*' + (" " * ((2*i)+1)) + "*")
    
print(" "*num + "*")