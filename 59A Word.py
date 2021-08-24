s = input()
n = 0
upper = 0
lower = 0
while len(s) >= 0 and len(s) <= 100 and n <= len(s):
  for i in s:
    if str(s)[n].isupper():
      upper = upper + 1
      n = n + 1
    elif str(s)[n].islower():
      lower = lower + 1
      n = n + 1
  if lower >= upper:
    print(s.lower())
    break
  elif upper > lower:
    print(s.upper())
    break