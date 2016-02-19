import re
file = open('regex_sum_237416.txt')

numbers = list()

for line in file:
    line = line.strip()
    numbers += re.findall('[0-9]+', line)

# print numbers
print sum([int(number) for number in numbers])
