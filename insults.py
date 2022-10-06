import random

from database import DataBase as Db


def insults():
    data = Db.read_data(Db(), "database/compliments.json")
    da = data["insult"]

    pop = random.choices(da)
    return pop
