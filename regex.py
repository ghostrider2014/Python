import re

fh = open("regex_sum_855220.txt")
total = 0
for line in fh:
    line = line.rstrip()
    temp = re.findall('[0-9]+',line)
    if len(temp) > 0:
        for w in temp:
            total += int(w)
print(total)
