"""
Analysis of alcohol consuming database in CSV by country
"""
import research


def main():
    """
    Starts the application
    """

    top_countries = {
        "beer": research.top_beer(research.read_csv()),
        "spirit": research.top_spirit(research.read_csv()),
        "wine": research.top_wine(research.read_csv()),
        "alcohol": research.top_alcohol(research.read_csv()),
    }
    for count, (key, country_list) in enumerate(top_countries.items(), start=1):
        print("\n##################\n")
        print(f"Top 5 Countries which drink {key} the most:\n")
        for index, row in enumerate(country_list[:30]):
            print(f"{index+1} | {row.country} | {row[count]}")


if __name__ == "__main__":
    main()
