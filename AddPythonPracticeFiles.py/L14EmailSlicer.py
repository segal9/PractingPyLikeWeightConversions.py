# email slicer to add value to practice string indexing
email = input("Enter your email: ")

#i1234@gmail.com
#index = email.index("@")
username =  email[0:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")
