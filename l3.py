arr =[]
r=int(input("к:"))
for i in range(r):
    arr.append(int(input(":")))
print(arr)
s=sum(arr)
print("c.:"+ str(s))
a=int(s)/r
print("с.а.:"+ str(a))
min=arr[0]
for i in arr:
    if i<a:
        print("min:"+ str(min))

