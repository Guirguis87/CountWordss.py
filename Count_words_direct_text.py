from collections import *
user_text = input (r" Please Enter your text : ")
#1st step , count letters , "," " " and so on...... 
user_count_letters = len(user_text)
# insert delimiter for each " "
user_words= user_text.split (" ")
# Exceptins to be considered and not counting
exceptions_counting = ["?" , "," , "." , "!", "/" , "_", "@"]


for i in user_words : 
    if i in exceptions_counting:
        user_words.remove(i)
        continue
print(len(user_words))
