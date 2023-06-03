

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):


    price_table = {
        'A': {'price': 50, 'special_offer': [(5, 200), (3, 130)]},
        'B': {'price': 30, 'special_offer': [(2, 45)]},
        'C': {'price': 20},
        'D': {'price': 15},
        'E': {'price': 40, 'special_offer': [(2, 'B')]}
    }

    item_counts = {}
    total_price = 0
    free_items = {}

    for item in skus:
        if item in price_table:
            item_counts[item] = item_counts.get(item, 0) + 1
        else:
            return -1


    for item, count in item_counts.items():
        if 'special_offer' in price_table[item]:
            special_offers = price_table[item]['special_offer']
            for offer in special_offers:
                offer_qty, offer_value = offer

                if offer_value != item or item_counts.get(offer_value, 0) < offer_qty:
                    while count >= offer_qty:
                        total_price += offer_qty * price_table[item]['price']
                        count -= offer_qty
                elif offer_value == item and count >= offer_qty and item_counts.get(offer_value,
                                                                                    0) >= offer_qty:
                    special_offer_count = count // offer_qty
                    remaining_items = count % offer_qty
                    total_price += special_offer_count * offer_qty * price_table[item]['price']
                    total_price += remaining_items * price_table[item]['price']
                    count = remaining_items

        total_price += count * price_table[item]['price']
        print(total_price)

        if item in free_items:
            free_items_count = min(count, free_items[item])
            free_items[item] -= free_items_count
            count -= free_items_count
            total_price -= free_items_count * price_table[item]['price']


        if 'special_offer' in price_table[item]:
            for offer in price_table[item]['special_offer']:
                offer_qty, offer_item = offer
                if item_counts.get(offer_item, 0) >= offer_qty:
                    free_items[offer_item] = item_counts[offer_item] // offer_qty

    return total_price
