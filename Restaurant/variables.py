from tkinter import *

#region root and frames
root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f'{width}x{height}')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='soup-plate.gif'))
root.tk_setPalette(background='gray20')
root.title("Ain's Diner Online Order")

tops = Frame(root, width=800, height=25, bg='gray20', relief=SUNKEN)
tops.pack(side=TOP)

bottom = Frame(root, width=800, height=25, bg='gray20', relief=SUNKEN)
bottom.pack(side=BOTTOM)

frame = Frame(root, width=800, height=500, relief=SUNKEN)
frame.pack(side=LEFT)
#endregion

#region variables
fries_price = 6.99
veggie_price = 7.99
fillet_price = 9.99
fish_price = 9.99
chicken_price = 8.99
cheese_price = 6.49
drinks_price = 0.49
chburg_price = 4.99
vgburg_price = 3.99
taco_price = 2.99
cookies_price = 0.49
icecream_price = 0.99

fries_meal = StringVar()
veggie_meal = StringVar()
fillet_meal = StringVar()
fish_meal = StringVar()
chicken_meal = StringVar()
cheese_meal = StringVar()

chicken_burger = StringVar()
veggie_burger = StringVar()
taco = StringVar()
ice_cream = StringVar()
cookies = StringVar()
drinks = StringVar()

order = StringVar()
cost = StringVar()
service = StringVar()
tax = StringVar()
sub_total = StringVar()
total = StringVar()
#endregion
