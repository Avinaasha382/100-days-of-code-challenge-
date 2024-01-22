#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

with open("./Input/Names/invited_names.txt",mode = "r") as File:
    names = File.readlines()

with open("./Input/Letters/starting_letter.txt",mode = "r") as File:
    contents = File.read()

for i in range(len(names)):
    name = names[i].strip("\n")
    names[i] = name
print(names)
    

for i in range(len(names)):
    with open("./Output/ReadyToSend/"+names[i]+".txt",mode = "w") as File:
        x = contents.replace("[name]",names[i])
        File.write(x)

        
    


    
