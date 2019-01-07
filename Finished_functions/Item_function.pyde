user_choice = 0

items = ["food", "food", "food", "food", 15, 73, 420, 90]

def use_items(item_index):
    value = items[item_index + 4]
    items.pop(item_index + 4)
    items.pop(item_index)
    
    return value

print(use_items(user_choice))
    
