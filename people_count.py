def get_people_count(names):
    
    unique_names = []

    for name in names:
        if name not in unique_names:
            unique_names = unique_names + [name]

    return len(unique_names)

names = ["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]

print(get_people_count(names))
