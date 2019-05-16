string1 = "Be kind to your "
string2 = "-footed "
string3 = ". \nFor a duck may be somebody`s "
string4 = ". \nBe kind to your "
string5 = " at "
string6 = ". \nWhere the weather is always "
string7 = ". \nYou may think that this is the "
string8 = ". \nWell it is."
print("Let's play a game of MadLibs.\n Enter a...")
a=str(raw_input("\nnoun: "))
string1+=str(a)
b=str(raw_input("\nplural noun: "))
string2+=str(b)
c=str(raw_input("\nnoun: "))
string3+=str(c)
d=str(raw_input("\nplural noun: "))
string4+=str(d)
e=str(raw_input("\nplace: "))
string5+=str(e)
f=str(raw_input("\nadjective: "))
string6+=str(f)
g=str(raw_input("\nnoun: "))
string7+=str(g)
print("\nHere is your story:")
print(str(string1 + string2 + string3 + string4 + string5 + string6 + string7 + string8))
