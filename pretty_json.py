import requests

again = "Y"

while again.upper() == "Y":

    print("Welcome to the Book of Mormon Summary Tool!")

    book = input("Which book of the Book of Mormon would you like? ")
    chapter = input(f"Which chapter of {book} are you interested in? ")

    base_url = "https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/"
    url = base_url + book.lower().replace(" ", "") + "/" + chapter

    response = requests.get(url)
    data = response.json()

    summary = data["chapter"]["summary"]

    print(f"\nSummary of {book} chapter {chapter}:")
    print(summary)

    again = input("\nWould you like to view another (Y/N)? ")

print("Thank you for using Book of Mormon Summary Tool!")

