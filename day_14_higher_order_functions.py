from functools import reduce

# --- 1. map(): Apply a Function to All Items ---
# Syntax: map(function, iterable)
# Scale feature values by multiplying by 100
raw_features = [0.12, 0.45, 0.78, 0.91]

# Using map with lambda
scaled_features = list(map(lambda x: x * 100, raw_features))
print("Scaled Features (map):", scaled_features)


# --- 2. filter(): Filter Items Based on a Condition ---
# Syntax: filter(function, iterable)
# Keep only features above a variance threshold (e.g., > 0.5)
feature_variances = [0.12, 0.85, 0.04, 0.62, 0.91, 0.23]

high_variance_features = list(filter(lambda x: x > 0.5, feature_variances))
print("High Variance Features (filter):", high_variance_features)


# --- 3. reduce(): Aggregate Items Sequentially into a Single Value ---
# Syntax: reduce(function, iterable)
# Calculate total loss across a sequence of batch loss values
batch_losses = [0.45, 0.32, 0.18, 0.12, 0.08]

# Sums elements cumulatively: ((0.45 + 0.32) + 0.18)...
total_loss = reduce(lambda acc, val: acc + val, batch_losses)
print(f"Total Cumulative Loss (reduce): {total_loss:.2f}")


# --- 4. Returning Functions from Functions (Decorator Pattern Foundation) ---
# A function factory that returns custom scaling functions
def create_scaler(factor):
    """Returns a function that multiplies its input by 'factor'."""
    def scaler(value):
        return value * factor
    return scaler

double_scaler = create_scaler(2)
triple_scaler = create_scaler(3)

print("\nCustom Scaled (Double):", double_scaler(10))  # 20
print("Custom Scaled (Triple):", triple_scaler(10))  # 30