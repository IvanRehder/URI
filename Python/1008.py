w_id = int(input())
w_hours = int(input())
w_pay_hour = float(input())

salary = w_hours * w_pay_hour

print("NUMBER = " + str(w_id))
print("SALARY = U$ " + "{:.2f}".format(salary))