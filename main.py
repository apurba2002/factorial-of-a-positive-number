num = int (input("Enter a positive integer :"))
res = 1
if (  num > 0):
    n = 1
    for n in range(1,num+1):
        res = n * res
    print(res)
else:
    print("Please enter a positive integer .")