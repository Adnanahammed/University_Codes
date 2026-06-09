from tkinter import *

# Event handler function
def handle_click():
    user_input = entry.get()
    print(f"User entered: {user_input}")

# Initialize main window
root = Tk()
root.title("My GUI Application")
root.geometry("300x200")

# Create and pack widgets
label = Label(root, text="Enter your name:", fg="blue")
label.pack(pady=10)

entry = Entry(root, width=20)
entry.pack(pady=5)

submit_btn = Button(root, text="Submit", command=handle_click)
submit_btn.pack(pady=10)

# Start the event loop
root.mainloop()