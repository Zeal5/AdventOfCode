"""https://adventofcode.com/2022/day/7"""

curr_dir = ['/']
stuff = {}
y = []
with open("taken_flight.txt") as read:
    for i in read.readlines()[1:]:
        if i.startswith('$'):
            if y:
                stuff[tuple(curr_dir)] = y
                y = []
            i = i[2:].strip()
            if i.startswith('cd'):
                x = i[3:]
                if x == '..':
                    curr_dir.pop()
                else:
                    curr_dir.append(x)
            else:
                y = []
        else:
            a, b = i.split()
            y.append(tuple(i.split()))
if y:
    stuff[tuple(curr_dir)] = y

def size(start):
    tot = 0
    for i in stuff[start]:
        if i[0] == 'dir':
            tot += size(start + (i[1],))
        else:
            tot += int(i[0])
    return tot


qwer = 70000000

o = 0
free = qwer - size(('/',))
req = 30000000 - free
asdf = float('inf')
for i in stuff:
    print(i, size(i))
    if size(i) >= req:
        print(i, size(i))
        asdf = min(asdf, size(i))
print(asdf)