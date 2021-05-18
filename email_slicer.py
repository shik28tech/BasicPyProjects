email = input("Enter Your Email Address: ").strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print(f"Username is {user_name} and Domain name is {domain_name}")