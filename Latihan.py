print("---Mengakses list---")
a = [31,33,35,37,39]
print(a[2]) 
print(a[1:4]) 
print(a[-1]) 

print("---Mengubah elemen list---")
a[3] = 40
print(a)
a[3:] = [42,45]
print(a)

print ("---Menambah elemen list---")
b = a[0:2]
print (b)
b.append('python')
print(b)
b.extend([50,55,60])
print(b)
b.extend(a)
print(b)