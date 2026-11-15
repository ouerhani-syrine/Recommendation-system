import numpy as np
# Users in our recommendation system
users = ["User1", "User2", "User3", "Target"]

# Items available on our platform
items = ["A", "B", "C", "D"]

# Interactions between users and items
interactions = [
    ("User1", "A"),
    ("User1", "B"),
    ("User1", "D"),

    ("User2", "A"),
    ("User2", "B"),
    ("User2", "C"),

    ("User3", "C"),
    ("User3", "D"),

    ("Target", "A"),
    ("Target", "B")
]
# Create a matrix filled with zeros
R = np.zeros((len(users), len(items)), dtype=int)
# Create dictionaries to identify each user's and item's position
user_to_id = {user: i for i, user in enumerate(users)}
item_to_id = {item: i for i, item in enumerate(items)}
# Fill the matrix using our interactions
for user, item in interactions:
    user_index = user_to_id[user]
    item_index = item_to_id[item]
    R[user_index, item_index] = 1
num_users = len(users)
num_items = len(items)
# Create the adjacency matrix
A = np.block([[np.zeros((num_users, num_users)), R],[R.T, np.zeros((num_items, num_items))]])



