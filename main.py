from tkinter import *
from textblob import TextBlob

APP_LABEL_FONT = ("Arial", 25, "bold")
CORRECT_LABEL_FONT = ("Arial", 15)


# Function
# Check function
def check():
    input_word = input_word_var.get()
    correct_word.set(str(TextBlob(input_word).correct()))
    input_word_var.set("")


# Main window
root = Tk()
root.title("Spelling Checker App")
root.configure(background="cadetblue1")
root.config(padx=50, pady=50)

# Label
# App label
app_label = Label(text="Spelling Checker",
                  font=APP_LABEL_FONT,
                  bg="cadetblue1",
                  fg="cornflowerblue")
app_label.grid(row=0,
               column=0,
               columnspan=2,
               pady=10)

# Correct label
correct_label = Label(text=f"Correct spelling is:",
                      font=CORRECT_LABEL_FONT,
                      fg="cyan3",
                      bg="cadetblue1")
correct_label.grid(row=3,
                   column=0,
                   pady=10)

# Correct word label
correct_word = StringVar()
correct_word_label = Label(textvariable=correct_word,
                           bg="cadetblue1",
                           font=CORRECT_LABEL_FONT,
                           fg="cyan4")
correct_word_label.grid(row=3, column=1, pady=10)

# Entry
# User entry
input_word_var = StringVar()
user_entry = Entry(width=40, textvariable=input_word_var)
user_entry.grid(row=1,
                column=0,
                ipady=5,
                columnspan=2,
                pady=10)

# Button
# Check button
check_btn = Button(text="Check",
                   highlightthickness=0,
                   width=10,
                   bg="yellow",
                   command=check)

check_btn.grid(row=2,
               column=0,
               columnspan=2,
               pady=10)

root.mainloop()
