import numpy as np

def propagate_layers(P, E0, num_layers):
    # Store the initial embeddings
    embeddings = [E0]
    # Start with the initial embeddings
    current_embeddings = E0
    # Perform propagation
    for layer in range(num_layers):
        current_embeddings = P @ current_embeddings
        # Store the embeddings of this layer
        embeddings.append(current_embeddings)
    return embeddings
