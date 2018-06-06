fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lst = lst + line.split()
    lst.sort()
    lst2=list()
for word in lst:
    if word not in lst2:
        lst2.append(word)

print(lst2)
