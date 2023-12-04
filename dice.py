from tkinter import *
import random

root = Tk()
root.geometry("500x500")

# Get The Dice Number . We used unicode characters instead of real images
def get_number(x):
	if x == '\u2680':
		return(1)
	elif x == '\u2681':
		return(2)
	elif x == '\u2682':
		return(3)
	elif x == '\u2683':
		return(4)
	elif x == '\u2684':
		return(5)
	elif x == '\u2685':
		return(6)

# Roll the dice
def roll_dice():
	# Roll Random Dice
	d1 = random.choice(my_dice)
	d2 = random.choice(my_dice)

	# Determine Dice Number
	sd1 = get_number(d1)
	sd2 = get_number(d2)

	# Update Labels
	dice_label1.config(text=d1)
	dice_label2.config(text=d2)

	# Update Sub Labels
	sub_dice_label1.config(text=sd1)
	sub_dice_label2.config(text=sd2)

	# Update Total Label
	total = sd1 + sd2
	total_label.config(text=f"Total Rolled: {total}")


# Create A Dice List
my_dice = ['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685',]

# Create a Frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create Dice Labels
dice_label1 = Label(my_frame, text='', font=("Tahoma", 100), fg="green")
dice_label1.grid(row=0, column=0, padx=20)
sub_dice_label1 = Label(my_frame, text="")
sub_dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, text='', font=("Tahoma", 100), fg="green")
dice_label2.grid(row=0, column=1, padx=20)
sub_dice_label2 = Label(my_frame, text="")
sub_dice_label2.grid(row=1, column=1)


# Create Roll Button
my_button = Button(root, text="Roll Dice", command=roll_dice, font=("Tahoma", 24),fg="green")
my_button.pack(pady=20)

# Create Totals Label
total_label = Label(root, text="", font=("Tahoma", 20), fg="green")
total_label.pack(pady=40)


# Roll the dice
roll_dice()

root.mainloop()
