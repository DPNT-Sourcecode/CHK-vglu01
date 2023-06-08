# import math
#
#
# # noinspection PyUnusedLocal
# # skus = unicode string
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
#         'K': {'price': 80, 'special_offer': [(2, 150)]},
#         'L': {'price': 90},
#         'M': {'price': 15},
#         'N': {'price': 40, 'special_offer': [(3, 'M')]},
#         'O': {'price': 10},
#         'P': {'price': 50, 'special_offer': [(5, 200)]},
#         'Q': {'price': 30, 'special_offer': [(3, 80)]},
#         'R': {'price': 50, 'special_offer': [(3, 'Q')]},
#         'S': {'price': 30},
#         'T': {'price': 20},
#         'U': {'price': 40, 'special_offer': [(3, 'U')]},
#         'V': {'price': 50, 'special_offer': [(2, 90), (3, 130)]},
#         'W': {'price': 20},
#         'X': {'price': 90},
#         'Y': {'price': 10},
#         'Z': {'price': 50}
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
#     for item, count in item_counts.items():
#         if 'special_offer' in price_table[item]:
#             special_offers = price_table[item]['special_offer']
#
#             for offer in special_offers:
#                 offer_qty, offer_value = offer
#
#                 if not isinstance(offer_value, str):
#                     while count >= offer_qty:
#                         total_price += offer_value
#                         count -= offer_qty
#
#                 if offer_value in item_counts and count >= offer_qty:
#
#                     count_offer = count
#                     while count_offer >= offer_qty:
#
#                         if item != offer_value:
#                             item_counts[offer_value] -= 1
#
#                             if item_counts[offer_value] > 0:
#                                 if item_counts[offer_value] >= price_table[offer_value]["special_offer"][0][0]:
#                                     total_price -= price_table[offer_value]["price"]
#                                 else:
#                                     total_price += price_table[offer_value]["price"]
#                                     total_price -= price_table[offer_value]["special_offer"][0][1]
#                             else:
#                                 total_price -= price_table[offer_value]["price"]
#                         elif item == offer_value and count_offer > offer_qty:
#                             total_price -= price_table[offer_value]["price"]
#
#                         count_offer -= offer_qty
#
#         total_price += count * price_table[item]['price']
#
#     return total_price


import math


# noinspection PyUnusedLocal
# skus = unicode string
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
        'K': {'price': 80, 'special_offer': [(2, 150)]},
        'L': {'price': 90},
        'M': {'price': 15},
        'N': {'price': 40, 'special_offer': [(3, 'M')]},
        'O': {'price': 10},
        'P': {'price': 50, 'special_offer': [(5, 200)]},
        'Q': {'price': 30, 'special_offer': [(3, 80)]},
        'R': {'price': 50, 'special_offer': [(3, 'Q')]},
        'S': {'price': 30},
        'T': {'price': 20},
        'U': {'price': 40, 'special_offer': [(3, 'U')]},
        'V': {'price': 50, 'special_offer': [(2, 90), (3, 130)]},
        'W': {'price': 20},
        'X': {'price': 90},
        'Y': {'price': 10},
        'Z': {'price': 50}

    }

    item_counts = {}
    total_price = 0
    skus = sorted(skus)
    for item in skus:
        if item in price_table:
            item_counts[item] = item_counts.get(item, 0) + 1
        else:
            return -1

    print(item_counts)
    for item, count in item_counts.items():
        if 'special_offer' in price_table[item]:
            special_offers = price_table[item]['special_offer']

            for offer in special_offers:
                offer_qty, offer_value = offer

                if not isinstance(offer_value, str):
                    while count >= offer_qty:
                        total_price += offer_value
                        count -= offer_qty

                if offer_value in item_counts and count >= offer_qty:

                    count_offer = count
                    while count_offer >= offer_qty:

                        if item != offer_value:
                        #     print(item, offer_value)
                        #     print(item_counts)
                            item_counts[offer_value] -= 1
                        #     print(item_counts)
                            if item_counts[offer_value] > 0:
                        #
                                if item_counts[offer_value] >= price_table[offer_value]["special_offer"][0][0]:
                                    print("not here 1")
                                    total_price -= price_table[offer_value]["price"]
                                else:
                                    print("coming here")
                                    print(total_price)
                                    total_price += price_table[offer_value]["price"]
                                    # print(total_price)
                        #             total_price -= price_table[offer_value]["special_offer"][0][1]
                                    print(total_price)
                            else:
                                print("not here 2")
                                total_price -= price_table[offer_value]["price"]
                                print(total_price)
                        #
                        elif item == offer_value and count_offer > offer_qty:
                        #     print("nor here 3")
                            total_price -= price_table[offer_value]["price"]

                        count_offer -= offer_qty

        print(total_price, item, count, price_table[item]['price'])
        total_price += count * price_table[item]['price']

    return total_price
