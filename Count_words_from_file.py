while True:
    user_text = input (r" Please Enter your file path : ")
    user_text_file = str(user_text)
    exceptions_counting = ["?" , "," , "." , "!", "/" , "_", "@"]

    # Creating dynamic input for user to put the required path in dynamic way 

    myfile = open(user_text_file , "r")
    myfile.seek(0)
    myfile.readlines()
    myfile.seek(0)

    # create myfile2 variable to can do splitting operation 

    myfile2=myfile.read()
    myfile.seek
    myfile3= myfile2.split(" ")
    myfile.seek(0)

    # for more details, creating that list to identify no of letters will not be counted !
    removed_letters = []

    # creating that loop to iterate all words in file , and remove exceptions mentioned 

    for i in myfile3 : 
        if i in exceptions_counting:
            removed_letters.append(i)
            myfile3.remove(i)
    print(len(myfile3))

    # creating Summary report 

    if len(myfile3) > 0 : 
        report = open(r"D:\Courses - Trainings\Programming\Projects\Count words in String\repot.txt","w+")
        finalevaluation= report.write(f"For the file in path {user_text_file} , no of words are {len(myfile3)} words ,Exluded letters are {removed_letters} No of Excluded letters {len (removed_letters)} ")
        report.close()
        print(f"For the file in path {user_text_file} , no of words are {len(myfile3)} words , No of Excluded letters {len (removed_letters)} ")


    user_decision = input ("Would you like to continue with another file:  (y/n)")

    if user_decision == "y" :
        continue
    else:
        break














# for i in myfile.readlines() : 
#     if i in exceptions_counting:
#         myfile2= open(r"D:\Courses - Trainings\Programming\Projects\Count words in String\test.txt",w+)
#         myfile.
        
#         continue
# print(len(myfile.readlines()))

# for i in user_words : 
#     if i in exceptions_counting:
#         user_words.remove(i)
#         continue
# print(len(user_words))




# newfile= file.read()
# newfile.replace(",","  ")
# newfile.replace("!","  ")
# print(newfile)
# newfile.split(" ")
# # print(newfile.split(" "))

# # from os import replace


# file = open(r"D:\Courses - Trainings\Programming\Projects\Count words in String\Words to be counted.txt", "w+")
# file.seek(0)
# # for i in file: 
# #     if i == (",") or ("!") or ("?"):
# #         newfile= open(r"D:\Courses - Trainings\Programming\Projects\Count words in String\Words to be counted2.txt", "w+")
# #         replace(i, " ")
# #         newfile.close()
# # print(newfile.readlines())


# newfile = open(r"D:\Courses - Trainings\Programming\Projects\Count words in String\Words to be counted2.txt","w+")
# for i in file : 
#     if i == "?" :







