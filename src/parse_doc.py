# -*- coding: utf-8 -*-
import re
import os

#set path to your data
input_path = 'data/za7.txt'         # here your should paste your path

#set output path to your data
output_path = 'output/za7spl.txt'   # here your should paste your output path

#make new variable that list files in dir
what_in_dir = os.listdir('data')

#for files in dir open it and split on new doc
#we should find pattern that we want recognize and split our data
#my case is 2 new string simbols
for i in what_in_dir:
    print(i)
    raw_file = open('data/' + i, mode='r')
    articles = re.split(r'\n\s*\n', raw_file.read(), flags=re.M)



#split our data to new file
for i in range(len(articles)):
    article = articles[i]
    file_name = "output/{}{}.txt".format(article[:20], str(i))
    file = open(file_name, mode='w', encoding='utf-8')
    file.write(article)
    file.close() 

print(what_in_dir)

#chek what we have in dir, if dir not empty delete all files from dir
if not what_in_dir:
    print('dir is empty')    
else:
    os.remove(input_path)
    print('Your files has been deleted')