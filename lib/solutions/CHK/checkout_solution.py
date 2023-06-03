

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    price_table = {
        'A': {'price': 50, 'offer': {'quantity': 3, 'offer_price': 130}},
        'B': {'price': 30, 'offer': {'quantity': 2, 'offer_price': 45}},
        'C': {'price': 20},
        'D': {'price': 15},
    }

    item_counts = {}

    for i in skus:
        if i not in price_table:
            return -1

        if i in item_counts:
            item_counts[i] += 1
        else:
            item_counts[i] = 1

    total_price = 0

    for product, count in item_counts.items():
        if 'offer' in price_table[product]:
            offer = price_table[product]['offer']
            offer_quantity = offer['quantity']
            offer_price = offer["offer_price"]

            while count >= offer_quantity:
                total_price += offer_price
                count -= offer_quantity

        total_price += count * price_table[product]["price"]

    return total_price

