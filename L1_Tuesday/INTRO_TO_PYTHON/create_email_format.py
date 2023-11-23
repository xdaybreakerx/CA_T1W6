# John Smith -> dairyfarm
# work email is usually name + company
# eg, 
# john.smith@dairyfarm.com.au

# variable naming conventions
# first_name -> snake case -> standard for py
# firstName -> camel case -> standard for js 
# FirstName -> pascal case -> typically for classes
# first-name -> kebab case -> rarely used

first_name = input("Your First name: ").lower()
last_name = input("Your Last name: ").lower()
company_name = input("Your company name: ").lower()

predicted_email = first_name + "." + last_name + "@" + company_name + ".com.au"
predicted_email_using_fstring = f"{first_name}.{last_name}@{company_name}.com.au"

print(predicted_email)
print(predicted_email_using_fstring)