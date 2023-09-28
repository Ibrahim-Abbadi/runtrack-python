import matplotlib.pyplot as plt

with open("data.txt", "r") as file:
    text = file.read()
    words = text.split()

# Count the occurrences
letter_counts = {}
total_words = len(words)

for word in words:
    if word:
        first_char = word[0].lower()  # Convert the first character to lowercase
        if first_char.isalpha():  # Only consider alphabetic characters
            if first_char not in letter_counts:
                letter_counts[first_char] = 0
            letter_counts[first_char] += 1

# Calculate percentages
letter_percentages = {letter: (count / total_words) * 100 for letter, count in letter_counts.items()}

# Generate a histogram 
letters = list(letter_percentages.keys())
percentages = list(letter_percentages.values())

plt.figure(figsize=(10, 6))
plt.bar(letters, percentages)
plt.xlabel("Letters")
plt.ylabel("Percentage")
plt.title("Percentage of Letters at the Beginning of Words")
plt.show()
