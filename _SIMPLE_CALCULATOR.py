import math

print(" CALCULATOR ")


def calculator_op():

    # OPERATION SELECTOR
    op_selector = input("Choose the operation [+ - * / s(qrt)]: ")

    # SQUARE ROOT CONDITION
    if op_selector == "s":
        # sqrt_number = int(input("Choose the number for square root operation: "))
        print(math.sqrt(int(input("Insert a number for square root: "))))

    # OPERATION CONDITIONS
    if op_selector in ["+", "-", "*", "/"]:

        # INPUT NUMBERS
        in_num_01 = int(input("Choose the first number [int]: "))
        in_num_02 = int(input("Choose the second number [int]: "))

        if op_selector == "+":
            print(in_num_01 + in_num_02)

        if op_selector == "-":
            print(in_num_01 - in_num_02)

        if op_selector == "*":
            print(in_num_01 * in_num_02)

        if op_selector == "/":
            print(in_num_01 / in_num_02)

    # OPERATION NOT FOUND
    if op_selector not in ["+", "-", "*", "/", "s"]:
        print("No such operation!")

    # RESTART LOOP?
    restart = input("Do you want to execute another operation [y/n]: ")

    def restart_op():

        if restart == "y":
            calculator_op()
        else:
            print("Goodbye!")
            exit()

    restart_op()


calculator_op()
