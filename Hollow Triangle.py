# Author: Ashish Jangra from Teenage Coder

num = 5

print(" "*(num-1)  + "*")

for i in range(num-2):
    print(" "*(num - i-3) + " *" + (" "*(2*i + 1) + "*"))

print(num * "* ")