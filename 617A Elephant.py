x = int(input())
steps = 0
if 1 <= x and x <= 1000000:
  steps = steps + x // 5
  if x % 5 > 0:
    steps = steps + 1
print(steps)