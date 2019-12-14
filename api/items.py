from datetime import datetime
from flask import make_response, abort


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


def getAll() -> list:
    return PERSON


def getOne(lname):
    """
    This function responds to a request for /api/person/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name

    """
    if lname in PERSON:
        person = PERSON.get(lname)
        return person
    else:
        abort(
            400, "Person with last name {lname} not found".format(lname=lname)
        )


def create(person):
    """
    This function responds to a request for /api/person/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    lname = person.get('lname', None)
    fname = person.get('fname', None)
    timestamp = get_timestamp()

    if lname not in PERSON and lname is not None:
        PERSON[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp()
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 200
        )
    else:
        abort(
            400, "Person with last name {lname} already exists".format(lname=lname)
        )


def delete(lname):
    """
    This function responds to a request for /api/person/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    if lname in PERSON:
        del PERSON[lname]
        return make_response(
            "{lname} record successfully deleted".format(lname=lname), 200
        )
    else:
        abort(
            400, "Person with last name {lname}".format(lname=lname)
        )
