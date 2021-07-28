p1 = input()
p1 = p1.split()
p2 = input()
p2 = p2.split()

c_p1 = int(p1[0])
n_p1 = int(p1[1])
p_p1 = float(p1[2])

c_p2 = int(p2[0])
n_p2 = int(p2[1])
p_p2 = float(p2[2])

total = n_p1 * p_p1 + n_p2 * p_p2

print("VALOR A PAGAR: R$ " + "{:.2f}".format(total))