import re

file ="raw_data/paragraph_2.txt"
text_analysis = "analysis/output_analysis_1.txt"


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
avg_letter_count = round(sum(letter_count) / float(len(letter_count)),2)

sentences = re.split('[.|?|!]', passage)
print(sentences)

no_sentences = len(sentences)

words_in_sentence = []

for sentence in sentences:
    words_in_sentence.append(len(sentence.split(" ")))    

#Average words per sentence

avg_sentence = sum(words_in_sentence)/float(len(words_in_sentence))

#Paragraph Analysis

text = (
    f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {word_count}\n"
    f"Approximate Sentence Count: {no_sentences}\n"
    f"Average Letter Count: {avg_letter_count}\n"
    f"Average Sentence Length: {avg_sentence}\n"
)

# Print to terminal
print(text)

# Save the results to analysis text file
with open(text_analysis, "a") as txt_file:
    txt_file.write(text)
