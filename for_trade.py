from pysondb import db
import pdb

data = db.getDb("data/for_trade.json")
USAGE = "Use this format ffs ```!ft <trainer_name>\n!ft add <your shit>\n!ft forget```"

def get_trainer_ft(member):
    """Get items for trade by member"""
    username = str(member)
    entry = data.getBy({"user": username})
    if len(entry) == 1:
        value = entry[0]["for_trade"]
        response = "{username} is trading:\n```\n" + str(value) + "\n```"
        return response.format(username=member.mention)
    else:
        response = "{username} is trading absolutely nothing cause they're poor."
        return response.format(username=member.mention)


def del_trainer_ft(member):
    """Delete items for trade by member"""
    username = str(member)
    entry = data.getBy({"user": username})
    if len(entry) == 1:
        idx = entry[0]["id"]
        data.deleteById(idx)
        return "Guess you're poor now {username}.".format(username=member.mention)
    else:
        response = "{username} you poor bro, nothing to forget."
        return response.format(username=member.mention)


def set_trainer_ft(member, items):
    """Set items for trade by member"""
    if len(items) > 0:
        username = str(member)
        entry = data.getBy({"user": username})
        curr_ids = []
        if len(entry) == 1:
            curr_ids = entry[0]["for_trade"].split("\n")
            curr_ids.append(items)
            data.updateByQuery({"user": username}, {"for_trade": "\n".join(curr_ids)})
        else:
            data.add({"user": username, "for_trade": "\n".join([items])})
        return "Okay bruh."
    return USAGE


def trainer_ft_handler(message):
    """Handler code"""
    values = message.content.split()
    response = USAGE
    if len(values) == 1 and values[0] == "!ft":
        response = get_trainer_ft(message.author)

    if len(values) >= 2 and values[0] == "!ft":
        if len(message.mentions) == 1:
            member = message.mentions[0]
            response = get_trainer_ft(member)

        if len(message.mentions) > 1:
            response = "One at a time bb."

        if values[1] == "forget":
            response = del_trainer_ft(message.author)

        if values[1] == "help":
            response = USAGE

        if values[1] == "add":
            response = set_trainer_ft(message.author, message.content.replace("!ft add", "").strip())
    return response


if __name__ == "__main__":
  print(db.keys())