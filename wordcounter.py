from collections import Counter
import string

print("WORD COUNTER IS RUNNING")


try:
    with open("text.txt", "r") as file:
        text = file.read()
        text = text.lower()

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    ) 

    
    words = text.split()

    if not words:
        print("The file is empty.")

    else:
        word_count = Counter(words)

        print("\n--- WORD FREQUENCY ---")

        for word, count in word_count.items():
            print(word, ":", count)


except FileNotFoundError:
    print("Error: text.txt was not found.")