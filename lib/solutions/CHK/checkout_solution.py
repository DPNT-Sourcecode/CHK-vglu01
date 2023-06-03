

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    price_table = {
        'A': {'price': 50, 'offer': {'quantity': 3, 'offer_price': 130}},
        'B': {'price': 30, 'offer': {'quantity': 2, 'offer_price': 45}},
        'C': {'price': 20},
        'D': {'price': 15},
        'E': {'price': 40, 'offer': {'quantity': 2, 'free_item': 'B'}},
    }

    item_counts = {}

    for i in skus:
        if i not in price_table:
            return -1

        if i in item_counts:
            item_counts[i] += 1
        else:
            item_counts[i] = 1

    for product, count in item_counts.items():
        if 'offer' in price_table[product]:
            offer = price_table[product]['offer']
            offer_quantity = offer['quantity']
            if product == "E" and offer['free_item'] in item_counts:
                free_item_count = item_counts[offer["free_item"]]
                print(free_item_count, count)
                free_item_count -= count
                if free_item_count < 0:
                    free_item_count = 0
                item_counts[offer["free_item"]] = free_item_count


            if product == "B" and "offer" in price_table[product]:
                offer = price_table[product]["offer"]
                offer_quantity = offer["quantity"]
                if offer_quantity <= count:
                    free_item_count = count
                    item_counts[product] -= free_item_count


    total_price = 0

    for product, count in item_counts.items():
        if 'offer' in price_table[product]:
            offer = price_table[product]['offer']
            offer_quantity = offer['quantity']
            offer_price = offer.get("offer_price")
            while count >= offer_quantity:
                total_price += offer_price
                count -= offer_quantity

        total_price += count * price_table[product]["price"]

    return total_price





