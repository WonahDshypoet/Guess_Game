from django.shortcuts import render
import random


def guess_game(request):
    if 'guess' not in request.session or 'remaining_guesses' not in request.session:
        # Initialize a new game when the page is loaded or when session data is missing
        request.session['guess'] = random.randint(1, 100)
        request.session['remaining_guesses'] = 5

    if request.method == 'POST':
        num = int(request.POST.get('guess'))
        remaining_guesses = request.session.get('remaining_guesses', 5)
        correct_number = request.session['guess']

        if num == correct_number:
            message = 'Correct guess!, You Genius.'

            # Reset the game if answer's correct
            del request.session['guess']
            del request.session['remaining_guesses']

            # message = 'Enter Guess'

        elif num < correct_number:
            message = 'Too low...'
            remaining_guesses -= 1
        else:
            message = 'Too high...'
            remaining_guesses -= 1

        request.session['remaining_guesses'] = remaining_guesses

        if remaining_guesses <= 0:
            message = 'Game over! You have run out of guesses. Number was ', request.session['guess'], 'Try Again?'

            # Reset the game when it's over
            del request.session['guess']
            del request.session['remaining_guesses']

            # message = 'Enter Guess, Try getting it this round.'

    else:
        message = 'Enter your guess:'

    context = {
        'message': message,
    }

    return render(request, 'play_game.html', context)
