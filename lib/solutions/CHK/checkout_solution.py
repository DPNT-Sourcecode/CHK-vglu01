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
            special_offers = sorted(price_table[item]['special_offer'], reverse=True)

            for offer in special_offers:
                offer_qty, offer_value = offer

                if not isinstance(offer_value, str):
                    while count >= offer_qty:
                        print("here")
                        print(count, offer_qty)
                        total_price += offer_value
                        count -= offer_qty

                        print(item_counts, offer_value)

                if offer_value in item_counts and count >= offer_qty:

                    count_offer = count
                    while count_offer >= offer_qty:
                        print("back here")
                        if item != offer_value:

                            item_counts[offer_value] -= 1

                            if item_counts[offer_value] > 0: #check if there is any items left after offers
                                print("here 1")
                                print(item_counts, offer_value)

                                if item_counts[offer_value] >= price_table[offer_value]["special_offer"][0][0]: #if no offers on the offer value then takeaway the price
                                    print("here 2")
                                    total_price -= price_table[offer_value]["price"]
                                    print(total_price)
                                else:
                                    print("here 3")
                                    print(item_counts[offer_value], price_table[offer_value]["special_offer"][0][0])

                                    # total_price += price_table[offer_value]["price"]

                                    # total_price -= price_table[offer_value]["special_offer"][0][1]
                                    print(total_price)
                            else:
                                print("here 4")
                                print(item_counts, offer_value)

                                total_price -= price_table[offer_value]["price"]
                                print(total_price)
                        #
                        elif item == offer_value and count_offer > offer_qty:
                            print("here 5")
                            item_counts[offer_value] -= 1
                            total_price -= price_table[offer_value]["price"]


                        count_offer -= offer_qty

        print("here 6")
        print(item, count, price_table[item]['price'], total_price)
        total_price += count * price_table[item]['price']

    return total_price

