from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    published_year: int

def main():

    book1 = Book(title="The Beginning After The End: Retribution", author="TurtleMe", published_year=2023)
    book2 = Book(title="TThe Time I Got Reincarnated as a Slime, vol.15 ", author="Fuse", published_year=2021)

    print("Book 1:", book1)
    print("Book 2:", book2)

if __name__ == "__main__":
    main()
