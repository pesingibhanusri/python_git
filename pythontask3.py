n=4
for i in range(1,n+1):
    for j in range(1,i+1 ):
        print(j,end=" ")
    print()    

n = 5
for i in range(1, n + 1):
    start_value = i % 2 
    for j in range(i):
        print((start_value + j) % 2, end=" ")  
    print()





rows = 4
for i in range(rows):
    print(" " * i, end="")
    print("* " * rows)
