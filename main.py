from src.dataset import users, items, interactions

print("Users:", users)
print("Items:", items)

print("\nInteractions:")
for user, item in interactions:
    print(user, "->", item)

print("\nTotal users:", len(users))
print("Total items:", len(items))
print("Total interactions:", len(interactions))
