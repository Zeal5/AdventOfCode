"""https://adventofcode.com/2022/day/3"""


import string
#fuirst half
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
letters =   dict(enumerate((lowercase + uppercase),1))

common_letters = ''
total = 0
def clean(first_half,second_half):
    global common_letters 
    for letter in first_half:
        if letter in second_half:
            common_letters += letter
            return

with open('zzzinp.text','r') as file:
    compartment = file.readlines()
    for line in compartment:
        half = len(line)// 2
        clean(line[:half],line[half:])

# 
def get_key(val,my_dict):
    for key, value in my_dict.items():
        if val == value:
            return int(key)
    return 0
print(common_letters)
for common in common_letters:
    total += get_key(common,letters)
print(total) 

#send half
letters = {v: k for k, v in enumerate(string.ascii_letters, 1)}

common_letters = []
total = 0


def clean(first_half):
    global common_letters
    a, b, c = first_half[0], first_half[1], first_half[2]
    common_letters.append(str(set(a).intersection(b).intersection(c)))


with open('zzzinp.text', 'r') as file:
    lines = file.read().splitlines()
    for i in range(0, len(lines), 3):
        lines_3 = [l for l in lines][i:3*(i+1)]
        clean(lines_3)


total = 0
for i in common_letters:
    total += letters[i.strip("'{}")]
print(total)