# --- 1. Basic If-Else Statements ---
accuracy = 0.88

if accuracy >= 0.90:
    print("Model performance: Excellent")
else:
    print("Model performance: Needs Improvement")

# --- 2. Multiple Conditions using Elif ---
# Classifying loss metrics
loss = 0.25

if loss > 0.80:
    status = "High Loss - High Risk of Underfitting"
elif loss > 0.30:
    status = "Moderate Loss - Model is Learning"
elif loss > 0.05:
    status = "Low Loss - Good Performance"
else:
    status = "Near Zero Loss - Check for Overfitting!"

print(f"Loss Status ({loss}): {status}")

# --- 3. Logical Operators in Conditionals ---
# Validating hyperparameters before model training
learning_rate = 0.01
batch_size = 64

if learning_rate > 0 and batch_size > 0:
    print("Hyperparameters are valid. Starting training...")
else:
    print("Invalid hyperparameters! Values must be positive.")

# Combining 'and', 'or', and 'not'
val_accuracy = 0.85
is_overfitted = False

if val_accuracy >= 0.80 and not is_overfitted:
    print("Deploying model to production...")
else:
    print("Model retained for further tuning.")

# --- 4. Inline / Ternary Conditional Operator ---
# Shortened syntax for simple assignments
score = 0.92
status = "Pass" if score >= 0.80 else "Fail"
print(f"Evaluation result: {status}")

# --- 5. Handling Missing Data (Common ML Task) ---
feature_value = None

if feature_value is None:
    print("Missing value detected. Imputing with median value...")
    feature_value = 0.0  # Imputation
print("Processed feature value:", feature_value)