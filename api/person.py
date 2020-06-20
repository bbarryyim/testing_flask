"""
This is the person module and supports all the ReST actions for the
PERSON collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
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


def read_all():
    """
    This function responds to a request for /api/person
    with the complete lists of person
    :return:        json string of list of person
    """
    # Create the list of person from our data
    return [PERSON[key] for key in sorted(PERSON.keys())]


def read_one(lname):
    """
    This function responds to a request for /api/person/{lname}
    with one matching person from person
    :param lname:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in person?
    if lname in PERSON:
        person = PERSON.get(lname)

    # otherwise, nope, not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

    return person


def create(person):
    """
    This function creates a new person in the person structure
    based on the passed in person data
    :param person:  person to create in person structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    if lname not in PERSON and lname is not None:
        PERSON[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PERSON[lname], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Peron with last name {lname} already exists".format(lname=lname),
        )


def update(lname, person):
    """
    This function updates an existing person in the person structure
    :param lname:   last name of person to update in the person structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in person?
    if lname in PERSON:
        PERSON[lname]["fname"] = person.get("fname")
        PERSON[lname]["timestamp"] = get_timestamp()

        return PERSON[lname]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )


def delete(lname):
    """
    This function deletes a person from the person structure
    :param lname:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if lname in PERSON:
        del PERSON[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )