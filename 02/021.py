f = open('./02_input.txt', 'r')
import re

lines = f.read().splitlines()

regex = r'([\d]+)-([\d]+) ([\w]): ([\w]+)'

correct = 0

for line in lines:
  m = re.search(regex, line)
  fr = int(m.group(1))
  to = int(m.group(2))
  ch = m.group(3)
  password = m.group(4)

  cnt = list(password).count(ch)
  if cnt >= fr and cnt <= to:
    correct += 1

print(correct)