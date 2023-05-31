import os

command = input()

while command != 'End':
    command = command.split('-')

    if command[0] == 'Create':
        file = open(command[1], 'w')
        file.close()
    elif command[0] == 'Add':
        with open(command[1], 'a') as f:
            f.write(command[2] + '\n')
    elif command[0] == 'Replace':
        with open(command[1], 'r') as f:
            if os.path.exists(command[1]):
                for line in open(command[1], 'r').readlines():
                    line = line.replace(command[2], command[3])
                    f.write(line)
            else:
                print("An error occurred")
    # elif command[0] == 'Delete':
    #     try:
    #         os.remove(command[1])
    #     except FileNotFoundError:
    #         print("An error occurred")

    command = input()


# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2
# nd
# Delete-random.txt
# Delete-file.txt
# End