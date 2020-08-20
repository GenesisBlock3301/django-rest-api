arr = [1,7,2,4]
a = []
b = []
d = []
for i in range(len(arr)):
    c = i
    for j in range(c+1,len(arr)):
        a.append((arr[i],arr[j]))
        c+=1
print(a)
for i in a:
    if sum(i)%3 !=0 :
        b.append(i[0])
        d.append(i[1])
print(b,d)

