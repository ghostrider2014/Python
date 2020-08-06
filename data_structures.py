""" fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))
"""

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    count = count + 1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")
