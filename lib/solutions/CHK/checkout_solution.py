

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    price_table = {
        'A': {'price': 50, 'offer': [{'quantity': 3, 'offer_price': 130}, {'quantity': 5, 'offer_price': 200}]},
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

    total_price = 0

    for product, count in item_counts.items():
        item_price = price_table[product]["offer_price"]
        if "offer" in price_table[product]:
            offer = price_table[product]['offer']
            offer.sort(key = lambda x: x.get("quantity", 0), reverse=True)

            for offer in price_table[product]:
                if "quantity" in offer and "offer_price" in offer:
                    offer_quantity = offer["quantity"]
                    offer_price = offer["price"]
                    q, r = divmod(count, offer_quantity)
                    total_price += q, offer_price
                    count = r

                if "quantity" in offer and "free_item" in offer:
                    offer_quantity = offer["quantity"]
                    free_item = offer["offer_item"]
                    free_item_count = item_counts.get(free_item, 0)
                    max_free_items = min(count // offer_quantity, free_item_count)
                    total_price += max_free_items * item_price
                    count -= max_free_items * offer_quantity

        total_price += count * item_price

    return total_price

