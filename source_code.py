import tkinter as tk

render = None


def write_slogan():
    # get image and display
    image = tk.PhotoImage(file="1.png")
    imageLabel.configure(image=image)
    imageLabel.image = image


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

imageLabel = tk.Label(frame)
imageLabel.pack(side=tk.LEFT)

root.mainloop()
