#Assigment3
print("Cipher Text:")
a=open("text.txt","r")
print(a.read())
print("Analysis:")
import string
text = open('text.txt')
letters = string.ascii_letters
for i in text:
  text_upper = i.upper()
  text_nospace = text_upper.replace(" ", "")
  text_nopunctuation = text_nospace.strip(string.punctuation)
  for a in letters:
    if a in text_nopunctuation:
      num = text_nopunctuation.count(a)
      print(a,"->", num,end=', ')

print("\n""options:")


def menu():
  print(" 1)take a replace rule:")
  print(" 2)exit:")


menu()
option = int(input("Enter your option:"))

while option != 0:
  if option == 1:
    print("Enter Replacment Rule->")

  elif option == 2:
    exit()
  else:
    print("invalid option:")

  print()
  menu()
  option = int(input("Enter your option:"))
