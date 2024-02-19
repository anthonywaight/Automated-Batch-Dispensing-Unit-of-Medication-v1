from ABDU import process_orders

#manage available quantities here
item_quantities_available = {'A': 10, 'B': 20, 'C': 10, 'D': 5}
order_dict = {
    "Order1": 0,  # Initial values can be set to 0; the user will select the item and quantity
    "Order2": 0,
    "Order3": 0,
    "Order4": 0
}
results = process_orders(item_quantities_available,order_dict)
print(results)