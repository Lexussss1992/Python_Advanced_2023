from collections import deque


def shop_from_grocery_list(budget, *data):
    purchased_products = []
    grorecy_list = [product for product in data[0]]
    for product, price in data[1::]:
        if budget < price:
            break
        if product not in grorecy_list or product in purchased_products:
            continue
        if product not in purchased_products and product in grorecy_list:
            purchased_products.append(product)
            grorecy_list.remove(product)
            budget -= price

    return f"Shopping is successful. Remaining budget: {budget:.2f}." if len(grorecy_list) <= 0 else f"You did not buy all the products. Missing products: {', '.join(grorecy_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))