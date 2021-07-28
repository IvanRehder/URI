s_name = input()
s_salary = float(input())
s_sold = float(input())

total_salary = s_salary + s_sold*0.15

print("TOTAL = R$ " + "{:.2f}".format(total_salary))