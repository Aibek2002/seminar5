try:
        fhand = open('mailbox.txt')
except:
        print('File cannot be opened')
        exit()

lines=fhand.readlines()
bibon=open('output.txt', 'w')
for line in lines:
        if line.startswith('Received: from'):
                ind=line.find('[')
                en_ind=line.find(']')
                word=line[ind+1:en_ind]
                print(word)
                bibon.write(word)
                bibon.write('\n')
fhand.close()


