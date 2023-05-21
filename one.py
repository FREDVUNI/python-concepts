def is_natural_number(string):
    return string.isdigit()

variables = {}

def get_result(prompt):
    parts = prompt.split()

    if len(parts) < 2:
        print("Syntax error.")
        return

    if parts[0] == "quit":
        print("Goodbye")
        quit()
    elif parts[0] == "input":
        var = parts[1]
        val = input("Enter a value for {}: ".format(var))
        variables[var] = val
    elif parts[0] == "print":
        var = parts[1]
        if var.isnumeric():
            print(var)
        elif var in variables:
            print("{} equals {}".format(var, variables[var]))
        else:
            print("{} is undefined.".format(var))
    elif parts[1] == "gets":
        if len(parts) != 3 or not parts[0].isalpha() or not parts[2].isalnum():
            print("Syntax error.")
            return
        var = parts[0]
        val = parts[2]
        if val.isnumeric():
            val = int(val)
        elif val in variables:
            val = variables[val]
        else:
            print("{} is undefined.".format(val))
            return
        variables[var] = str(val)
    elif parts[1] == "adds":
        if len(parts) != 3:
            print("Syntax error.")
            return
        var = parts[0]
        val = parts[2]
        if is_natural_number(val):
            val = int(val)
        elif val.isalpha() and val in variables:
            val = int(variables[val])
        else:
            print("{} is undefined.".format(val))
            return
        if var in variables:
            variables[var] = str(int(variables[var]) + val)
        else:
            variables[var] = str(val)
    else:
        print("Syntax error.")

print("Welcome to the Adder REPL.")

prompt = input("??? ")
while prompt != "quit":
    get_result(prompt)
    prompt = input("??? ")

print("Goodbye.")
