'''filename = 'test.txt'
file_writer = open(filename, 'w')
file_writer.write('Hello new little file.\n')
file_writer.close()


filename = 'test.txt'
file_writer = open(filename, 'a')
file_writer.write('Hello again new little file.')
file_writer.close()
'''

filename = 'test.txt'
writer = open(filename, 'w')
writer.write('Hello new little file.\n')
writer.write('How are you today?\n')
writer.write('Who the hell this?')
name = input('Enter your name: ')
writer.write('\n\tYours truely,')
writer.write('\n\t'+ name)
writer.close()

reader = open(filename , 'r')
for line in reader:
    print('Line:\t' + line.rstrip())
reader.close()