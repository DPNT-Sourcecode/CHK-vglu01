

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # price_table = {
    #     'A': {'price': 50, 'offers': [{'quantity': 3, 'offer_price': 130}, {'quantity': 5, 'offer_price': 200}]},
    #     'B': {'price': 30, 'offer': {'quantity': 2, 'offer_price': 45}},
    #     'C': {'price': 20},
    #     'D': {'price': 15},
    #     'E': {'price': 40, 'offer': {'quantity': 2, 'free_item': 'B'}}
    # }
    #
    # item_counts = {}
    #
    # for i in skus:
    #     if i not in price_table:
    #         return -1
    #
    #     if i in item_counts:
    #         item_counts[i] += 1
    #     else:
    #         item_counts[i] = 1
    #
    # total_price = 0
    #
    # for product, count in item_counts.items():
    #     if "offers" in price_table[product]:
    #         offers = price_table[product]['offers']
    #
    #         for offer in offers:
    #             offer_quantity = offer["quantity"]
    #             offer_price = offer["offer_price"]
    #
    #
    #             while count >= offer_quantity:
    #                 # print(product, count, offer_quantity)
    #                 total_price += offer_price
    #                 count -= offer_quantity
    #     item_counts[product] = count
    #     if "offer" in price_table[product]:
    #         offer = price_table[product]["offer"]
    #         offer_quantity = offer["quantity"]
    #         if product == "E" and offer["free_item"] in item_counts:
    #             free_item_count = item_counts[offer["free_item"]]
    #             offer_applicable_count = min(count // offer_quantity, free_item_count)
    #             total_price += offer_applicable_count * price_table[product]["price"]
    #             # total_price += (count - offer_applicable_count) * price_table[product]['price']
    #             item_counts[offer['free_item']] -= offer_applicable_count
    #
    # print(item_counts)
    # for item, count in item_counts.items():
    #     total_price += count * price_table[item]["price"]
    # return total_price

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

    # Count the occurrences of each item
    for item in skus:
        if item in price_table:
            item_counts[item] = item_counts.get(item, 0) + 1
        else:
            return -1  # Invalid item found

    # Calculate the total price
    for item, count in item_counts.items():
        if 'special_offer' in price_table[item]:
            special_offers = price_table[item]['special_offer']
            for offer in special_offers:
                offer_qty, offer_value = offer
                while count >= offer_qty:
                    total_price += price_table[offer_value]["price"]
                    count -= offer_qty
        total_price += count * price_table[item]['price']

        # Update free items count
        if item in free_items:
            free_items_count = min(count, free_items[item])
            free_items[item] -= free_items_count
            count -= free_items_count
            total_price -= free_items_count * price_table[item]['price']

        # Check if item generates free items
        if 'special_offer' in price_table[item]:
            for offer in price_table[item]['special_offer']:
                offer_qty, offer_item = offer
                if item_counts.get(offer_item, 0) >= offer_qty:
                    free_items[offer_item] = item_counts[offer_item] // offer_qty

    return total_price

