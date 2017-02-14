# -*- coding: utf-8 -*-
import re
import os


#make new variable that list files in dir
what_in_dir = os.listdir('data')

# delete all urls from files
for files in what_in_dir:
    clean_list = []
    with open('data/' + files, 'r', encoding="utf-8") as f_input:
        for l in f_input:
            if not l.startswith('http'):
                clean_list.append(l)
    
    with open('data/' + files, 'w', encoding="utf-8") as f_out:
        f_out.write(''.join(clean_list))


#for files in dir open it and split on new doc
#we should find pattern that we want recognize and split our data
#my case is 2 new string simbols
  
for files in what_in_dir:
    print(files + '\n')
    raw_file = open('data/' + files, mode='r', encoding='utf-8')
    readed_file = raw_file.read()
    articles = re.split(r'\n\s*\n', readed_file)
  
   
   
try:
    #split our data to new file
    for i in range(len(readed_file)):
        article = articles[i]
        file_name = "output/{}{}.txt".format(article[:50], str(i))
        file = open(file_name, mode='w', encoding='utf-8')
        file.write(article)
        file.close() 
        
except(IndexError):
    
    print("End of list\n")
          
print("Numbers of files: ",len(os.listdir('output')))
#     
# #chek what we have in dir, if dir not empty delete all files from dir
# if not what_in_dir:
#     print('dir is empty')    
# else:
#     os.remove(input_path)
#     print('Your files has been deleted')