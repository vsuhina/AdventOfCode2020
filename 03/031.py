f = open('./03_input.txt', 'r')

lines = f.read().splitlines()

x = 3
y = 1
current = 0
cnt = 0

for line in lines:
  length = len(line)
  if line[current % length] == '#':
    cnt += 1
  current += x

print(cnt)
