while True:
    text = input()
    if ("hello" in text or "Hello") in text:
        print("Hello there, good stranger")
    if ("How are you" in text):
        print("I am fine, thanks. How are you?")
    if ("feelings" in text or "Feelings" in text):
        print("I am machine. I have not feelings")
        
    if ("Age" in text or "age" in text):
        print("I am a machine, I have no age, just current timestamp")
