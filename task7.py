# ---------------------------------------------
# Word Count Program
# Author: [Your Name]
# Description:
# This program counts the number of words in a given text input by the user.
# ---------------------------------------------

text = input("Enter a sentence or paragraph: ")

# Split the text into words
words = text.split()

# Count the number of words
word_count = len(words)

print(f"\n🧾 Your text contains {word_count} words.")
