from bot.browser import launch_browser
from bot.actions import start_game, focus_board, enter_guess
from bot.board_reader import read_feedback_from_board
from bot.solver import WordleSolver


def load_words():
    # Load all valid 5-letter words from file
    with open("words/words.txt") as f:
        return [w.strip() for w in f.readlines()]


def main():
    print(">>> main() started")

    # Initialize solver with the word list
    words = load_words()
    solver = WordleSolver(words)

    # Launch browser and open a visible Chrome window
    playwright, browser, page = launch_browser(headless=False)

    # Start Wordle and make sure the board is focused
    start_game(page)
    focus_board(page)

    # Wordle allows up to 6 guesses
    for attempt in range(6):
        guess = solver.next_guess()
        print(f"Guess {attempt + 1}: {guess}")

        # Type the guess into the game
        enter_guess(page, guess)

        # Wait for tile feedback to appear after animation
        feedback = None
        for _ in range(40):  # ~12 seconds max
            page.wait_for_timeout(300)
            feedback = read_feedback_from_board(page, attempt)
            if feedback:
                break

        # If feedback never showed up, stop safely
        if not feedback:
            print("ERROR: Feedback never appeared")
            break

        print("Feedback:", feedback)

        # If all tiles are green, the word is solved
        if all(f == "correct" for f in feedback):
            print("SOLVED!")
            break

        # Update solver rules and narrow down possible words
        solver.update_constraints(guess, feedback)
        solver.filter_words()

    # Keep the browser open briefly so the result is visible
    try:
        page.wait_for_timeout(5000)
    except:
        pass

    # Clean shutdown
    browser.close()
    playwright.stop()


if __name__ == "__main__":
    main()