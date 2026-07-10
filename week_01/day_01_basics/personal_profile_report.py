# Mini Project 01: Personal Profile Report

# Original Profile Information
name = " Bhavana Chintala "
city = "Bengaluru"
goal = "Understanding and learning python basics in 7 days/1 week"
email = "BHAVANA@GMAIL.COM"

# Cleaned profile information
clean_name = name.strip().title()
clean_city = city.strip().title()
clean_goal = goal.strip().title()
clean_email = email.lower()

# Display final profile report
print("Personal Profile Report")
print("------------------------")
print(f"Name: {clean_name}")
print(f"City: {clean_city}")
print(f"Goal: {clean_goal}")
print(f"Email: {clean_email}")


