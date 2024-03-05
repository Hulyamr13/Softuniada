n = int(input())
length = n * 2 + 1
midsize = n - 3
print("{0}_/_{0}".format('.' * (n - 1)))
print("/{0}^,^{0}\\".format('.' * (n - 2)))
for i in range(midsize):
    print("|{0}|".format('.' * (length - 2)))
print("\\{0}\\_/{0}/".format('.' * (n - 2)))
