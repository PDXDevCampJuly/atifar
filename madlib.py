# Prints a funny article put together using blind user input strings and predetermined strings.

def answer(prompt):
    inp = input(prompt)
    return inp

# Save the beginning of the article
article = "An Univision poll seeking "

# Get user to provide their input
nationality = answer("Provide a name of a nationality: ")

# Append the user input to the article
article += nationality

# Get more user input
politician = answer("Provide a politician's name: ")

# Continue appending to the article
article = article + " views on " + politician + "'s prickly comments about "

country = answer("Name a country: ")

article = article + country + ", and "

residents = answer("Provide the name of the residents of a country: ")

article = article + residents + " who cross the border illegally, found that "

percentage = answer("Pick a number between 0 and 100:")

article = article + percentage + " percent said they were offensive."

# Print the final articleJ
print("\n\n" + article + "\n\n")
