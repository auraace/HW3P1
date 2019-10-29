name = input()
sum = 0
for c in name.upper():
    print(c + ": " + str(ord(c)))
    sum += ord(c)
print("output: " + str((sum ^ 4660)^22136))