f = open('./03_input.txt', 'r')

lines = f.read().splitlines()

xs = [1,3,5,7,1]
ys = [1,1,1,1,2]

total = 1

for i in range(len(xs)):
  x = xs[i]
  y = ys[i]

  current_x = 0
  current_y = 0
  cnt = 0

  for j in range(int(len(lines) / y)):
    line = lines[current_y]
    length = len(line)
    if line[current_x % length] == '#':
      cnt += 1
    current_x += x
    current_y += y

  total *= cnt

print(total)
