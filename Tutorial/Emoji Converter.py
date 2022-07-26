message = input("> ")
words = message.split(' ') #--> Allows each word to be checked/replaced using the dictionary

emoji = {
    ":)": "😊",
    ":(":"😢" #<--Replaces only these specific strings. Hence, dictionary
}

output = "" #--> Creates the line of text, without it, the words would print one-by-one
for word in words:
        output += emoji.get(word, word) + " "
print(output)                      #^ Uses whatever the word was if it's not in the dictionary
