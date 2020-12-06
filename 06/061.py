f = open('./06_input.txt', 'r')

lines = f.read().splitlines()

group = ''
sum = 0

for line in lines:
  if len(line) == 0:
    sum += len(set(group))
    group = ''
  else:
    group = group + line

print(sum)
