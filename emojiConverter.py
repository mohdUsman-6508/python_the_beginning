# one of the application of dictionary

def emoji_converter(message):
    msg_list = message.split(" ")
    emoji = {
        ":(": "☹️",
        ":)": "😎"
    }
    out = " "
    for word in msg_list:
        out += emoji.get(word, word) + ' '
    return out


print(emoji_converter("hello :)"))
print(emoji_converter('wow :('))


