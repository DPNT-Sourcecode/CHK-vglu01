import math


# noinspection PyUnusedLocal
# skus = unicode string
# def checkout(skus):
#
#
#     price_table = {
#         'A': {'price': 50, 'special_offer': [(5, 200), (3, 130)]},
#         'B': {'price': 30, 'special_offer': [(2, 45)]},
#         'C': {'price': 20},
#         'D': {'price': 15},
#         'E': {'price': 40, 'special_offer': [(2, 'B')]},
#         'F': {'price': 10, 'special_offer': [(2, 'F')]},
#         'G': {'price': 20},
#         'H': {'price': 10, 'special_offer': [(5, 45), (10, 80)]},
#         'I': {'price': 35},
#         'J': {'price': 60},
#         'K': {'price': 70, 'special_offer': [(2, 120)]},
#         'L': {'price': 90},
#         'M': {'price': 15},
#         'N': {'price': 40, 'special_offer': [(3, 'M')]},
#         'O': {'price': 10},
#         'P': {'price': 50, 'special_offer': [(5, 200)]},
#         'Q': {'price': 30, 'special_offer': [(3, 80)]},
#         'R': {'price': 50, 'special_offer': [(3, 'Q')]},
#         'S': {'price': 20, 'special_offer_any_three': [(3, 45)]},
#         'T': {'price': 20, 'special_offer_any_three': [(3, 45)]},
#         'U': {'price': 40, 'special_offer': [(3, 'U')]},
#         'V': {'price': 50, 'special_offer': [(2, 90), (3, 130)]},
#         'W': {'price': 20},
#         'X': {'price': 70, 'special_offer_any_three': [(3, 45)]},
#         'Y': {'price': 20, 'special_offer_any_three': [(3, 45)]},
#         'Z': {'price': 20, 'special_offer_any_three': [(3, 45)]}
#
#     }
#
#     item_counts = {}
#     total_price = 0
#     skus = sorted(skus)
#     for item in skus:
#         if item in price_table:
#             item_counts[item] = item_counts.get(item, 0) + 1
#         else:
#             return -1
#
#     item_counts_copy = item_counts.copy()
#
#     for item, count in item_counts.items():
#         if 'special_offer' in price_table[item]:
#             special_offers = sorted(price_table[item]['special_offer'], reverse=True)
#
#             for offer in special_offers:
#
#                 offer_qty, offer_value = offer
#
#                 if not isinstance(offer_value, str):
#
#                     while count >= offer_qty:
#                         total_price += offer_value
#                         count -= offer_qty
#
#                 if offer_value in item_counts and count >= offer_qty:
#
#                     count_offer = count
#
#                     while count_offer >= offer_qty:
#
#                         if item != offer_value:
#                             item_counts[offer_value] -= 1
#
#                         elif item == offer_value and count_offer > offer_qty:
#                             item_counts[offer_value] -= 1
#                             total_price -= price_table[offer_value]["price"]
#
#                         count_offer -= offer_qty
#
#                     if item_counts[offer_value] == 0:
#
#                         if "special_offer" in price_table[offer_value]:
#                             total_price = 0
#                         else:
#                             total_price -= item_counts_copy[offer_value] * price_table[offer_value]["price"]
#
#                     elif item_counts[offer_value] >= price_table[offer_value]["special_offer"][0][0] and item != offer_value:
#                         total_price -= price_table[offer_value]["price"]
#
#                     elif item_counts[offer_value] < price_table[offer_value]["special_offer"][0][0]:
#                         total_price += item_counts[offer_value] * price_table[offer_value]["price"]
#                         total_price -= price_table[offer_value]["special_offer"][0][1]
#
#         total_price += count * price_table[item]['price']
#
#     return total_price


