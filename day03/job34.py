import re

def countWords(File, size):
    
    with open(File, 'r') as file:
            content = file.read()
            words = re.findall(r'\b\w+\b', content)

            count = sum(1 for word in words if len(word) == size)
            return count

if __name__ == "__main__":
    File = "data.txt"
    
    while True:
        try:
            size = int(input("Enter a positive whole number : "))
            nb_word = countWords(File, size)
            print(f"Number of words of size {size} in '{File}': {nb_word}")
            break  
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")
