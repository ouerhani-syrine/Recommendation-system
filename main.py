from src.dataset import users, items, interactions
from src.dataset import P, E0
from src.lightgcn import propagate_one_layer
print("Users:", users)
print("Items:", items)
print("\nInteractions:")
for user, item in interactions:
    print(user, "->", item)
print("\nTotal users:", len(users))
print("Total items:", len(items))
print("Total interactions:", len(interactions))
E1 = propagate_one_layer(P, E0)
