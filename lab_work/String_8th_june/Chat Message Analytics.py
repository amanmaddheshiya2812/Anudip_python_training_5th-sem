'''Tasks 
Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants.  '''

message = "Python is awesome and Python is easy to learn"

# 1. Count total characters
total_chars = len(message)

# 2. Count total words
words = message.split()
total_words = len(words)

# 3. Find the longest word
longest_word = max(words, key=len)

# 4. Find the shortest word
shortest_word = min(words, key=len)

# 5. Count occurrences of "Python"
python_count = words.count("Python")

# 6. List of words > 4 characters
long_words = [w for w in words if len(w) > 4]

# 7. Display words starting with a vowel
vowels_str = "aeiouAEIOU"
vowel_starts = [w for w in words if w[0] in vowels_str]

# 8. Count vowels and consonants
vowels_count = 0
consonants_count = 0
for char in message:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels_count += 1
        else:
            consonants_count += 1

# Output Results
print(f"Message: {message}")
print(f"Total Characters: {total_chars}")
print(f"Total Words: {total_words}")
print(f"Longest Word: {longest_word}")
print(f"Shortest Word: {shortest_word}")
print(f"Occurrences of Python: {python_count}")
print(f"Words Longer Than 4 Characters: {long_words}")
print(f"Words Starting With Vowel: {vowel_starts}")
print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")