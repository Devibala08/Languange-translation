import pandas as pd
import os, psutil
import timeit
setup_code = "from math import factorial"

with open(r'C:\Users\welcome\Desktop\t8.shakespeare.txt') as file:
    data = file.read()

words  = pd.read_excel(r'C:\Users\welcome\Desktop\translate.xlsx')  # excel file

orignal_text = data
n= 0
while n < len(words):
    txt1 = str(words['English'].iloc[n])
    translated_word = words['French'].iloc[n]
    orignal_text = orignal_text.replace(txt1, translated_word)
    #print(n)
    n = n + 1
#print(orignal_text)
file = open(r'C:\Users\welcome\Desktop\Translated_text4.xlsx','w')
file.write(orignal_text)
file.close()

print(f"Execution time is: {timeit.timeit(setup = setup_code, number = 10000000)}")
process = psutil.Process(os.getpid())
print(f"Used memory is bytes: {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2}")
