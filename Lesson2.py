# Task 1

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def format_flight_itineraries(itineraries):
    for i, itinerary in enumerate(itineraries, start=1):
        print(f"Itinerary {i}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}")

format_flight_itineraries(itineraries)
print()


# Task 2
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, new_book):
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"The book '{new_book[0]}' by {new_book[1]} has been added to the library.")

new_books = [("1984", "George Orwell"), ("Dune", "Frank Herbert")]

for book in new_books:
    add_book(library, book)

print("\nUpdated Library:")
for book in library:
    print(book)

print(library)
