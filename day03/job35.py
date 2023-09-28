import matplotlib.pyplot as plt

def countLetter_occurrences(File):
    try:
        with open(File, 'r') as file:
            text = file.read()
            # Convert text to lowercase 
            text = text.lower()
            letter_count = {}

            for char in text:
                if char.isalpha():  # Check if the character is a letter
                    if char in letter_count:
                        letter_count[char] += 1
                    else:
                        letter_count[char] = 1

            total_letters = sum(letter_count.values())
            print(total_letters)
            letter_percentages = {k: v / total_letters * 100 for k, v in letter_count.items()}
            return letter_percentages
    except FileNotFoundError:
        print(f"The file '{File}' does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Main program
if __name__ == "__main__":
    File = "data.txt"
    letter_percentages = countLetter_occurrences(File)

    if letter_percentages:
        # Create the histogram 
        letters = list(letter_percentages.keys())
        percentages = list(letter_percentages.values())

        plt.figure(figsize=(12, 6))
        plt.bar(letters, percentages)
        plt.xlabel('Letters')
        plt.ylabel('Percentage (%)')
        plt.title('Percentage of Appearance of Each Letter')
        plt.show()
    else:
        print("No data to display or an error occurred.")
