from src.dataset import users, items, interactions
from src.dataset import P, E0
from src.lightgcn import propagate_layers
print("Users:", users)
print("Items:", items)
print("\nInteractions:")
for user, item in interactions:
    print(user, "->", item)
print("\nTotal users:", len(users))
print("Total items:", len(items))
print("Total interactions:", len(interactions))
num_layers = 2
all_embeddings = propagate_layers(P, E0, num_layers)
