import re
variables = {}

variable_pattern = r"(int|string|float)\s+(\w+)\s*:\s*(.+?)!"
print_pattern = r"print\s+(.+?)!"
add_pattern = r"add\s+(\w+)\s*:\s*(.+?)!"
sub_pattern = r"sub\s+(\w+)\s*:\s*(.+?)!"
mul_pattern = r"mul\s+(\w+)\s*:\s*(.+?)!"  
div_pattern = r"div\s+(\w+)\s*:\s*(.+?)!"  
pow_pattern = r"pow\s+(\w+)\s*:\s*(.+?)!"  
loop_pattern = r"loop\s+(\w+)\s*:\s*(.+?)!"
loopa_pattern = r"loopa\s+(\w+)\s*:\s*(.+?)\s*:(.+?)!"
loops_pattern = r"loops\s+(\w+)\s*:\s*(.+?)\s*:(.+?)!"
loopm_pattern = r"loopm\s+(\w+)\s*:\s*(.+?)\s*:(.+?)!"
loopd_pattern = r"loopd\s+(\w+)\s*:\s*(.+?)\s*:(.+?)!"
loope_pattern = r"loope\s+(\w+)\s*:\s*(.+?)\s*:(.+?)!"
if_pattern = r"if\s+(\w+)\s+(<|>|=|!=)\s+(\w+)\s*:\s+(.+?)!"
ifn1_pattern = r"ifn1\s+(.+?)\s+(<|>|=|!=)\s+(\w+)\s*:\s+(.+?)!"
ifn2_pattern = r"ifn2\s+(\w)\s+(<|>|=|!=)\s+(.+?)\s*:\s+(.+?)!"
ifa_pattern = r"ifa\s+(\w+)\s+(<|>|=|!=)\s+(\w+)\s*:\s+(\w+)\s*:\s*(.+?)!"
ifs_pattern = r"ifs\s+(\w+)\s+(<|>|=|!=)\s+(\w+)\s*:\s+(\w+)\s*:\s*(.+?)!"
ifm_pattern = r"ifm\s+(\w+)\s+(<|>|=|!=)\s+(\w+)\s*:\s+(\w+)\s*:\s*(.+?)!"
ifd_pattern = r"ifd\s+(\w+)\s+(<|>|=|!=)\s+(\w+)\s*:\s+(\w+)\s*:\s*(.+?)!"
ife_pattern = r"ife\s+(\w+)\s+(<|>|=|!=)\s+(\w+)\s*:\s+(\w+)\s*:\s*(.+?)!"
loopp_pattern = r"loopp\s+(\w+)\s*:\s*(.+?)\s*:(.+?)!"
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
        elif match := re.match(pow_pattern, line):
            name, pow_value = match.groups()
            pow_value = pow_value.strip()

            if name in variables:
                try:
                    if isinstance(variables[name], int):
                        variables[name] = variables[name] ** int(pow_value)
                    elif isinstance(variables[name], float):
                        variables[name] = variables[name] ** float(pow_value)
        
                except ValueError:
                    print(f"Invalid value '{pow_value}' for exponentiation of variable '{name}'.")
            else:
                print(f"Cannot raise string variable '{name}' to a power.")
        elif match := re.match(loop_pattern,line):
            var,amount = match.groups()
            amount = amount.strip()
            if var in variables:
                amount = int(amount)
                for _ in range(amount):
                    print(variables[var])
            else:
                print("Variable Doesn't Exist")
        elif match := re.match(loopa_pattern,line):
            var,num,amount = match.groups()
            num = num.strip()
            amount = amount.strip()
            if var in variables:
                num = int(num)
                amount = int(amount)
                for _ in range(amount):
                    variables[var] += num
        elif match := re.match(loops_pattern,line):
            var,num,amount = match.groups()
            num = num.strip()
            amount = amount.strip()
            if var in variables:
                num = int(num)
                amount = int(amount)
                for _ in range(amount):
                    variables[var] -= num
        elif match := re.match(loopm_pattern,line):
            var,num,amount = match.groups()
            num = num.strip()
            amount = amount.strip()
            if var in variables:
                num = int(num)
                amount = int(amount)
                for _ in range(amount):
                    variables[var] *= num
        elif match := re.match(loopd_pattern, line):
            var, num, amount = match.groups()
            num = num.strip()
            amount = amount.strip()
            if var in variables:
                num = int(num)
                amount = int(amount)
            for _ in range(amount):
                variables[var] /= num
        elif match := re.match(loope_pattern, line):
            var, num, amount = match.groups()
            num = num.strip()
            amount = amount.strip()
            if var in variables:
                num = int(num)
                amount = int(amount)
            for _ in range(amount):
                variables[var] =  variables[var] ** num
        elif match := re.match(if_pattern, line):
            var1, condition, var2, result = match.groups()
            if var1 in variables and var2 in variables:
                if condition == '>':
                    if variables[var1] > variables[var2]:
                        print(result)
                elif condition == '<':
                    if variables[var1] < variables[var2]:
                        print(result)
                elif condition == '=':
                    if variables[var1] == variables[var2]:
                        print(result)
                elif condition == '!=':
                    if variables[var1] == variables[var2]:
                        print(result)
        elif match := re.match(ifn1_pattern, line):
            num1, condition, var2, result = match.groups()
            if var2 in variables:
                num1 = int(num1)
                if condition == '>':
                    if num1 > variables[var2]:
                        print(result)
                elif condition == '<':
                    if num1 < variables[var2]:
                        print(result)
                elif condition == '=':
                    if num1 == variables[var2]:
                        print(result)
                elif condition == '!=':
                    if num1 == variables[var2]:
                        print(result)       
        elif match := re.match(ifn2_pattern, line):
            var1, condition, num2, result = match.groups()
            if var1 in variables:
                num2 = int(num2)
                if condition == '>':
                    if variables[var1] > num2:
                        print(result)
                elif condition == '<':
                    if variables[var1] < num2:
                        print(result)
                elif condition == '=':
                    if variables[var1] == num2:
                        print(result)
                elif condition == '!=':
                    if variables[var1] == num2:
                        print(result)    
        elif match := re.match(ifa_pattern, line):
            var1, condition, var2, var3,num = match.groups()
            num = num.strip()
            num = int(num)
            if var1 in variables and var2 in variables:
                if condition == '>':
                    if variables[var1] > variables[var2]:
                        if var3 in variables:
                            variables[var3] += num
                elif condition == '<':
                    if variables[var1] < variables[var2]:
                        if var3 in variables:
                            variables[var3] += num
                elif condition == '=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] += num
                elif condition == '!=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] += num  
        elif match := re.match(ifs_pattern, line):
            var1, condition, var2, var3,num = match.groups()
            num = num.strip()
            num = int(num)
            if var1 in variables and var2 in variables:
                if condition == '>':
                    if variables[var1] > variables[var2]:
                        if var3 in variables:
                            variables[var3] -= num
                elif condition == '<':
                    if variables[var1] < variables[var2]:
                        if var3 in variables:
                            variables[var3] -= num
                elif condition == '=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] -= num
                elif condition == '!=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] -= num  
        elif match := re.match(ifm_pattern, line):
            var1, condition, var2, var3,num = match.groups()
            num = num.strip()
            num = int(num)
            if var1 in variables and var2 in variables:
                if condition == '>':
                    if variables[var1] > variables[var2]:
                        if var3 in variables:
                            variables[var3] *= num
                elif condition == '<':
                    if variables[var1] < variables[var2]:
                        if var3 in variables:
                            variables[var3] *= num
                elif condition == '=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] *= num
                elif condition == '!=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] -= num 
        elif match := re.match(ifd_pattern, line):
            var1, condition, var2, var3,num = match.groups()
            num = num.strip()
            num = int(num)
            if var1 in variables and var2 in variables:
                if condition == '>':
                    if variables[var1] > variables[var2]:
                        if var3 in variables:
                            variables[var3] /= num
                elif condition == '<':
                    if variables[var1] < variables[var2]:
                        if var3 in variables:
                            variables[var3] /= num
                elif condition == '=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] /= num
                elif condition == '!=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] -= num 
        elif match := re.match(ife_pattern, line):
            var1, condition, var2, var3,num = match.groups()
            num = num.strip()
            num = int(num)
            if var1 in variables and var2 in variables:
                if condition == '>':
                    if variables[var1] > variables[var2]:
                        if var3 in variables:
                            variables[var3] = variables[var3] ** num
                elif condition == '<':
                    if variables[var1] < variables[var2]:
                        if var3 in variables:
                            variables[var3] = variables[var3] ** num
                elif condition == '=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] = variables[var3] ** num
                elif condition == '!=':
                    if variables[var1] == variables[var2]:
                        if var3 in variables:
                            variables[var3] = variables[var3] ** num
        elif match:= re.match(loopp_pattern,line):
            var,message,amount = match.groups()
            amount = amount.strip()
            amount = int(amount)
            if var in variables:
                for _ in range(amount):
                    print(message)
        elif match := re.match(print_pattern, line):
            msg = match.group(1)

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