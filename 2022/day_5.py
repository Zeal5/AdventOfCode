import re

stacks = [
    ['p','f','m','q','w','g','r','t'],
    ['h','f','r'],
    ['p','z','r','v','g','h','s','d'],
    ['q','h','p','b','f','w','g'],
    ['p','s','m','j','h'],
    ['m','z','t','h','s','r','p','l'],
    ['p','t','h','n','m','l'],
    ['f','d','q','r'],
    ['d','s','c','n','l','p','h']
            ]


syntax = re.compile(r'\d+')

with open("2022\day_5input.txt" , "r") as file:
    f = file.readlines()
    arrangment = map(lambda x: syntax.findall(x), f)


for row in arrangment:
  
    for i in range(int(row[0])):
        try:
            item =  stacks[int(row[1]) -1].pop()
        except IndexError:
            pass
        stacks[int(row[2]) - 1].append(item)


ans = ''
for h in stacks:
    ans += h[-1]
print(ans.upper())