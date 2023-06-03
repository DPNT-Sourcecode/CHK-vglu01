

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    price_table = {
        'A': {'price': 50, 'offers': [{'quantity': 3, 'offer_price': 130}, {'quantity': 5, 'offer_price': 200}]},
        'B': {'price': 30, 'offer': {'quantity': 2, 'offer_price': 45}},
        'C': {'price': 20},
        'D': {'price': 15},
        'E': {'price': 40, 'offer': {'quantity': 2, 'free_item': 'B'}}
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
        if "offers" in price_table[product]:
            offers = price_table[product]['offers']
            for offer in offers:
                offer_quantity = offer["quantity"]
                offer_price = offer["offer_price"]

                while count >= offer_quantity:
                    total_price += offer_price
                    count -= offer_quantity

        if "offer" in price_table[product]:
            offer = price_table[product]["offer"]
            offer_quantity = offer["quantity"]
            if product == "E" and offer["free_item"] in item_counts:
                free_item_count = item_counts[offer["free_item"]]
                offer_applicable_count = min(count // offer_quantity, free_item_count)
                total_price += offer_applicable_count * price_table[product]["price"]
                item_counts[offer['free_item']] -= offer_applicable_count

    for item, count in item_counts.items():
        total_price += count * price_table[item]["price"]
    return total_price

