from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Display a mad libs story using an adjective and noun provided by the user."""
    return f'Legends tell of the {adjective} {noun}, which can only be found by one pure of heart.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Display the result of multiplying two numbers"""
    if number1.isdigit() and number2.isdigit():
        return f'{number1} times {number2} is {int(number1) * int(number2)}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'
    
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Display the users word n times."""
    if n.isdigit():
        return (f'{word} ' * int(n))
    else:
        return 'Invalid input. Please try again by entering a word and a number.'
    
@app.route('/dicegame')
def dicegame():
    "Generates a random number from 1 to 6. If the user rolls a 6, they win the game; otherwise, they lose."
    roll = random.randint(1, 6)
    outcome = 'won' if roll == 6 else 'lost'
    return f'You rolled a {roll}. You {outcome}!'


if __name__ == '__main__':
    app.run(debug=True)

