def main():
    message = input("Enter a message : ")
    new_message = convert(message)
    print(new_message)

def convert(text):
    text = text.replace(":)","🙂").replace(":(","🙁")
    return text

main()