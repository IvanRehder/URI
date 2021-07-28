p1 = input()
p1 = p1.split()
p2 = input()
p2 = p2.split()

c_p = (int(p1[0]), int(p2[0]))
n_p = (int(p1[1]), int(p2[1]))
p_p = (float(p1[2]), float(p2[2]))

total = 0
for i in range(2):
    total = n_p[i] * p_p[i] + total

print("VALOR A PAGAR: R$ " + "{:.2f}".format(total))