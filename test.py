#data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#pos = data.find('.')
#print(pos)
#print(data[pos:pos+3])

""" text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
dummy = text[pos:]
print(float(dummy)) """

"""
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    print(line.rstrip().upper())
"""

fname = input("Enter file name: ")
fh = open(fname)
count = 0
avg = 0.0
value = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1;
    str = line.rstrip()
    pos = str.find('0')
    text = str[pos:]
    value = value + float(text)
print(value/count)
