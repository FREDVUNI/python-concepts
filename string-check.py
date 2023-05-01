def check_string(input_str):
    happyTrue = True
    happyFalse = False
    for i in range(len(input_str)):
        if input_str[i] == 'g':
            if i > 0 and input_str[i-1] == 'g':
                continue
            elif i < len(input_str)-1 and input_str[i+1] == 'g':
                continue
            else:
                return "Happy?:" + happyFalse
    return "Happy?:" + happyTrue
    
input_str = input("string: ")
print(check_string(input_str))

# problem
# We’ll say that a lowercase ’g’ in a string is ”happy” if there is another ’g’ immediately to its left or right. Write a function to print True if all the g’s in the given string are happy, otherwise, print False. in python using input
