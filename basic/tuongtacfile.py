
filename = "commands.txt"
key = ''
""" #biến dành cho cách 1
commands = dict()
component = {}
component2 ={}"""
result = {}
with open(filename, "r") as fh:
    """# cách 1:
    for line in fh:
        command = line.strip().split('\n')
        if '[' in command[0] and ']' in command[0]:
            convertline = command[0].split('[')
            convertlineagain = convertline[1].split(']')
        if '=' in command[0]:
            command2, des = command[0].strip().split('=')
            s = des.strip().split('|')
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
#cách 2 - tối ưu nhất:
    for line in fh:
        command = line.strip().split('\n')
        if '[' in command[0] and ']' in command[0]:
            convertline = command[0].split('[')
            convertlineagain = convertline[1].split(']')
            key = convertlineagain[0]
            result[convertlineagain[0]]=dict()
        if '=' in command[0] and '|' in command[0]:
            command2, des = command[0].strip().split('=')
            s = des.strip().split('|')
            obj = {command2:s[0]}
            result[key].update(obj)
print(result)
"""#cách 3:
input_file = open("config.txt",'r')
content = [i[:-1] for i in input_file.readlines()]
result = dict()
for idx, e in enumerate(content):

    if "[" in e:
        content[idx] = content[idx].replace('[', '')
        content[idx] = content[idx].replace(']', '')
        key = idx
        result[content[idx]] = dict()
    elif "=" in e:
        content[idx] = e[:e.index('|')]
        e = e[:e.index('|')]
        obj = {e[:e.index('=')].strip():  e[e.index('=') + 1:].strip()}
        if key < idx:
            result[content[key]].update(obj)

print(result)"""

