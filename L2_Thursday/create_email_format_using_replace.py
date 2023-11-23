full_name = input("Enter your full name: ")

company_name = input("Enter your company name: ")

required_full_name_format = full_name.replace(" ", ".")
required_company_name_format = company_name.replace(" ", "")

predicted_email = f"{required_full_name_format}@{required_company_name_format}.com.au".lower()

print(predicted_email)