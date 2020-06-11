
# Question 2
ilist = []

# Get input from user
print("Input string:")
name = input()

# Add input to list and print
for i in name:
    ilist.append(i)

print(*ilist, sep="")

# Delete two characters
del ilist[2]
del ilist[3]

# Reverse and print new list
ilist.reverse()
print(*ilist, sep="")

