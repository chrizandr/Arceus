from pysondb import db
import pdb

data = db.getDb("data/trainer_id.json")

def get_trainer_id(member):
    username = str(member)
    entry = data.getBy({"user": username})
    if len(entry) == 1:
        value = entry[0]["trainer_number"]
        response = "{username}: " + str(value)
        return response.format(username=member.mention)
    else:
        return "Idk man."


def del_trainer_id(member):
    username = str(member)
    entry = data.getBy({"user": username})
    if len(entry) == 1:
        idx = entry[0]["id"]
        data.deleteById(idx)
        return "You're dead to me {username}.".format(username=member.mention)
    else:
        return "Idk man."


def set_trainer_id(member, trainer_id):
    username = str(member)
    curr_ids = []
    if trainer_id.isdecimal():
        entry = data.getBy({"user": username})
        if len(entry) == 1:
            value = entry[0]["trainer_number"]
            curr_ids = value.replace(" ", "").split(",")
            curr_ids.append(trainer_id)
            data.updateByQuery({"user": username}, {"trainer_number": ", ".join(curr_ids)})
        else:
            data.add({"user": username, "trainer_number": ", ".join([trainer_id])})
        return "Good to know."
    else:
        return "Use only numbers noob."


def trainer_id_handler(message):
    values = message.content.split()
    response = ""
    if len(values) > 2:
        response = "Use this format ffs ```!id <trainer ID>```"

    if len(values) == 1 and values[0] == "!id":
        response = get_trainer_id(message.author)

    if len(values) == 2 and values[0] == "!id":
        if len(message.mentions) == 1:
            member = message.mentions[0]
            response = get_trainer_id(member)

        elif len(message.mentions) > 1:
            response = "One at a time bb."

        elif values[1] == "forget":
            response = del_trainer_id(message.author)

        else:
            response = set_trainer_id(message.author, values[1])
    return response

if __name__ == "__main__":
  print(db.keys())