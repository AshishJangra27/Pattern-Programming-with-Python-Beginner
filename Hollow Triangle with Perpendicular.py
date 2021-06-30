# Author: Ashish Jangra from Teenage Coder

num = 12

print(num * " " + "*")

for i in range(num-2):
    print((" "*(num-i-1)) + ("*") + (" "*i) + "*" + (" "*i) + "*")
    
print("* " * (num+1))