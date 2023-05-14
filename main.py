# Open and read the dictionary file.
file = open("dictionary.txt", "r")

# Create an empty list to store the words.
dictionary = []

# Iterate over each line in the file.
for line in file:
  # Remove any leading or tailing whitespace.
  word = line.strip()

  # Converting the words to lowercase.
  lowercase_word = word.lower()

  # Add the word to the dictionary list.
  dictionary.append(lowercase_word)

# Close the file.
file.close()

# Prompt the user to enter a piece of text.
text = input("Enter some text: ")

# Tokenize the text (Split the input text into individual words).
tokens = text.split()

# Remove the punctuation marks or any special characters.
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~`+'''

clean_tokens = []

for token in tokens:
  # Remove any punctuation marks in the token.
  cleaned_token = ""

  for char in token:
    if char not in punctuation:
      cleaned_token += char
    
  # Add the clean token to the list.
  clean_tokens.append(cleaned_token)

# Check each token in the clean_tokens list.
misspelled_words = []

for token in clean_tokens:
  # Convert the token to lowercase for case-insensitive comparison
  lowercase_token = token.lower()

  # Check if the token is in the dictionary.
  if lowercase_token not in dictionary:
    # If not found, considering it as a potentially mispelled word.
    misspelled_words.append(token)

# Output all potentially misspelled words.
if not(len(misspelled_words)):
  print("No misspelled words found!")
else:
  print("Potentially misspelled words:", misspelled_words)