# Happy New Year (2024)

def Eprint(Data) -> None:
  print(Data, end = "")

print("1. A full christmas tree")
print("2. A half christmas tree")
Option = input("-> ")

if(Option == "1"):
  Number = 2
elif(Option == "2"):
  Number = 1
else:
  print("Invalid option!")
  exit()

Lines = input("Enter number of lines: ")

try:
  Lines = int(Lines)
except:
  print("The number of lines must be an integer!")
  exit()

if(Lines < 1):
  print("The number of lines must be greater than 0!")
  exit()

Asterisks = 1

for I in range(Lines):
  for J in range(Lines-I-1):
    Eprint(" ")

  for K in range(Asterisks):
    Eprint("*")

  Asterisks = Asterisks + Number
  Eprint("\n")

if(Option == "1"):
  Iterations = int(Asterisks / 2) - 1
  
  for I in range(3):
    for J in range(Iterations):
      Eprint(" ")
    
    Eprint("|\n")