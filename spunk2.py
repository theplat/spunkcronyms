from flask import Flask, request
from random import randrange
crapp = Flask(__name__)


def generate_spunk():
    with open(f"spunkcronyms.list", "r") as f:
        spunklist = f.readlines()
    spunk = spunklist[randrange(len(spunklist))]
    return spunk

@crapp.route("/", methods=['GET'])
def spunk():
    output = generate_spunk()
    return f"Your spunkcronym is: {output}"

@crapp.route("/yourmom", methods=['GET'])
def moimspunk():
    output = generate_spunk()
    return f"I left a hot load of {output} in your mom lastnight"

