

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
    #         for offer in offers:
    #             offer_quantity = offer["quantity"]
    #             offer_price = offer["offer_price"]
    #
    #             if count !=
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

    price_table = {'A': (50, [(5, 200), (3, 130)]), 'B': (30, [(2, 45)]), 'C': (20, []), 'D': (15, []),
                   'E': (40, [(2, 0, 'B')])}
    basket = {}
    total_price = 0

    # Count the number of occurrences of each item in the basket
    for item in skus:
        if item not in price_table:
            return -1  # Return -1 for illegal input
        basket[item] = basket.get(item, 0) + 1

    # Calculate the total price based on the price table and special offers
    for item, count in basket.items():
        price, special_offers = price_table[item]
        remaining_items = count

        for special_offer in special_offers:
            special_count, special_price, free_item = special_offer

            special_offer_applicable = remaining_items // special_count
            remaining_items %= special_count

            total_price += special_offer_applicable * special_price

            if free_item is not None and free_item in basket:
                free_item_count = min(basket[free_item], special_offer_applicable)
                basket[free_item] -= free_item_count
                remaining_items -= free_item_count

        total_price += remaining_items * price

    return total_price





