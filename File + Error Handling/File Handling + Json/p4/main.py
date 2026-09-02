'''
Problem 4: Contact Book 📇
You have a file called contacts.txt with these lines:

text
Alice,123-456-7890
Bob,987-654-3210
Charlie,555-123-4567
Your task:

Ask the user (using input()) to enter a name.

Search for that name in the file.

If found, print "Phone: [number]".

If NOT found, ask the user to enter a phone number for that new contact, and append the new contact to the file (so it's saved for next time).

Example run:

text
Enter name: Bob
Phone: 987-654-3210

Enter name: David
David not found. Enter phone: 444-555-6666
Contact added!
'''


while True:
    user = input("Enter a name: ")
    found = False
    if user == 'q':
        break
    with open('contacts.txt','r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            info = line.split(',')
            if info[0].lower() == user.lower():
                print(f'Phone: {info[1]}')
                found = True
        if not found:   
            new_info = input(f'{user.lower()} not found. Enter phone: ')
            with open('contacts.txt','a') as f:
                f.write(f'\n{user.lower()},{new_info}')
                
        
        
