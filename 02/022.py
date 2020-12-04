f = open('./02_input.txt', 'r')
import re

lines = f.read().splitlines()

regex = r'([\d]+)-([\d]+) ([\w]): ([\w]+)'

correct = 0

for line in lines:
  m = re.search(regex, line)
  first = int(m.group(1))
  second = int(m.group(2))
  ch = m.group(3)
  password = m.group(4)

  if (password[first -1 ] == ch) ^ (password[second - 1] == ch):
    correct += 1

print(correct)