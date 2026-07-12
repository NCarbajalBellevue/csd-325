def city_country(city, country, population=None, language=None):

    result = f"{city}, {country}"

    if population:
        result += f" - population {population}"

    if language:
        result += f", {language}"

    return result


print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France", 2161000))
print(city_country("Tokyo", "Japan", 13960000, "Japanese"))