# Question 1
# There were several changes between python 2 and 3 version
# One difference was the print command was changed to print() function.
# Ex: print 'hello world' would work in V2 but not in V3.
# Another is that by default the output produced by integer division is a float in version 3.
# Ex: 3/2 = 1 in V2 while 3/2 = 1.5 in V3.


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


# Question 3
# Get input sentence from user and put in list
print("Input sentence:")
sentence = input()
jlist = sentence.split()

print(*jlist, sep=" ")

# Search and replace "python" with "pythons"
for i in range(len(jlist)):
    if jlist[i] == "python":
        jlist[i] = "pythons"

print(*jlist, sep=" ")