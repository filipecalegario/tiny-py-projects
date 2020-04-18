words = open('input.txt').read().split('\n')
output = open('output.txt', mode = 'w')
print(len(words))
for i in range(len(words)):
    output.write(words[i] + ', ')
    if i % 10 == 9:
        output.write('\n')