#concatenation of string
str1="bomb"
str2="blast"
result = str1 + "" + str2
print(result)

#Finding length of string
text = "Monkey D Luffy"
length = len(text)
print("Length of string is:", length)

#Changing case of string
#upper() and lower()
yup="Monkey D Garp"
upper= yup.upper()
lower= yup.lower()

print ("Upper case string is:", upper)
print ("Lower case string is:", lower)


#String replacement
#replace()
chef=" Sanji zoro"
new_chef= chef.replace("Zoro", "Black foot")
print("The Chef is:", new_chef)


#String slicing
#split()
Swordsman = "Roronoa Zoro"
Cut = Swordsman.split()
print("The Swordsman is:", Cut)

#String stripping
#strip()
#strip() removes leading and trailing whitespace
text = "Monkey D Luffy                "
strip_text = text.strip()
print("String after stripping whitespace:", strip_text)

#substring of text
#substring
text = "Monkey D Luffy"
substring ="D"
if substring in text:
    print ("Substring is found which is Will of D", substring)

    



