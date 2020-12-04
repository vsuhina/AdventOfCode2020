f = open('./01_input.txt', 'r')

lines = f.read().splitlines()
num = list(map(lambda x: int(x), lines))
cnt = len(num)

for i in range(cnt):
  x = num[i]
  for y in num[i::]:
    if (x+y == 2020):
      print(x*y)
      quit()
