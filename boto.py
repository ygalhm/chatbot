"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random
from weather import Weather, Unit
name = ""
getName = False


@route('/', method='GET')
def index():
    global name
    global getName
    name = ""
    getName = False
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps(get_message(user_message))


def get_message(user_message):

    user_message = user_message.lower()
    user_message_split = user_message.split()

    if name is "":
        return hello_user(user_message, user_message_split)
    else:
        return speak_user(user_message, user_message_split)


def hello_user(user_message, user_message_split):
    global name
    hello_list = ['hello', 'my', 'name', 'is', 'i', 'am', "i'm", 'hey', 'hi', 'yo']
    for word in user_message_split:
        if word not in hello_list:
            name = word
            return {"animation": "excited", "msg": ("Your name is {0} ? Right ?".format(name))}

    speak_user(user_message, user_message_split)


def speak_user(user_message, user_message_split):

    swear_list = ['fuck', 'fucker', 'bitch', 'bastard', 'dick', 'asshole', 'cunt', 'shit', 'piss', 'damn']
    swear_list_answer = ['If you want to keep your job, you should always be polite to your boss.', 'You make me sad. Be nice please :(', 'Polite people do not argue in public.']

    hello_list = ['hello', 'hi', 'yo', 'hey', 'howdy', 'welcome', 'shalom', 'salam', 'bonjour', 'heyy']

    joke_list = ['joke', 'fun', 'laugh', 'joking', 'funny', 'farce', 'yarn', 'pleasantry', 'prank']
    joke_list_answer = ['I bought a universal remote control today. I’m kind of afraid of myself now…', 'Time is money. Therefore, ATMs are time machines.', 'How Long is a Chinese name.', 'Tomato is a fruit, right? Does that make ketchup a smoothie?']

    inlove_list = ['love', 'crush', 'flirt', 'fall in love', 'date', 'hug', 'kiss', 'wedding', 'engaged']
    inlove_list_answer = ["I love being married. It's so great to find one special person you want to annoy for the rest of your life", "3 words, 7 letters: I Love You"]

    afraid_list = ['kill', 'murder', 'intimidate', 'knife', 'gun', 'ghost', 'bouh', 'zombie', 'vampire']
    afraid_list_answer = ['Sniff. Do not scare me please.', 'Once, I heard about a guy, his name is Frankestein.']

    bored_list = ['school', 'university', 'work', 'working', 'project', 'mozart', 'people']
    bored_list_answer = ["Don't annoy me with such thing", 'Leave me alone, or speak about jokes', 'Arghhhhhhh']

    dancing_list = ['party', 'sing', 'song', 'drink', 'partying', 'fiesta', 'shalvata','gift', 'present', 'bar']
    dancing_list_answer = ['I looooove to dance, dance, dance', "Let's party yihaaaaa", "I love Santa Papa, wouuuuh"]

    dog_list = ['animal', 'dog', 'cat', 'animals', 'dogs', 'woof', 'chihuahua' ]
    dog_list_answer = ['I love animals, and especially dogs', 'woof woof woof', "I've a robot dog @home ;)"]

    giggling_list = ['smart', 'beautiful', 'kind', 'strong', 'brave', 'tall']
    giggling_list_answer = ['Oh yeah keep going on my friend', 'Niark niark niark', 'Mmmmmmh thank you Mr.Burns']

    heartbroke_list = ['ugly', 'bad', 'deformed', 'repelling', 'hideous', 'awful']
    heartbroke_list_answer = ['Ohhhhh do not say such things, you break my heart', 'snif snif snif', 'noooooooo']

    money_list = ['money', 'dollars', 'euros', 'shekels', 'nis', 'rich', 'bank', 'million']
    money_list_answer = ['I need dollars, dollars what i need', 'money, money, money', '$$$$$$$$$$$$$$$$$']

    no_list = ['error', 'leave', 'alone', 'never', 'impossible', 'jail', 'prison']
    no_list_answer = ['never say never amigo', 'impossible is nothing like Nike said', 'error 404 bzzzzzzzzzz']

    ok_list = ['agree', 'play', 'playing', 'games', 'game', 'friend', 'together']
    ok_list_answer = ['Boto like you, Boto is your friend :)', "Yeaaaaah, let's go", 'vamoooooooos']

    takeoff_list = ['plane', 'trip', 'journey', 'countries', 'train', 'adventure', 'trek']
    takeoff_list_answer = ['To infinity, and beyond !', 'I love travelling everywhere in the world', 'Fiouuuuu, vamos!']

    waiting_list = ['wait', 'time', 'long', 'interim', 'lifetime', 'months', 'duration']
    waiting_list_answer = ['Be patient dude', 'mmmmmh, give me a moment please', 'come back later if you wanna know a good joke ;)']

    weather_list = ['weather', 'temperature', 'sunshine', 'cloud', 'sun', 'rain']

    yes_list = ['yes', 'y', 'yeah', 'yep', 'yup']

    global getName
    global name

    if getName is False:
        if any((word in yes_list for word in user_message_split)):
            getName = True
            return {"animation": "excited", "msg": ("Alright {0} ! Nice to meet you".format(name))}
        else:
            getName = True
            name = 'Mr. No name'
            return {"animation": "giggling", "msg": "Anyway, your name is weird, i don't want to learn it ;)"}
    else:
        if any((word in user_message_split for word in swear_list)):
                return {"animation": "crying", "msg": random.choice(swear_list_answer)}
        elif any((word in user_message_split for word in hello_list)):
                return {"animation": "excited", "msg": ("Hey {0} ! What's up ?.".format(name))}
        elif any((word in user_message_split for word in weather_list)):
                city = "Tel-Aviv"
                weather = Weather(unit=Unit.CELSIUS)
                location = weather.lookup_by_location(city)
                condition = location.condition
                return {"animation": "excited", "msg": ("Hey, in {0} ! The weather is: {1} and the temperature is {2}.".format(city, condition.text, condition.temp))}
        elif any((word in user_message_split for word in joke_list)):
                return {"animation": "laughing", "msg": random.choice(joke_list_answer)}
        elif any((word in user_message_split for word in inlove_list)):
                return {"animation": "inlove", "msg": random.choice(inlove_list_answer)}
        elif any((word in user_message_split for word in afraid_list)):
                return {"animation": "afraid", "msg": random.choice(afraid_list_answer)}
        elif any((word in user_message_split for word in bored_list)):
                return {"animation": "afraid", "msg": random.choice(bored_list_answer)}
        elif any((word in user_message_split for word in dancing_list)):
                return {"animation": "afraid", "msg": random.choice(dancing_list_answer)}
        elif any((word in user_message_split for word in dog_list)):
                return {"animation": "afraid", "msg": random.choice(dog_list_answer)}
        elif any((word in user_message_split for word in giggling_list)):
                return {"animation": "afraid", "msg": random.choice(giggling_list_answer)}
        elif any((word in user_message_split for word in heartbroke_list)):
                return {"animation": "afraid", "msg": random.choice(heartbroke_list_answer)}
        elif any((word in user_message_split for word in money_list)):
                return {"animation": "afraid", "msg": random.choice(money_list_answer)}
        elif any((word in user_message_split for word in no_list)):
                return {"animation": "afraid", "msg": random.choice(no_list_answer)}
        elif any((word in user_message_split for word in ok_list)):
                return {"animation": "afraid", "msg": random.choice(ok_list_answer)}
        elif any((word in user_message_split for word in takeoff_list)):
                return {"animation": "afraid", "msg": random.choice(takeoff_list_answer)}
        elif any((word in user_message_split for word in waiting_list)):
                return {"animation": "afraid", "msg": random.choice(waiting_list_answer)}
        else:
                return {"animation": "confused", "msg": "what ? i'm so confused, can you speak normally please ? i'm just a robot ;)"}


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
