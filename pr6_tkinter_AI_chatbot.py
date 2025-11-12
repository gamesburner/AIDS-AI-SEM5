from tkinter import *

root = Tk()
root.title("Chatbot")

def send():
    send_text = "\nYou : " + e.get()
    txt.insert(END, send_text)
    user = e.get().lower()

    if user == "hello":
        txt.insert(END, "\nBot : Hi\n")
    elif user in ["hi", "hii", "hiiii"]:
        txt.insert(END, "\nBot : Hello\n")
    elif user == "how are you":
        txt.insert(END, "\nBot : fine! and you\n")
    elif user in ["fine", "i am good", "i am doing good"]:
        txt.insert(END, "\nBot : Great! how can I help you.\n")
    else:
        txt.insert(END, "\nBot : Sorry! I didn't get you\n")

    e.delete(0, END)

# Chat display
txt = Text(root, wrap=WORD)
txt.grid(row=0, column=0, columnspan=2)

# Entry box
e = Entry(root, width=100)
e.grid(row=1, column=0)

# Send button
Button(root, text="Send", command=send).grid(row=1, column=1)

root.mainloop()
