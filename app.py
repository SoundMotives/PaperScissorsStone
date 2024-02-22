import os
from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Route for Homepage
@app.route("/", methods=['GET', 'POST'])
def home_page():
    # Get method
    if request.method == "GET":
        return render_template("homepage.html")
    else:
    # Post method
        guess = request.form["choice"]
        guess = guess.lower()

        choices = ['paper', 'scissors', 'stone']
        opponent_choice = random.choice(choices)
    # Wrong Answers 
        if guess not in choices:
            errors = "Your guess must be either 'paper', 'scissors' or 'stone' to play! Try again!"
            return render_template("homepage.html", errors=errors)
    #Generate opponent choice

    # tie
        if guess == opponent_choice:
            response1 = "You tied!"
            response2 = f"You both guessed {guess}."
            return render_template("result.html", response1=response1, response2=response2)
    # Victory or loss
        else:
            if guess == 'paper' and opponent_choice == "scissors" \
                or guess == "scissors" and opponent_choice == 'stone' \
                or guess == "stone" and opponent_choice == "paper":
                response1 = "You lost!"
                response2 = f"You chose {guess} and your opponent chose {opponent_choice}."
            else:
                response1 = "You won!"
                response2 = f"You chose {guess} and your opponent {opponent_choice}." 
            return render_template("result.html", response1=response1, response2=response2)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
