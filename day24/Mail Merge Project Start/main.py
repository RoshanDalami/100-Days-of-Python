#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("./Input/Names/invited_names.txt","r") as names:
    name_list = names.readlines()

with open("./Input/Letters/starting_letter.txt",'r') as letter:
    letter_list = letter.read()
    for name in name_list:
        modified_name = name.strip()
        ready_letter = letter_list.replace("[name]",modified_name)
        print(ready_letter)
        with open(f"./Output/ReadyToSend/letter_for_{modified_name}.txt",mode="w") as completed_letter:
            completed_letter.write(ready_letter)

