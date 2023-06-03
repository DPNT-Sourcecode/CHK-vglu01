

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
                while count >= offer_qty:

                    if isinstance(offer_value, str):
                        # total_price += offer_qty * price_table[offer_value]['price']
                        if offer_value == 'B':
                            if count >= offer_qty * 2:
                                total_price += price_table[item]['price'] * offer_qty
                                count -= offer_qty
                                continue
                        offer_item_price = price_table[offer_value]['price']
                        total_price += offer_item_price
                    else:
                        total_price += offer_value

                    count -= offer_qty

        total_price += count * price_table[item]['price']


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

