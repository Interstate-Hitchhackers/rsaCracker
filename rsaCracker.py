import math
import sys

numberList = input("Message to Decrypt: ").split(" ")
d = int(input("D Value (https://www.wolframalpha.com/widgets/view.jsp?id=d5bb63088eb2fb2e762f1c260d2b886d): "))
n = int(input("N Value (Given): "))
stringVal = []

for x in numberList:
    val = (int(x)**d) % n

    stringVal.append(chr(val))

print("".join(stringVal))