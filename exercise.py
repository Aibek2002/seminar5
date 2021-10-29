  GNU nano 4.8                      exercise1.py                                

try:
        fhand = open('mailbox.txt')
except:
        print('File cannot be opened')
        exit()

lines=fhand.readlines()

for line in lines:
        if line.startswith('Received: from'):
                tokens=line.split()
                print(tokens[4:5])


fhand.close()
