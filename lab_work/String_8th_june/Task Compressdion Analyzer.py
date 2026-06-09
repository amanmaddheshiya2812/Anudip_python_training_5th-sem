'''Tasks 
Write a program to: 
1. Count occurrences of each character.  
2. Create a dictionary of character frequencies.  
3. Display unique characters.  
4. Find the most frequent character.  
5. Create a compressed output:  
A3B3C3D3A3 
6. Calculate compression ratio. '''

text = "AAABBBCCCDDDAAA"

# 1. Validation
if not text or not text.isalpha():
    print("Invalid input: Please provide a non-empty string of alphabetic characters.")
else:
    # 2. Count occurrences and create frequency dictionary
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    # 3. Unique characters
    unique_chars = sorted(list(freq_dict.keys()))

    # 4. Find the most frequent character
    most_frequent = unique_chars[0]
    for char in freq_dict:
        if freq_dict[char] > freq_dict[most_frequent]:
            most_frequent = char

    # 5. Create compressed output (Run-Length Encoding style)
    compressed_text = ""
    if text:
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                compressed_text += text[i - 1] + str(count)
                count = 1
        compressed_text += text[-1] + str(count)

    # 6. Calculate compression ratio
    original_len = len(text)
    compressed_len = len(compressed_text)
    ratio = (compressed_len / original_len) * 100

    # Output Results
    print(f"Original Text: {text}")
    print("\nCharacter Frequencies:")
    for char, count in freq_dict.items():
        print(f"{char} -> {count}")

    print(f"\nUnique Characters: {unique_chars}")
    print(f"Most Frequent Character: {most_frequent}")
    print(f"\nCompressed Output: {compressed_text}")
    print(f"Original Length: {original_len}")
    print(f"Compressed Length: {compressed_len}")
    print(f"Compression Ratio: {ratio:.2f}%")