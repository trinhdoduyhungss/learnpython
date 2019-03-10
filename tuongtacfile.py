
filename = "commands.txt"
d = ''
commands = {}
component = {}
key = ''
with open(filename, "r") as fh:
    for line in fh:
        command = line.strip().split('\n')
        if '[' in line  and ']' in line:
            convertline = line.split('[')
            convertlineagain = convertline[1].split(']')
            key = convertlineagain[0]
        if '=' in line:
            command2,des = line.strip().split('=')
            component[command2] = des
            commands[key] = component


print(commands)