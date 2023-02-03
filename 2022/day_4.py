"""https://adventofcode.com/2022/day/4"""

counter = 0
def check(fa:int,sa:int):
    global counter
    a = set(range(int(fa[0]),int(fa[1])+1))
    b = set(range(int(sa[0]),int(sa[1])+1))
    if b.issubset(a) == True:
        counter += 1
        return
    elif a.issubset(b) == True:
        counter += 1
        return


with open("zzzinp.text",'r') as file:
    file = file.readlines()
    for i in file:
        aa = i.strip().split(',')
        ab = [k.split('-') for k in aa]
        check(ab[0],ab[1])

print(counter)