def translater(phrase):
    translation = ""
    for letters in phrase:
        if letters.lower() in "aeiou": #makes letters in lower case so that it works for uppercase letters
            if letters.isupper(): #considers uppercase letters and makes them uppercase "G"
                translation += "G"
            else: #considers lowercase letters and makes them uppercase "g"
                translation += "g"
        else:
            translation += letters #if not a vowel or "aeiou" it just uses whatever the phrase/letter(s) is
    return translation

#print(translater("dog")) #For specific words/phrases
print(translater(input("Enter some words: "))) #Allows for you to choose what "phrase" goes through the translato   r