import operator
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
ops = {
    1: ("+", operator.add),
    2: ("-", operator.sub),
    3: ("*", operator.mul),
    4: ("/", operator.truediv),
    5: ("%", operator.mod)
}
menu = "\n".join([f"{k}.{v[0]}" for k, v in ops.items()])
choice = int(input(f"{menu}\nEnter your choice: "))
if choice in ops:
    result = ops[choice][1](a, b)
    print(f"{a} {ops[choice][0]} {b} = {result}")
else:
    print("Invalid input")