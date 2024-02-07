from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    published_year: int

    def display_book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Published Year: {self.published_year}")

def main():

    book1 = Book(title="The Beginning After The End: Retribution", author="TurtleMe", published_year=2023)
    book2 = Book(title="TThe Time I Got Reincarnated as a Slime, vol.15 ", author="Fuse", published_year=2021)

    print("Book 1:")
    book1.display_book_info()

    print("\nBook 2:")
    book2.display_book_info()

if __name__ == "__main__":
    main()
