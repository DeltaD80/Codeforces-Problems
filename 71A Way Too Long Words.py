while True:
    n = int(input())
    if n in range(1,101):
        break
word_list = []
for i in range(n):
    while True:
        word = input()
        if len(word) in range(1,101):
            break
    word_list.append(word.lower())
 
for x in word_list:
    if len(x) > 10:
        print(x[0] + str(len(x[1:-1])) + x[-1])
    else:
        print(x)