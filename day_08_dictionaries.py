# --- 1. Creating and Accessing Dictionaries ---
# Representing hyperparameter configuration for an ML model
model_config = {
    "model_name": "RandomForestClassifier",
    "n_estimators": 100,
    "max_depth": 10,
    "random_state": 42
}

print("Model Name:", model_config["model_name"])

# Safely access keys using .get() (avoids KeyError if key doesn't exist)
learning_rate = model_config.get("learning_rate", 0.01)  # Default value 0.01 if key missing
print("Learning Rate:", learning_rate)

# --- 2. Modifying and Adding Key-Value Pairs ---
model_config["max_depth"] = 15        # Update existing key
model_config["learning_rate"] = 0.001 # Add new key

print("Updated Config:", model_config)

# --- 3. Dictionary Methods & Iteration ---
# Extracting Keys, Values, and Items
print("Keys:", list(model_config.keys()))
print("Values:", list(model_config.values()))

# Iterating over key-value pairs (common pattern for logging metrics)
print("\n--- Model Configuration Summary ---")
for key, value in model_config.items():
    print(f"{key}: {value}")

# --- 4. Nested Dictionaries (Used for Storing Complex ML Experiment Results) ---
experiment_results = {
    "model_1": {"accuracy": 0.88, "precision": 0.86, "recall": 0.90},
    "model_2": {"accuracy": 0.93, "precision": 0.91, "recall": 0.94}
}

print("\nModel 2 Precision:", experiment_results["model_2"]["precision"])

# --- 5. Removing Keys ---
removed_value = model_config.pop("random_state")
print("Removed random_state:", removed_value)