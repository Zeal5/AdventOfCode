
new = calories_list.replace("\n\n",'break')
new_new = new.split('break')
def sum(num)-> int:
    sum = 0
    real_num = ''
    for i in num:
        if i != '\n':
            real_num += i
        if i == '\n':
            sum += int(real_num)
            real_num = ''
    sum += int(real_num)
    return sum

max_L = []
for i in new_new:
    max_L.append(sum(i))
max_L.sort()
summ = 0
for h in max_L[-3:]:
    summ += h
print(summ)