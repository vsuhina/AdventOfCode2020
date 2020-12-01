f = open('./input.txt', 'r')

lines = f.read().splitlines()
num = list(map(lambda x: int(x), lines))
cnt = len(num)
indexes = range(cnt)

for i in indexes:
  x = num[i]
  for j in indexes[i::]:
    y = num[j]
    for z in num[j::]:
      if (x+y+z == 2020):
        print(x*y*z)
        quit()
