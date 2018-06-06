fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
list=list()
for line in fh:
    line.rstrip()
    if line.startswith("From: "):
        list=line.split()
        print(list[1])
        
        count=count+1


print("There were", count, "lines in the file with From as the first word")
