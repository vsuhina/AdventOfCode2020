f = open('./06_input.txt', 'r')

lines = f.read().splitlines()

group = set()
first = True
sum = 0

for line in lines:
  if len(line) == 0:
    sum += len(set(group))
    group = set()
    first = True
  else:
    if first:
      group = set(line)
      first = False
    else:
      new = set(line)
      group = set(filter(lambda x: x in new, group))

print(sum)
