"""Get person data"""

DATA = {
    111: {
        "name": "Dan",
        "age": 20,
    },
    112: {
        "name": "Maria",
        "age": 33,
    },
}



def get_name_and_age(person_id):
    """Returns person name and age"""

    return DATA[person_id]

if __name__ == "__main__":
    try:
        person = get_name_and_age(111)
        print(person)
    except KeyError:
        print("Not a good user ID")