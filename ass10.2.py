name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):
        time = line.split()[5].split(":")
        counts [time[0]] = counts.get(time[0], 0) + 1


list = list()

for key, value in counts.items():
    list.append( (key,value) )
list.sort()

for hour, counts in list:
    print (hour, counts)
