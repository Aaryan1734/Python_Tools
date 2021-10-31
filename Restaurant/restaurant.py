from tkinter import *
from functions import total_button, reset_button, quit_exit
from variables import *


def restaurant():
    # region frame info
    lbl_info = Label(tops, font=('Comic Sans MS', 25, 'bold'), text="Welcome to Ain's Diner!", fg='green3', bd=5,
                     anchor='w')
    lbl_info.grid(row=0, column=0)
    # endregion
    # region meals
    meal_label = Label(frame, font=('Comic Sans MS', 12, 'bold'), text='Meals')
    meal_label.grid(row=0, column=0, columnspan=3)

    chicken_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                          text=f'Chicken Meal, \n${chicken_price}', bd=10, anchor='w')
    chicken_label.grid(row=1, column=0)
    chicken_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=chicken_meal, bd=10, insertwidth=4, bg='gold', fg='black',
                         justify=RIGHT)
    chicken_text.grid(row=1, column=1)
    chicken_desc = Label(frame, font=('Comic Sans MS', 10),
                         text='Chicken wings \n plus burger and sauce', bd=10, anchor='w', justify=CENTER)
    chicken_desc.grid(row=1, column=2)

    veggie_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                         text=f'Veggie Meal, \n${veggie_price}', bd=10, anchor='w')
    veggie_label.grid(row=2, column=0)
    veggie_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=veggie_meal, bd=10, insertwidth=4, bg='gold', fg='black',
                        justify=RIGHT)
    veggie_text.grid(row=2, column=1)
    veggie_desc = Label(frame, font=('Comic Sans MS', 10),
                        text='3 vegetarian dishes \nplus soup', bd=10, anchor='w')
    veggie_desc.grid(row=2, column=2)

    cheese_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                         text=f'Spicy Cheese Meal, \n${cheese_price}', bd=10, anchor='w')
    cheese_label.grid(row=3, column=0)
    cheese_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=cheese_meal, bd=10, insertwidth=4, bg='gold', fg='black',
                        justify=RIGHT)
    cheese_text.grid(row=3, column=1)
    cheese_desc = Label(frame, font=('Comic Sans MS', 10),
                        text='Many types of spicy cheese\nplus Cheese Soup', bd=10, anchor='w', justify=CENTER)
    cheese_desc.grid(row=3, column=2)

    fillet_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                         text=f'Fillet Meal, \n${fillet_price}', bd=10, anchor='w')
    fillet_label.grid(row=4, column=0)
    fillet_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=fillet_meal, bd=10, insertwidth=4, bg='gold', fg='black',
                        justify=RIGHT)
    fillet_text.grid(row=4, column=1)
    fillet_desc = Label(frame, font=('Comic Sans MS', 10),
                        text='Meat fillet in sauce', bd=10, anchor='w', justify=CENTER)
    fillet_desc.grid(row=4, column=2)

    fish_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                       text=f"Fish O' Meal, \n${fish_price}", bd=10, anchor='w')
    fish_label.grid(row=5, column=0)
    fish_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=fish_meal, bd=10, insertwidth=4, bg='gold', fg='black',
                      justify=RIGHT)
    fish_text.grid(row=5, column=1)
    fish_desc = Label(frame, font=('Comic Sans MS', 10),
                      text='Fish plus sauces', bd=10, anchor='w', justify=CENTER)
    fish_desc.grid(row=5, column=2)

    fries_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                        text=f'Fries Meal, \n${fries_price}', bd=10, anchor='w')
    fries_label.grid(row=6, column=0)
    fries_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=fries_meal, bd=10, insertwidth=4, bg='gold', fg='black',
                       justify=RIGHT)
    fries_text.grid(row=6, column=1)
    fries_desc = Label(frame, font=('Comic Sans MS', 10),
                       text='5 types of fries \nplus sauces', bd=10, anchor='w', justify=CENTER)
    fries_desc.grid(row=6, column=2)

    # endregion
    # region dishes
    dish_label = Label(frame, font=('Comic Sans MS', 12,
                                    'bold'), text='Dishes/Desserts')
    dish_label.grid(row=0, column=3, columnspan=3)
    chburg_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                         text=f'Chicken Burger, \n${chburg_price}', bd=10, anchor='w')
    chburg_label.grid(row=1, column=3)
    chburg_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=chicken_burger, bd=10, insertwidth=4, bg='dodger blue', fg='black',
                        justify=RIGHT)
    chburg_text.grid(row=1, column=4)
    chburg_desc = Label(frame, font=('Comic Sans MS', 10),
                        text='Chicken Burger', bd=10, anchor='w')
    chburg_desc.grid(row=1, column=5)

    vgburg_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                         text=f'Veggie Burger, \n${vgburg_price}', bd=10, anchor='w')
    vgburg_label.grid(row=2, column=3)
    vgburg_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=veggie_burger, bd=10, insertwidth=4, bg='dodger blue', fg='black',
                        justify=RIGHT)
    vgburg_text.grid(row=2, column=4)
    vgburg_desc = Label(frame, font=('Comic Sans MS', 10),
                        text='Vegetarian Burger', bd=10, anchor='w')
    vgburg_desc.grid(row=2, column=5)

    taco_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                       text=f'Taco, \n${taco_price}', bd=10, anchor='w')
    taco_label.grid(row=3, column=3)
    taco_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=taco, bd=10, insertwidth=4, bg='dodger blue', fg='black',
                      justify=RIGHT)
    taco_text.grid(row=3, column=4)
    taco_desc = Label(frame, font=('Comic Sans MS', 10),
                      text='Soft Shell \nVegetarian Taco', bd=10, anchor='w')
    taco_desc.grid(row=3, column=5)

    icecream_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                           text=f'Ice Cream, \n${icecream_price}', bd=10, anchor='w')
    icecream_label.grid(row=4, column=3)
    icecream_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=ice_cream, bd=10, insertwidth=4, bg='dodger blue', fg='black',
                          justify=RIGHT)
    icecream_text.grid(row=4, column=4)
    icecream_desc = Label(frame, font=('Comic Sans MS', 10),
                          text='Vanilla Ice \nCream Cone', bd=10, anchor='w')
    icecream_desc.grid(row=4, column=5)

    cookies_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                          text=f'Cookies, \n${cookies_price}', bd=10, anchor='w')
    cookies_label.grid(row=5, column=3)
    cookies_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=cookies, bd=10, insertwidth=4, bg='dodger blue', fg='black',
                         justify=RIGHT)
    cookies_text.grid(row=5, column=4)
    cookies_desc = Label(frame, font=('Comic Sans MS', 10),
                         text='Warm, fresh chocolate \nchip cookies', bd=10, anchor='w')
    cookies_desc.grid(row=5, column=5)

    drinks_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                         text=f'Drinks, \n${drinks_price}', bd=10, anchor='w')
    drinks_label.grid(row=6, column=3)
    drinks_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=drinks, bd=10, insertwidth=4, bg='dodger blue', fg='black',
                        justify=RIGHT)
    drinks_text.grid(row=6, column=4)
    drinks_desc = Label(frame, font=('Comic Sans MS', 10),
                        text='Fruit Juice/Soda', bd=10, anchor='w')
    drinks_desc.grid(row=6, column=5)
    # endregion
    # region result
    result_label = Label(frame, font=('Comic Sans MS', 12,
                                      'bold'), text='Result (DO NOT TYPE)')
    result_label.grid(row=0, column=6, columnspan=2)
    order_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                        text='Order No.', bd=10, anchor='w')
    order_label.grid(row=1, column=6)
    order_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=order, bd=10, insertwidth=4, bg='green3', fg="black",
                       justify=RIGHT)
    order_text.grid(row=1, column=7)

    cost_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                       text='Cost', bd=10, anchor='w')
    cost_label.grid(row=2, column=6)
    cost_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=cost, bd=10, insertwidth=4, bg='green3', fg="black",
                      justify=RIGHT)
    cost_text.grid(row=2, column=7)

    service_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                          text='Service', bd=10, anchor='w')
    service_label.grid(row=3, column=6)
    service_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=service, bd=10, insertwidth=4, bg='green3', fg="black",
                         justify=RIGHT)
    service_text.grid(row=3, column=7)

    tax_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                      text='Tax', bd=10, anchor='w')
    tax_label.grid(row=4, column=6)
    tax_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=tax, bd=10, insertwidth=4, bg='green3', fg="black",
                     justify=RIGHT)
    tax_text.grid(row=4, column=7)

    subtotal_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                           text='Sub Total', bd=10, anchor='w')
    subtotal_label.grid(row=5, column=6)
    subtotal_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=sub_total, bd=10, insertwidth=4, bg='green3', fg="black",
                          justify=RIGHT)
    subtotal_text.grid(row=5, column=7)

    total_label = Label(frame, font=('Comic Sans MS', 10, 'bold'),
                        text='Total', bd=10, anchor='w')
    total_label.grid(row=6, column=6)
    total_text = Entry(frame, font=('Comic Sans MS', 10, 'bold'), textvariable=total, bd=10, insertwidth=4, bg='green3', fg="black",
                       justify=RIGHT)
    total_text.grid(row=6, column=7)
    # endregion
    # region buttons
    empty = Label(frame, font=('Comic Sans MS', 12, 'bold'), text='')
    empty.grid(row=7, column=0, rowspan=2, columnspan=7)

    button_total = Button(frame, padx=20, pady=12, bd=12, fg='black', font=('Comic Sans MS', 12, 'bold'), width=10,
                          text='Total', bg='dodger blue', command=lambda: total_button()).grid(row=9, column=2)
    button_reset = Button(frame, padx=20, pady=12, bd=12, fg='black', font=('Comic Sans MS', 12, 'bold'), width=10,
                          text='Reset', bg='green3', command=lambda: reset_button()).grid(row=9, column=4)
    button_quit = Button(frame, padx=20, pady=12, bd=12, fg='black', font=('Comic Sans MS', 12, 'bold'), width=10,
                         text='Quit', bg='gold', command=lambda: quit_exit()).grid(row=9, column=6)
    # endregion

    root.mainloop()
