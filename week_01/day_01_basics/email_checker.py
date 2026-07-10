# Mini Project 4: Email Checker

email = "BHAVANA@GMAIL.COM"
# Cleaning the email
clean_email = email.strip().lower()
# Checking if the email contains "@gmail.com" and ends with ".com"
contains_gmail = "@gmail.com" in clean_email
ends_with_com = clean_email.endswith(".com")

# Display the final email report
print("Email Checker")
print("-----------------")
print(f"Original Email: {email}")
print(f"Cleaned Email: {clean_email}")
print(f"Contains '@gmail.com': {contains_gmail}")
print(f"Ends with '.com': {ends_with_com}")

