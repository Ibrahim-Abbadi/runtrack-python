import matplotlib.pyplot as plt
from collections import defaultdict

# Step 1: Read the "data.txt" file
with open("data.txt", "r") as file:
    text = file.read()

# Step 2: Tokenize the text into words
words = text.split()

# Step 3 and 4: Count the occurrences and calculate percentages
letter_counts = defaultdict(lambda: defaultdict(int))

for word in words:
    word = word.lower()  # Convert the word to lowercase
    for i in range(len(word) - 1):
        current_letter = word[i]
        next_letter = word[i + 1]
        if current_letter.isalpha() and next_letter.isalpha():
            letter_counts[current_letter][next_letter] += 1

# Calculate percentages
letter_percentages = {}

for letter, next_letters in letter_counts.items():
    total = sum(next_letters.values())
    percentages = {next_letter: (count / total) * 100 for next_letter, count in next_letters.items()}
    letter_percentages[letter] = percentages

# Step 5: Generate a graph of superimposed curves using Matplotlib
plt.figure(figsize=(12, 8))

for letter, percentages in letter_percentages.items():
    next_letters = list(percentages.keys())
    percentage_values = list(percentages.values())
    plt.plot(next_letters, percentage_values, label=f"{letter.upper()}")

plt.xlabel("Next Letters")
plt.ylabel("Percentage (%)")
plt.title("Percentage of Next Letters Following Each Letter")
plt.legend()
plt.grid(True)
plt.show()

