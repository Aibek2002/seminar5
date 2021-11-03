try:
        fhand = open('mailbox.txt')
except:
        print('File cannot be opened')
        exit()

lines=fhand.readlines()
bibon=open('output.txt', 'w')
for line in lines:
        ind=line.find('[')
        en_ind=line.find(']')
        if line.startswith('Received: from') and 'unix' not in line[ind:en_ind]:
                word=line[ind+1:en_ind]
                print(word)
                bibon.write(word)
                bibon.write('\n')

fhand.close()

