for i in range (1,5):
    for j in range (1,5):
        print("*",end=" ")
    print()

for i in range(5):
    print(i*"*", end=" ")
    i=i+1
    print()


for i in range(5):
    print((4 - i) * " " + (i * 2 + 1) * "*", end=" ")
    print()
