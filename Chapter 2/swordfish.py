#continue statement tutorial
while answer != 'N':
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is your password?')
    password=input()
    if password == 'swordfish':
        break

print('Access granted!')