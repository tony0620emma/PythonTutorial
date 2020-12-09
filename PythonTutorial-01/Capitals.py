Capitals = {"Japan": "Tokyo", "Taiwan": "Taipei", "France": "Paris", "Canada": "Ottawa", "Cuba": "Havana", "Kenya": "Nairobi", "Italy": "Rome", "Austria": "Vienna", "Germany": "Berlin"}

for _ in range(len(Capitals)):
    min = 'Z'
    for country in Capitals:
        if country[0] < min:
            min = country[0]
            min_country = country

    print(f"Minimal country = {min_country}")
    del Capitals[min_country]