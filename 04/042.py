f = open('./04_input.txt', 'r')
import re

lines = f.read().splitlines()

req_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
req_keys_cnt = len(req_keys)

passport = {}
valid_cnt = 0

for line in lines:
  if len(line) == 0:
    p_keys = passport.keys()
    p_keys_cnt = len(p_keys)
    valid = (p_keys_cnt == req_keys_cnt) or (p_keys_cnt == req_keys_cnt - 1 and 'cid' not in p_keys)
    if valid:
      valid_cnt += 1
    passport = {}
  else:
    for kv in line.split(' '):
      ind = kv.find(':')
      key = kv[0:ind]
      value = kv[ind+1::]
      if key in req_keys:
        ok = False
        if (key == 'byr' and int(value) >= 1920 and int(value) <= 2002):
          ok = True
        elif (key == 'iyr' and int(value) >= 2010 and int(value) <= 2020):
          ok = True
        elif (key == 'eyr' and int(value) >= 2020 and int(value) <= 2030):
          ok = True
        elif key == 'hgt':
          if len(value) >=4:
            h = int(value[0:-2])
            unit = value[-2::]
            if unit == 'cm' and h >= 150 and h <= 193:
              ok = True
            elif unit == 'in' and h >= 59 and h <= 76:
              ok = True
        elif key == 'hcl' and bool(re.match(r'^#[0-9a-f]{6}$', value)):
          ok = True
        elif key == 'ecl' and value in ['amb','blu','brn','gry','grn','hzl','oth']:
          ok = True
        elif key == 'pid' and bool(re.match(r'^[0-9]{9}$', value)):
          ok = True
        elif key == 'cid':
          ok = True

        if ok:
          passport[key] = value

print(valid_cnt)
