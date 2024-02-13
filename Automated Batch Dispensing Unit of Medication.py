def process_orders(item_quantities, orders):
    remaining_quantities = item_quantities.copy()
    selected_quantities_per_order = {}

    for order in orders:
        print(f"\nProcessing {order}...")
        print(f"Available quantities: {remaining_quantities}")

        selected_items = []
        order_quantity_total = 0

        while True:
            selected_item = input(f"Select item for {order} (A, B, C, D) or 'done' to finish: ").upper()

            if selected_item == 'DONE':
                break

            if selected_item in remaining_quantities:
                while True:
                    try:
                        order_quantity = int(input(f"Enter quantity for {selected_item}: "))
                        if 0 <= order_quantity <= remaining_quantities[selected_item]:
                            break
                        else:
                            print(f"Invalid quantity. Available quantity for {selected_item}: {remaining_quantities[selected_item]}")
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

                order_quantity_total += order_quantity
                remaining_quantities[selected_item] -= order_quantity
                selected_items.append((selected_item, order_quantity))

            else:
                print("Invalid input. Please select a valid item.")

        selected_quantities_per_order[order] = selected_items
        print(f"You selected in {order}: {', '.join([f'{item} = {qty}' for item, qty in selected_items])}")
        print(f"Remaining quantities after {order}: {remaining_quantities}")

    print(f"\nFinal remaining quantities: {remaining_quantities}")
    print(f"Quantities selected in each order: {selected_quantities_per_order}")

# Example usage:
item_quantities_available = {'A': 10, 'B': 20, 'C': 10, 'D': 5}
order_dict = {
    "Order1": 0,  # Initial values can be set to 0; the user will select the item and quantity
    "Order2": 0,
    "Order3": 0,
    "Order4": 0
}

process_orders(item_quantities_available, order_dict)
