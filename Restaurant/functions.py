import random
from variables import *


def total_button():
    try:
        x = random.randint(100000, 1000000)
        order_no = str(x)
        order.set(order_no)

        fries_meal_cost = float(fries_meal.get())*fries_price
        veggie_meal_cost = float(veggie_meal.get())*veggie_price
        fillet_meal_cost = float(fillet_meal.get())*fillet_price
        fish_meal_cost = float(fish_meal.get())*fish_price
        chicken_meal_cost = float(chicken_meal.get())*chicken_price
        cheese_meal_cost = float(cheese_meal.get())*cheese_price
        chburg_cost = float(chicken_burger.get())*chburg_price
        vgburg_cost = float(veggie_burger.get())*vgburg_price
        taco_cost = float(taco.get())*taco_price
        icecream_cost = float(ice_cream.get())*icecream_price
        cookies_cost = float(cookies.get())*cookies_price
        drinks_cost = float(drinks.get())*drinks_price

        items_cost = (fries_meal_cost + veggie_meal_cost + fillet_meal_cost + fish_meal_cost + chicken_meal_cost +
                      cheese_meal_cost + chburg_cost + vgburg_cost + taco_cost + icecream_cost + cookies_cost + drinks_cost)
        meal_cost = f"${round(items_cost, 2)}"
        taxed = ((items_cost)*0.09)
        total_cost = (items_cost)
        service_charge = ((fries_meal_cost + veggie_meal_cost + fish_meal_cost + chicken_meal_cost +
                          cheese_meal_cost + chburg_cost + vgburg_cost + taco_cost + icecream_cost + cookies_cost + drinks_cost)/99)
        ser_charge = f"${round(service_charge, 2)}"
        overall_cost = f"${round(taxed + total_cost + service_charge, 2)}"
        paid_tax = f"${round(taxed, 2)}"

        service.set(ser_charge)
        cost.set(meal_cost)
        tax.set(paid_tax)
        sub_total.set(meal_cost)
        total.set(overall_cost)
    except ValueError:
        reset_button()


def reset_button():
    fries_meal.set('')
    veggie_meal.set('')
    fillet_meal.set('')
    fish_meal.set('')
    cheese_meal.set('')
    chicken_meal.set('')

    chicken_burger.set('')
    veggie_burger.set('')
    taco.set('')
    ice_cream.set('')
    cookies.set('')
    drinks.set('')

    order.set('')
    cost.set('')
    service.set('')
    tax.set('')
    sub_total.set('')
    total.set('')


def quit_exit():
    root.destroy()
