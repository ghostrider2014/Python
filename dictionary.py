fname = input("Enter file name: ")
fh = open(fname)
email = []
counts = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    email.append(words[1])
for word in email:
    counts[word] = counts.get(word,0)+1
bigword = None
bigcount = None
for word,count in counts.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)
