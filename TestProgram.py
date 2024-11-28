import re

variables = {}

variable_pattern = r"(int|string|float)\s+(\w+)\s*:\s*(.+?)!"
print_pattern = r"print\s+(.+?)!"
add_pattern = r"add\s+(\w+)\s*:\s*(.+?)!"
sub_pattern = r"sub\s+(\w+)\s*:\s*(.+?)!"
mul_pattern = r"mul\s+(\w+)\s*:\s*(.+?)!"  
div_pattern = r"div\s+(\w+)\s*:\s*(.+?)!"  

with open("TestT.txt", "r") as file:
    for line in file:
        line = line.strip()  

        if line.startswith('#') or line.startswith('//'):
            continue
        
        if match := re.match(variable_pattern, line):
            data_type, name, value = match.groups()
            value = value.strip()
            if data_type == "int":
                try:
                    variables[name] = int(value)
                except ValueError:
                    variables[name] = value  
            elif data_type == "float":
                try:
                    variables[name] = float(value)
                except ValueError:
                    variables[name] = value 
            elif data_type == "string":
                variables[name] = value

        elif match := re.match(add_pattern, line):
            name, add_value = match.groups()
            add_value = add_value.strip()

            if name in variables:
                try:
                    if isinstance(variables[name], int):
                        variables[name] += int(add_value)
                    elif isinstance(variables[name], float):
                        variables[name] += float(add_value)
                    else:
                        print(f"Cannot add to string variable '{name}'.")
                except ValueError:
                    print(f"Invalid value '{add_value}' for addition to variable '{name}'.")
            else:
                print(f"Variable '{name}' is not defined.")

        elif match := re.match(sub_pattern, line):
            name, sub_value = match.groups()
            sub_value = sub_value.strip()

            if name in variables:
                try:
                    if isinstance(variables[name], int):
                        variables[name] -= int(sub_value)
                    elif isinstance(variables[name], float):
                        variables[name] -= float(sub_value)
                    else:
                        print(f"Cannot subtract from string variable '{name}'.")
                except ValueError:
                    print(f"Invalid value '{sub_value}' for subtraction from variable '{name}'.")
            else:
                print(f"Variable '{name}' is not defined.")

        elif match := re.match(mul_pattern, line):
            name, mul_value = match.groups()
            mul_value = mul_value.strip()

            if name in variables:
                try:
                    if isinstance(variables[name], int):
                        variables[name] *= int(mul_value)
                    elif isinstance(variables[name], float):
                        variables[name] *= float(mul_value)
                    else:
                        print(f"Cannot multiply string variable '{name}'.")
                except ValueError:
                    print(f"Invalid value '{mul_value}' for multiplication of variable '{name}'.")
            else:
                print(f"Variable '{name}' is not defined.")

        elif match := re.match(div_pattern, line):
            name, div_value = match.groups()
            div_value = div_value.strip()

            if name in variables:
                try:
                    if isinstance(variables[name], int):
                        variables[name] //= int(div_value)
                    elif isinstance(variables[name], float):
                        variables[name] /= float(div_value)
                    else:
                        print(f"Cannot divide string variable '{name}'.")
                except ValueError:
                    print(f"Invalid value '{div_value}' for division of variable '{name}'.")
            else:
                print(f"Variable '{name}' is not defined.")

        elif match := re.match(print_pattern, line):
            msg = match.group(1).strip()

            while '/' in msg:
                start_index = msg.find('/')
                end_index = msg.find(' ', start_index) if msg.find(' ', start_index) != -1 else len(msg)
                variable_name = msg[start_index + 1:end_index].strip()
                if variable_name in variables:
                    msg = msg[:start_index] + str(variables[variable_name]) + msg[end_index:] 
                else:
                    msg = msg[:start_index] + f"[undefined: {variable_name}]" + msg[end_index:]
            
            print(msg)

        else:
            print(f"Unrecognized command: {line}")