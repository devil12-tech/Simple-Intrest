# Simple Interest Formula: SI = (P * R * T) / 100

# Taking input from user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Display result
print("Simple Interest =", simple_interest)
