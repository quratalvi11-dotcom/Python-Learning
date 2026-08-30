# --- 1. For Loops (Iterating over Sequences) ---
# Iterating through dataset features
features = ["age", "income", "credit_score", "loan_status"]

print("--- Feature Extraction ---")
for feature in features:
    print(f"Processing feature: {feature}")

# Using range() for epoch loops (Start, Stop, Step)
print("\n--- Model Training Simulation ---")
epochs = 5
for epoch in range(1, epochs + 1):
    print(f"Epoch {epoch}/{epochs} - Loss: {1.0 / epoch:.4f}")

# --- 2. Enumerate (Index + Value Iteration) ---
# Crucial when you need both the position index and the data item
data_samples = [0.12, 0.45, 0.89, 0.23]

print("\n--- Sample Tracking ---")
for index, sample in enumerate(data_samples):
    print(f"Sample Index {index}: Value = {sample}")

# --- 3. Zip (Iterating Over Multiple Sequences Simultaneously) ---
predictions = [1, 0, 1, 1]
actual_labels = [1, 0, 0, 1]

print("\n--- Evaluating Model Predictions ---")
for pred, actual in zip(predictions, actual_labels):
    status = "Correct" if pred == actual else "Incorrect"
    print(f"Predicted: {pred} | Actual: {actual} -> {status}")

# --- 4. While Loops ---
# Used when the number of iterations depends on a dynamic condition (e.g., convergence)
current_loss = 0.8
target_loss = 0.2
epoch_count = 0

print("\n--- Training Until Convergence ---")
while current_loss > target_loss:
    epoch_count += 1
    current_loss -= 0.15  # Simulate gradient step reducing loss
    print(f"Epoch {epoch_count}: Loss reduced to {current_loss:.2f}")

# --- 5. Loop Control Statements (break, continue, else) ---
# Break: Stop early (e.g., Early Stopping to prevent overfitting)
# Continue: Skip current iteration (e.g., skip missing data)
val_losses = [0.45, 0.38, 0.35, 0.36, 0.40]  # Loss starts increasing at epoch 4

print("\n--- Early Stopping Check ---")
for index, loss in enumerate(val_losses):
    if index > 0 and loss > val_losses[index - 1]:
        print(f"Stopping early at step {index + 1}! Loss increased to {loss}")
        break
    print(f"Step {index + 1}: Loss = {loss}")