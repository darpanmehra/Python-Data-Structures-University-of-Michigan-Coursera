# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
pos=0
value=0
average=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find(" ")
    value=line[pos:].rstrip()
    value=float(value)
    count=count+1
    average=value+average
print('Average spam confidence:'," ", average/count)
