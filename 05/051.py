f = open('./05_input.txt', 'r')

lines = f.read().splitlines()

res = 0
seatID = 0

for line in lines:
  row = int(line[0:7].replace('F','0').replace('B','1'),2)
  column = int(line[7:10].replace('R','1').replace('L','0'),2)
  seatID = row * 8 + column
  if seatID > res:
    res = seatID

print(res)