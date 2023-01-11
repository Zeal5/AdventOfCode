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

