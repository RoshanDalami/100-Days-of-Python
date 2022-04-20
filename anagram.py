str1 = input("Enter the first word : ")
str2 = input("Enter the second word : ")

str1_list = list(str1)
str2_list = list(str2)
check = []
if len(str1_list)!= len(str2_list):
    print("Length of two String are not same so not an anagram")
else:
    for i in range(len(str1_list)):
        for j in range(len(str2_list)):
            if(str1_list[i] == str2_list[j]):
                check.append(str1_list[i])

    if(len(str1_list) == len(check)):
        print("Anagram")
    else:
        print("Not a Anagram")

