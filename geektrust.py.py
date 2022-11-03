item_dict = {"tshirt": [1000, 10], "jacket":[2000, 5], "cap":[500, 20], "notebook": [200, 20], "pens": [300, 10], "markers": [500, 5]}

cloth = {"tshirt": [1000, 10], "jacket":[2000, 5], "cap":[500, 20]}
stationary = {"notebook": [200, 20], "pens": [300, 10], "markers": [500, 5]}

purchase_cloth_dict = {"tshirt":0, "jacket":0, "cap":0}
purchase_stat_dict = {"notebook":0, "pens":0, "markers":0}

while True:
    item = input("ADD_ITEM")
    if len(item) > 0:
        name, quantity = item.split(" ")
        quantity = int(quantity)
        if name in cloth:
            if purchase_cloth_dict[name] + quantity <= 2:
                purchase_cloth_dict[name] += quantity
                print("ITEM_ADDED")
            else:
                print("ERROR_QUANTITY_EXCEEDED")
        else:
            if purchase_stat_dict[name] + quantity <= 3:
                purchase_stat_dict[name] += quantity
                print("ITEM_ADDED")
            else:
                print("ERROR_QUANTITY_EXCEEDED")
    else:
        break

# Copute total cost
total_cost = 0
for _, k in enumerate(purchase_cloth_dict):
    if purchase_cloth_dict[k] > 0:
        total_cost += item_dict[k][0] * purchase_cloth_dict[k]
for _, k in enumerate(purchase_stat_dict):
    if purchase_stat_dict[k] > 0:
        total_cost += item_dict[k][0]  * purchase_stat_dict[k]

# print(total_cost)

# Total discount
total_discount = 0
if total_cost >= 1000:
    for _, k in enumerate(purchase_cloth_dict):
        if purchase_cloth_dict[k] > 0:
            # print(item_dict[k][0], item_dict[k][1])
            total_discount += (item_dict[k][0] * (item_dict[k][1]/100) * purchase_cloth_dict[k])
        # print(k, purchase_cloth_dict[k], total_discount)
    for _, k in enumerate(purchase_stat_dict):
        if purchase_stat_dict[k] > 0:
            total_discount += (item_dict[k][0] * (item_dict[k][1]/100) * purchase_stat_dict[k])
        # print(k, purchase_stat_dict[k])
print("TOTAL_DISCOUNT ", total_discount)

# Total discounted cost
total_discounted_cost = total_cost - total_discount

# Additional discounts
additional_discount = 0
if total_cost >= 3000:
    additional_discount = total_discounted_cost * 0.05
    total_discounted_cost = total_discounted_cost - additional_discount

# Add Tax
tax = total_discounted_cost * 0.1
taxed_amount = total_discounted_cost + tax

print("TOTAL_AMOUNT_TO_PAY ", taxed_amount)