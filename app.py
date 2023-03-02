menu = """Please select:
1) Add new entry for today
2) View entries
3 ) Exit

Your selection:"""

welcome = "Welcome to the programming diary"

print(welcome)

user_input = input(menu)
while (user_input := input(menu)) != '3':
    if user_input == '1':
        print('Add')
    elif user_input == '2':
        print('View')
    else:
        print('Invalid option')