f = open('./04_input.txt', 'r')

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
        passport[key] = value

print(valid_cnt)
