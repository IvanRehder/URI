p1 = input()
p1 = p1.split()
p2 = input()
p2 = p2.split()

x_p1 = float(p1[0])
y_p1 = float(p1[1])
x_p2 = float(p2[0])
y_p2 = float(p2[1])

print("{:.4f}".format(((x_p2 - x_p1)**2 + (y_p2 - y_p1)**2)**0.5))