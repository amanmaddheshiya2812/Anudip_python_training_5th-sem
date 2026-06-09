'''Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words. '''

review = "This product is excellent excellent excellent and very useful"

# Prepare the words list
words = review.split()

# 1. Count total words
total_words = len(words)

# 2. Create a dictionary containing word frequencies
word_frequencies = {}
for word in words:
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

# 3. Find the most frequently used word
most_frequent_word = max(word_frequencies, key=word_frequencies.get)

# 4. Find all words appearing only once
words_appearing_once = [word for word, count in word_frequencies.items() if count == 1]

# 5. Count words having more than 5 characters
words_longer_than_5 = [word for word in words if len(word) > 5]
count_long_words = len(words_longer_than_5)

# 6. Display words in reverse order
reversed_words = words[::-1]

# 7. Create a list of unique words
unique_words = list(word_frequencies.keys())

# --- Displaying Output ---
print(f"Total Words: {total_words}")
print("\nWord Frequencies:")
for word, count in word_frequencies.items():
    print(f"{word} -> {count}")
print(f"\nMost Frequent Word: {most_frequent_word}")
print(f"\nWords Appearing Once:\n{words_appearing_once}")
print(f"\nWords with more than 5 characters: {count_long_words}")
print(f"Reversed Words: {reversed_words}")
print(f"\nUnique Words:\n{unique_words}")