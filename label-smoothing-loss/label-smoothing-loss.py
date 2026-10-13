import math

def label_smoothing_loss(predictions: list, target: int, epsilon: float) -> float:
    """
    Returns cross-entropy loss for the smoothed target distribution.
    """
    n = len(predictions)
    loss = 0.0
    for i in range(n):
        if i == target:
            q_i = 1-epsilon + epsilon/n
            loss -= q_i * math.log(predictions[i])
            continue 
        q_i = epsilon/n
        loss -= q_i * math.log(predictions[i])

    return loss
            