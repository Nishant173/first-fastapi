import random
import crud_ops

NAMES = ['Alex', 'Brian', 'Cody', 'Dylan', 'Eugene', 'Foebie', 'Graeme', 'Harry', 'Ingred', 'Jill',
         'Kenny', 'Larry', 'Maggie', 'Nate', 'Perry', 'Queen', 'Rashid', 'Tony']
SPORTS = ['Cricket', 'Football', 'Golf', 'Hockey', 'MMA', 'Rugby', 'Tennis']


if __name__ == "__main__":
    try:
        crud_ops.create_sports_table()
    except:
        pass

    for name in NAMES:
        age = random.randint(18, 60)
        fav_sport = random.choice(SPORTS)
        print(f"Added --> Name: {name} \t Age: {age} \t FavSport: {fav_sport}")
        crud_ops.add_sports_record(name=name, age=age, fav_sport=fav_sport)