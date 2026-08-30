# ml_helpers.py - Custom helper module

def calculate_mean(values):
    """Calculates the average of a list of numbers."""
    return sum(values) / len(values) if values else 0.0

def min_max_scale(values):
    """Scales a list of numbers to a range between 0 and 1."""
    min_v = min(values)
    max_v = max(values)
    if min_v == max_v:
        return [0.0 for _ in values]
    return [(x - min_v) / (max_v - min_v) for x in values]

# Module constant
DEFAULT_RANDOM_SEED = 42