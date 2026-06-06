books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]
# Display unavailable books (count is 0)
print("Unavailable Books:")
for title, count in books:
    if count == 0:
        print(f"- {title}")

# Find all books with more than 2 copies
print("\nBooks with more than 2 copies:")
for title, count in books:
    if count > 2:
        print(f"- {title} ({count} copies)")

# Count available books (count > 0)
available_count = sum(1 for title, count in books if count > 0)
print(f"\nTotal number of available book titles: {available_count}")

# Stop searching once a requested book is found
requested_book = "Java Programming"
print(f"\nSearching for '{requested_book}':")
for title, count in books:
    print(f"Checking: {title}...")
    if title == requested_book:
        print(f"Found! Status: {'Available' if count > 0 else 'Unavailable'}")
        break