
def fun_commands(message):
    """Fun commands that can be added here"""
    response = None
    if message.content.startswith('!allhail'):
        response = 'King and Queen Chowi'
    if message.content.startswith('!tst'):
        response = "I'm ngl, he's weird"
    if message.content.startswith('!chrizandr') or message.content.startswith('!chris'):
        response = "Master"
    if message.content.startswith('!gamer'):
        response = "Did you mean \"poop\"?"
    if message.content.startswith('!spookz'):
        response = "SpookZ is bae"
    if message.content.startswith('!shiva'):
        response = "He is rich now, start begging him for freebies."
    # if "contest" in message.content.lower():
    #     response = 'Grats Matt'
    return response
