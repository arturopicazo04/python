from tkinter import *
import settings
import utils

root = Tk()
# Override settings
root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=settings.width,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg="black",
    width=settings.width - utils.width_prct(25),
    height=settings.height - utils.height_prct(25)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

# Run window
root.mainloop()
