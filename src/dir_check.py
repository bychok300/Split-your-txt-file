import os

what_in_dir = os.listdir('data')

for i in what_in_dir:
    print(i)
    raw_file = open('data/' + i, mode='r')
#   print(file.read())
    
    