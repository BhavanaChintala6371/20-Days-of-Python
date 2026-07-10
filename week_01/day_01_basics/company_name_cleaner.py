# Mini Project 3: Company Name Cleaner

company = " abc technologies pvt ltd "
# Clean the company name by removing leading/trailing spaces and converting to title case
clean_company = company.strip().title()
print(clean_company)

first_character = clean_company[0]
last_character = clean_company[-1]
company_length = len(clean_company)

# Display the final company name report
print("Company Name Cleaner")
print("--------------------")
print(f"Original Company Name: {company} ")
print(f"Cleaned Company Name: {clean_company}")
print(f"First Character: {first_character}")
print(f"Last Character: {last_character}")
print(f"Length: {company_length}")

