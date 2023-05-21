def natural_number(string):
    return string.isdigit()

variables = {}

def get_result(command):
    parts = command.split()

    if parts[0] == "quit":
        return "quit"
    elif parts[0] == "input":
        var = parts[1]
        val = input("Enter a value for {}: ".format(var))
        variables[var] = val  #
    elif parts[0] == "print":
        var = parts[1]
        if var in variables:
            return variables[var]
        else:
            return "Variable '{}' is undefined.".format(var)
    elif parts[1] == "gets":
        var = parts[0]
        val = parts[2]
        if val in variables:
            variables[var] = variables[val] 
        else:
            return "Variable '{}' is undefined.".format(val)
    elif parts[1] == "adds":
        var = parts[0]
        val = parts[2]
        if natural_number(val):
            val = int(val)
        elif val in variables:
            val = int(variables[val])
        else:
            return "Variable '{}' is undefined.".format(val)
        variables[var] = str(int(variables.get(var, 0)) + val) 
    else:
        return "Syntax error: Invalid command."

script_name = input("Script name: ")

with open(script_name, "r") as script_file:
    for line in script_file:
        line = line.strip()
        if line == "quit":
            break
        else:
            result = get_result(line)
            if result == "quit":
                break
            elif result is not None:
                print(result)

print("Goodbye")
