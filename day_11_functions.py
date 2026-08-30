# --- 1. Basic Function Definition and Return ---
def calculate_accuracy(correct_predictions, total_samples):
    """Calculates accuracy percentage from predictions."""
    if total_samples == 0:
        return 0.0
    return (correct_predictions / total_samples) * 100

acc = calculate_accuracy(85, 100)
print(f"Accuracy: {acc:.2f}%")


# --- 2. Default Parameters and Named Arguments ---
# Setting default hyperparameters
def train_model(model_name, learning_rate=0.01, epochs=10):
    """Simulates training a model with configurable hyperparameters."""
    print(f"Training {model_name} with lr={learning_rate} for {epochs} epochs...")
    return f"{model_name}_trained"

# Calling with positional and default arguments
train_model("LogisticRegression")
# Overriding defaults using named keyword arguments
train_model("XGBoost", epochs=50, learning_rate=0.001)


# --- 3. Returning Multiple Values (As Tuples) ---
def evaluate_predictions(y_true, y_pred):
    """Calculates True Positives, False Positives, False Negatives, True Negatives."""
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    return tp, fp, fn, tn

# Unpacking returned metrics
true_y = [1, 0, 1, 1, 0]
pred_y = [1, 0, 0, 1, 0]
tp, fp, fn, tn = evaluate_predictions(true_y, pred_y)
print(f"Metrics -> TP: {tp}, FP: {fp}, FN: {fn}, TN: {tn}")


# --- 4. Flexible Arguments: *args and **kwargs ---
# *args: Accepts any number of positional arguments as a tuple
def compute_mean(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0.0

print("Mean score:", compute_mean(0.85, 0.90, 0.78, 0.92))

# **kwargs: Accepts any number of keyword arguments as a dictionary
def log_experiment_details(model_type, **hyperparameters):
    print(f"\nModel: {model_type}")
    for param, value in hyperparameters.items():
        print(f" - {param}: {value}")

log_experiment_details("Neural Network", layers=4, activation="relu", dropout=0.2)


# --- 5. Lambda Functions (Anonymous / One-Line Functions) ---
# Used frequently in data manipulation (e.g., applying transformations)
normalize = lambda x, min_val, max_val: (x - min_val) / (max_val - min_val)

sample_val = 75
scaled_val = normalize(sample_val, min_val=0, max_val=100)
print(f"\nOriginal: {sample_val} | Normalized: {scaled_val}")