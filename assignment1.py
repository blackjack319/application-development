name = input("What is your name? ")
length = len(name)
o = 0
for n in range(0, length):
    if o == 0:
        print(name)
    else:
        print(name[:o])
    o -= 1
