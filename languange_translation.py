import pandas as pd

with open('t8.shakespeare.txt') as file:
    data = file.read()

words  = pd.read_excel('translate.xlsx')  # excel file

orignal_text = data
n= 0
while n < len(words):
    txt1 = str(words['English'].iloc[n])
    translated_word = words['French'].iloc[n]
    orignal_text = orignal_text.replace(txt1, translated_word)
    #print(n)
    n = n + 1
#print(orignal_text)
file = open('Translated_text3.txt', 'w')
file.write(orignal_text)
file.close()
