import re

def countWords(File):
    
    with open(File, 'r') as file:
            content = file.read()
            words = re.findall(r'\b\w+\b', content)
            nb_words = len(words)
            return nb_words
# 'data.txt' file :
if __name__ == "__main__":
    File = "data.txt"
    nb_words = countWords(File)
    print(f"Number of words in '{File}': {nb_words}")
