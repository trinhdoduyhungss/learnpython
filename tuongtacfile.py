
filename = "commands.txt"
d = ''
commands = {}
component = {}
component2 = {}
key = ''
with open(filename, "r") as fh:
    # cách 1:
    for line in fh:
        command = line.strip().split('\n')
        if '[' in command[0] and ']' in command[0]:
            convertline = command[0].split('[')
            convertlineagain = convertline[1].split(']')
        if '=' in command[0]:
            command2, des = command[0].strip().split('=')
            s = des.strip().split('|')
            #tối ưu hóa được các đặc component thì sẽ tối ưu hóa đc code
            component[command2] = s[0]
            commands[convertlineagain[0]] = component

        if command[0] == '':
            for line2 in fh:
                if '[' in line2 and ']' in line2:
                    convertline = line2.split('[')
                    convertlineagain = convertline[1].split(']')
                    key = convertlineagain[0]
                    print(key)
                if '=' in line2:
                    command2, des = line2.strip().split('=')
                    ss = des.strip().split('|')
                    component2[command2] = ss[0]
                    commands[convertlineagain[0]] = component2

            break
    """
    # cách 2 - chưa xong:
    for line in fh:
        command = line.strip().split('\n')
        command2 = line.strip().split('=')
        if '[' in line and ']' in line:
            convertline = line.split('[')
            convertlineagain = convertline[1].split(']')
            key = convertlineagain[0]
        if '=' in command[0] :
            if component2 == {}:
                s = command2[1].strip().split('|')
                component[command2[0]] = s[0]
                commands[key] = component
            elif component2 != {}:
               ss = command2[1].strip().split('|')
               print(ss)


        if command[0] == '':
            component2 = component
            #print(component2)
            #break
    """
print(commands)