# JioHotstar App Information System
# Taking inputs
app_id = int(input("Enter App ID: "))
app_name = input("Enter App Name: ")
subscription_fee = float(input("Enter Monthly Subscription Fee: "))
categories = input("Enter Categories (comma-separated): ").split(",")
downloads = int(input("Enter Number of Downloads: "))
active_users = int(input("Enter Number of Active Users: "))
discount_percent = float(input("Enter Discount Percentage: "))
features = set(input("Enter Features (comma-separated): ").split(","))
developer_info = {
    "name": input("Enter Developer Name: "),
    "contact": input("Enter Developer Contact Number: "),
    "location": input("Enter Developer Location: ")
}

# Output using comma separation
print("\n1. Using Comma Separation (sep=','):")
print("App ID, Name, Fee:", app_id, app_name, subscription_fee, sep=", ")

# Output using % formatting
print("\n2. Using Percentage Formatting (% operator):")
print("Discount Available: %.2f%%" % discount_percent)

# Output using f-strings
print("\n3. Using f-strings:")
print(f"App Name: {app_name}")
print(f"Subscription Fee: ₹{subscription_fee}")
print(f"Downloads: {downloads} users")
print(f"Active Users: {active_users}")
print(f"Features: {features}")

# Output using .format() method
print("\n4. Using .format() method:")
print("Developer Details: Name - {name}, Contact - {contact}, Location - {location}".format(**developer_info))