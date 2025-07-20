text = "Hello, Python Programming!"

first_char = text[0]  
last_char = text[-1]  
print(f"First Character: {first_char}")
print(f"Last Character: {last_char}")

substring = text[7:13]
reversed_text = text[::-1]
print(f"Substring (7:13): {substring}")
print(f"Reversed Text: {reversed_text}")

upper_text = text.upper()  
lower_text = text.lower()  
replaced_text = text.replace("Python", "Java")  
split_text = text.split()  
joined_text = " ".join(split_text)

print(f"Uppercase: {upper_text}")
print(f"Lowercase: {lower_text}")
print(f"Replaced Text: {replaced_text}")
print(f"Split Text: {split_text}")
print(f"Joined Text: {joined_text}")

is_alpha = text.isalpha()
starts_with_hello = text.startswith("Hello")
ends_with_exclamation = text.endswith("!")

print(f"Is Alphabetic: {is_alpha}")
print(f"Starts with 'Hello': {starts_with_hello}")
print(f"Ends with '!': {ends_with_exclamation}")
