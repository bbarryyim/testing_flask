from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


PERSON = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}


def search() -> list:
    return PERSON


def create(person):
    lname = person.get('lname', None)
    fname = person.get('fname', None)
    timestamp = get_timestamp()

    if lname not in PERSON and lname is not None:
        PERSON[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp()
        }
