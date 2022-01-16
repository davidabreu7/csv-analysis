"""
Analysis of alcohol consuming database in CSV by country
"""
import research


def main():
    """
    Starts the application
    """

    countries_top_beer = research.top_beer(research.read_csv())
    countries_top_spirit = research.top_spirit(research.read_csv())
    countries_top_wine = research.top_wine(research.read_csv())
    countries_top_alcohol = research.top_alcohol(research.read_csv())

    top_countries = {
        "beer": countries_top_beer,
        "spirit": countries_top_spirit,
        "wine": countries_top_wine,
        "alcohol": countries_top_alcohol,
    }

    for key, country_list in top_countries.items():
        print(f"Top 5 Countries which drink {key} the most:\n")
        for index, row in enumerate(country_list[:10]):
            print(f"{index+1} | {row.country}")


if __name__ == "__main__":
    main()
