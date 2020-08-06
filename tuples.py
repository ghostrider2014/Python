fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
time = []
counts = dict()
#selecting hour from line starting with From and creating dictionary
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    hr = words[5].split(':')
    counts[hr[0]] = counts.get(hr[0],0)+1
#adding tuples to list
for k,v in counts.items():
    time.append((k,v))
time.sort()
#printing tuples
for k,v in time:
    print(k,v)
