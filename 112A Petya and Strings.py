inp1 = input().upper()
inp2 = input().upper()
n = 0
while 1 <= len(inp1) <= 100 and 1 <= len(inp2) <= 100:
  if str(inp1) == str(inp2):
    print('0')
    break
  elif str(inp1)[n] == str(inp2)[n]:
    n = n + 1
  elif str(inp1)[n] != str(inp2)[n]:
    if str(inp1)[n] < str(inp2)[n]:  
      print('-1')
      break
    elif str(inp1)[n] > str(inp2)[n]:
      print('1')
      break