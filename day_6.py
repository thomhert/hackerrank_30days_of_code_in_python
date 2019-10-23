# Enter your code here. Read input from STDIN. Print output to STDOUT
def printEven(s):
    output = ""
    for i in range(len(s)):
        if i % 2 == 0:
            output += s[i]
    return output

def printOdd(s):
    output = ""
    for i in range(len(s)):
        if i % 2 != 0:
            output += s[i]
    return output

t = int(input())

for i in range(0, t):
    s = input()
    print(printEven(s) + " " + printOdd(s))
