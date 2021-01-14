import re

file ="raw_data/paragraph_1.txt"

passage = ''

with open(file) as text_passage:
    # Store the contents as a string (with no new lines)
    passage = text_passage.read().replace("\n", " ")

# Split the paragraph based on spaces to calculate word count
word_split = passage.split(" ")
print(word_split)
word_count = len(word_split)
print(word_count)

letter_count = []

# Loop through the word array and calculate the length of each word
for word in word_split:
    # Add each letter count into the letter_counts list
    letter_count.append(len(word))

# Calculate the avg letter count
avg_letter_count = sum(letter_count) / float(len(letter_count))

sentences = re.split('[.|?|!]', passage)
print(sentences)

