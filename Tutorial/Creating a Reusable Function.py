def emoji_converter(message):
    words = message.split(' ')

    emoji = {
        ":)": "😊",
        ":(": "😢"
    }

    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
        return output #returns the value of the function


message = input("> ") #thats how def works, include the arguments here
print(emoji_converter(message))