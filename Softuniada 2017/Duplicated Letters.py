word = input()
operations = 0
while True:
    change = False
    i = 1
    while i < len(word):
        if word[i] == word[i - 1]:
            change = True
            operations += 1
            word = word[:i - 1] + word[i + 1:]
            i -= 1
        i += 1
    if not change:
        break

if len(word) == 0:
    print("Empty String")
else:
    print(word)

print("{0} operations".format(operations))
