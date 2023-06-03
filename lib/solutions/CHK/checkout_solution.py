

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

                if not isinstance(offer_value, str):

                    if count == offer_qty:
                        count = 1
                        price_table[item]['price'] = offer_value
                    else:
                        remaining = count / offer_qty
                        while count > offer_qty:
                            print(offer_qty, offer_value)
                            total_price += offer_qty * price_table[item]['price']
                            count -= remaining

                if offer_value in item_counts:
                    item_counts[offer_value] = 0

        total_price += count * price_table[item]['price']

    return total_price

