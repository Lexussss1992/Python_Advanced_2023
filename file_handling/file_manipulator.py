import os

command = input()

while command != 'End':
    command = command.split('-')

    if command[0] == 'Create':
        open(command[1], 'a+')

    elif command[0] == 'Add':
        with open(command[1], 'a') as f:
            f.write(command[2] + '\n')

    elif command[0] == 'Replace':
        if os.path.exists(command[1]):
            with open(command[1], 'r+') as f:
                text = f.read()
                text = text.replace(command[2], command[3])
                f.seek(0)
                f.write(text)
        else:
            print("An error occurred")

    elif command[0] == 'Delete':
        try:
            os.remove(command[1])
        except FileNotFoundError:
            print("An error occurred")

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