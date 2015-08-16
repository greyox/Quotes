__author__ = 'Steve'


from random import *
from flask import Flask, render_template


app = Flask(__name__)

request = ['Bring me a','I want a','Hi.  I would like a']
tone = ['kindly asks','loudly bellows','softly murmurs','violently yells']
name = ['Rick','Carl','Carol','Darrel','Michone','Baby Judith','Glenn','Maggie']
food = ['carrots','slim jims','apples','cheese','baby back ribs','nuts']
drink = ['water','sweet tea','yak milk','whisky','coffee','mead']
temp = ['hot','cold','room temperature','streaming','scalding','frosty']
flavor = ['bland', 'spicy', 'salty', 'sweet', 'bitter', 'tangy']
food_serving = ['plate','side', 'pound','handful','pile','bowl','crap ton']
drink_serving = ['jug','glass', 'tankard','shot','pitcher']
end = ['please','this instant!','pronto!', 'chop, chop!',"if that's ok?"]

def genQuotes(num_quotes):
    start = 0
    while start < num_quotes:
        yield choice(name) + ' ' + choice(tone) + '...' + choice(request) + ' ' + choice(food_serving) + ' of ' + choice(flavor) \
    + ' ' + choice(food)  + ' and a ' + choice(temp) + ' ' + choice(drink_serving) + ' of ' + choice(drink) + ', ' + choice(end)
        start += 1






@app.route('/')
def index():
    return render_template('index.html',quotes=list(genQuotes(1)))







if __name__ == '__main__':
    app.run(port=5001, debug=True)



