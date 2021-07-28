input = input()
input = input.split()

A = int(input[0])
B = int(input[1])
C = int(input[2])

maiorAB = (A + B + abs(A - B))/2
maiorC = (maiorAB + C + abs(maiorAB - C))/2

maiorAB = (A + (B + C + abs(B - C))/2 + abs(A - (B + C + abs(B - C))/2))/2

print(str(int(maiorC)) + " eh o maior")
print(str(maiorAB) + " eh o maior")