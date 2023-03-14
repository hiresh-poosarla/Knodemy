import random


def get_response(message: str) -> str: 
    p_message = message.lower()

    if p_message == 'hello': 
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1,6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'
    


    if p_message == 'i am tired':
        return '`that is ok!'


    return 'I didn\'t understand what you wrote. Try typing "!help".'