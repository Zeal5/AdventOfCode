"""https://adventofcode.com/2022/day/6"""


data = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""

check = data[:14]

def check_repeat(string: str):
    for i in  string:
        count = 0
        for j in range(14):
            if i == string[j]:
                count += 1
                if count>1:
                    return False
    print(len(check))
    return True



looping = True
for i in range(14,len(data)):
    check += data[i]
    for j in check[-14]:
        if check_repeat(check[-14:]) == True:
            looping = False
    if looping == False:
        break

    

