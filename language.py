print("Please select a language: English, Spanish, or French")
language = input()
lang = language[0]
print("Wow, you speak, "+ language +", right?")
if lang == "E" or lang=="e":
    print("You speal the Queen's English")
elif lang in ["S" , "s"]:
    print("Hola!Que pasa")
elif lang =="F" or lang =="f":
    print("Je veux un cake. Et toi?")
else:
    print("It doesn't work")
