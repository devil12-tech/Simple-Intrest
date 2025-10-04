# Formula:
# Simple Interest (SI) = (P * R * T) / 100
# Compound Interest (CI) = P * ( (1 + R/100) ^ T ) - P

# Taking input from user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Calculate Compound Interest
compound_interest = principal * ((1 + rate/100) ** time) - principal

# Display results
print("\nResults:")
print("Simple Interest =", simple_interest)
print("Compound Interest =", compound_interest)