def checkout(skus):


    price_table = {
        'A': {'price': 50, 'special_offer': [(5, 200), (3, 130)]},
        'B': {'price': 30, 'special_offer': [(2, 45)]},
        'C': {'price': 20},
        'D': {'price': 15},
        'E': {'price': 40, 'special_offer': [(2, 'B')]},
        'F': {'price': 10, 'special_offer': [(2, 'F')]},
        'G': {'price': 20},
        'H': {'price': 10, 'special_offer': [(5, 45), (10, 80)]},
        'I': {'price': 35},
        'J': {'price': 60},
        'K': {'price': 70, 'special_offer': [(2, 120)]},
        'L': {'price': 90},
        'M': {'price': 15},
        'N': {'price': 40, 'special_offer': [(3, 'M')]},
        'O': {'price': 10},
        'P': {'price': 50, 'special_offer': [(5, 200)]},
        'Q': {'price': 30, 'special_offer': [(3, 80)]},
        'R': {'price': 50, 'special_offer': [(3, 'Q')]},
        # 'S': {'price': 20, 'special_offer_any_three': [(3, 45)]},
        # 'T': {'price': 20, 'special_offer_any_three': [(3, 45)]},
        'S': {'price': 20, 'special_offer': [(3, 45)]},
        'T': {'price': 20, 'special_offer': [(3, 45)]},
        'U': {'price': 40, 'special_offer': [(3, 'U')]},
        'V': {'price': 50, 'special_offer': [(2, 90), (3, 130)]},
        'W': {'price': 20},
        # 'X': {'price': 70, 'special_offer_any_three': [(3, 45)]},
        # 'Y': {'price': 20, 'special_offer_any_three': [(3, 45)]},
        # 'Z': {'price': 20, 'special_offer_any_three': [(3, 45)]}
        'X': {'price': 70, 'special_offer': [(3, 45)]},
        'Y': {'price': 20, 'special_offer': [(3, 45)]},
        'Z': {'price': 20, 'special_offer': [(3, 45)]}

    }

    item_counts = {}
    total_price = 0
    skus = sorted(skus)
    for item in skus:
        if item in price_table:
            item_counts[item] = item_counts.get(item, 0) + 1
        else:
            return -1

    copy_item_counts = item_counts.copy()

    print(item_counts)

    for item, count in item_counts.items():
        if 'special_offer' in price_table[item]:
            special_offers = sorted(price_table[item]['special_offer'], reverse=True)

            for offer in special_offers:
                offer_qty, offer_value = offer
                print("here")
                print(item, count, offer_qty, offer_value)
                if not isinstance(offer_value, str):
                    print("price offer")
                    while count >= offer_qty:
                        print("here1")
                        print(count, offer_qty)
                        total_price += offer_value
                        count -= offer_qty

                        print(item_counts, offer_value)

                if offer_value in item_counts and count >= offer_qty:

                    count_offer = count
                    while count_offer >= offer_qty:
                        print("free item offer")
                        print("item:", item, "count_offer:", count_offer, "offer_quantity:", offer_qty)
                        if item != offer_value:
                            print("item != offer_value")
                            item_counts[offer_value] -= 1

                        elif item == offer_value and count_offer > offer_qty:
                            print("here 4")
                            item_counts[offer_value] -= 1
                            total_price -= price_table[offer_value]["price"]

                        count_offer -= offer_qty

                    if item_counts[offer_value] == 0:
                        print("here 5")
                        print(item_counts, offer_value)
                        print(total_price)

                        if "special_offer" in price_table[offer_value]:
                            print("lalalala")
                            print(offer_value)
                            # total_price -= price_table[offer_value]["special_offer"][0][1]
                            total_price = 0
                        else:
                            print("doesn't have special offer")
                            total_price -= copy_item_counts[offer_value] * price_table[offer_value]["price"]
                            print(copy_item_counts, total_price)

                    elif item_counts[offer_value] >= price_table[offer_value]["special_offer"][0][
                        0] and item != offer_value:
                        print("here 6")
                        total_price -= price_table[offer_value]["price"]
                    elif item_counts[offer_value] < price_table[offer_value]["special_offer"][0][0]:
                        print("here 7")
                        print(total_price)
                        print(item_counts, item_counts[offer_value], offer_value)
                        total_price += item_counts[offer_value] * price_table[offer_value]["price"]
                        total_price -= price_table[offer_value]["special_offer"][0][1]
                        print(total_price)
        # elif "special_offer_any_three" in price_table[item]:
        #     print()
            # item_counts[offer_value] -= 1



        print("here 8")
        print(item, count, price_table[item]['price'], total_price)
        total_price += count * price_table[item]['price']
        print("total_price", total_price)

    return total_price


