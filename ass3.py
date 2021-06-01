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
  print(" 1)try a replace rule written in the code:")
  print(" 2)exit:")

def replace_rule():
  # read the file
  #apply rule
  dict={"M":'a',"A":'b',"N":'c',"D":'l',"U":'d',"S":'e',"C":'f',"E":"m","F":'n',"B":'k',"G":'o',"H":'p',"I":'h',"J":'q',"K":'r',"L":'s',"O":'t',"P":'i',"Q":'u',"R":'g',"V":'v',"W":'w',"X":'x',"Y":'y'}
  cipher_text=""
  text = open('text.txt')
  for t in text:
    for key in dict.keys():
      t = t.replace(key, dict[key])
    cipher_text +=t
  print(cipher_text)


menu()
option = int(input("Enter your option:"))

while option != 0:
  if option == 1:
    print("Plain text:")
    replace_rule()

  elif option == 2:
    exit()
  else:
    print("invalid option:")

  print()
  menu()
  option = int(input("Enter your option:"))
