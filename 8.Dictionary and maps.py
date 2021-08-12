#task

# Given n names and phone numbers, assemble a phone book that maps friends' 
# names to their respective phone numbers. You will then be given an unknown 
# number of names to query your phone book for. For each name queried, print 
# the associated entry from your phone book on a new line in the form name=phoneNumber;
#  if an entry for name is not found, print Not found instead.


# Input Format

# The first line contains an integer, n, denoting the number of entries in the phone book.
# Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line. The first value is a friend's name, and the second value is an 8-digit phone number.

# After the n lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.

# Note: Names consist of lowercase English alphabetic letters and are first names only.


# Sample Input

# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
# Sample Output

# sam=99912222
# Not found
# harry=12299933

# #print(dir(dict))
# n=3

# d={'name':'renu','hgt':43,'wgt':43}
# #print(type(d))
# D={}

# for i in range(n):
#     k=input() 
#     v=input() 
#     d={k:v}
#     D.update(d)
# #print(D)
# for i in range(n):
#     s=input()
#     if s in D:
#         print(s+'='+D[s],sep=' ')
#     else:
#         print('Not found')

x = int(input())

dictt = {}

for i in range(x):
    text = input().split()
    dictt[text[0]] = text[1]

while True:
    try:
        inpt = input()
        if inpt in dictt:
            print(inpt+"="+dictt[inpt])
        else:
            print("Not found")
    except EOFError:
        break