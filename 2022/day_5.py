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


def part1(_quantity:int , _from:int , _to:int ) -> int:

    for _ in range(int(_quantity)):
        try:
            item =  stacks[int(_from) -1].pop()
        except IndexError:
            pass
        stacks[int(_to) - 1].append(item)


def part2(_quantity:int , _from:int , _to:int ) -> int:

    items = stacks[int(_from) - 1][-int(_quantity):]
    #to
    for i in items:
        stacks[int(_to)-1].append(i)
        stacks[int(_from) - 1].pop()

    

def handler():
    for row in arrangment:
        _quantity, _from, _to = row
        if int(_quantity) > 1:
            part2(_quantity, _from, _to)
        else:
            part1(_quantity, _from, _to)


    ans = ''
    for h in stacks:
        ans += h[-1]
    print(ans.upper())    
handler()