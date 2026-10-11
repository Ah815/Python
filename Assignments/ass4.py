
inventory = [
    ["P101", "Keyboard", 0, 10],
    ["P102", "Mouse", 5, 10],
    ["P103", "Monitor", 25, 10],
    ["P104", "USB Cable", 3, 5],
    ["P105", "Headphones", 15, 10]
]
restock_list = []
out_of_stock = 0
low_stock = 0
adequate_stock = 0
print("===== INVENTORY STOCK REPORT =====\n")
for item in inventory:
    sku = item[0]
    name = item[1]
    quantity = item[2]
    threshold = item[3]
    if quantity == 0:
        status = "OUT OF STOCK"
        action = "Emergency reorder required"
        out_of_stock += 1
        restock_list.append(item)
    elif quantity <= threshold:
        status = "LOW STOCK"
        action = "Add to purchase list"
        low_stock += 1
        restock_list.append(item)
    else:
        status = "ADEQUATE"
        action = "No action required"
        adequate_stock += 1
    print("SKU:", sku)
    print("Product:", name)
    print("Current Quantity:", quantity)
    print("Reorder Threshold:", threshold)
    print("Status:", status)
    print("Action:", action)
    print("-" * 35)
print("\n===== RESTOCK ACTION LIST =====")
if len(restock_list) == 0:
    print("No products require restocking.")
else:
    for item in restock_list:
        print(item[0], "-", item[1],
              "| Current Stock:", item[2],
              "| Threshold:", item[3])
print("\n===== OPERATIONAL SUMMARY =====")
print("Total Products:", len(inventory))
print("Out of Stock:", out_of_stock)
print("Low Stock:", low_stock)
print("Adequate Stock:", adequate_stock)
print("Products Requiring Restock:", len(restock_list))
