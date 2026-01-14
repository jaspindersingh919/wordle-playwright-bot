def start_game(page):
    # Click the "Play" button if Wordle shows the intro screen
    try:
        play_button = page.locator("button:has-text('Play')")
        play_button.wait_for(timeout=5000)
        play_button.click()
        page.wait_for_timeout(2000)
    except:
        # Sometimes the game starts without this screen
        pass

    # Close the help / instructions popup if it appears
    try:
        page.keyboard.press("Escape")
        page.wait_for_timeout(1000)
    except:
        pass


def enter_guess(page, word):
    # Type the word like a human and submit it
    page.keyboard.type(word, delay=150)
    page.keyboard.press("Enter")

    # Wait for the tile flip animation to finish
    page.wait_for_timeout(3500)


def focus_board(page):
    # Make sure the Wordle board has keyboard focus
    page.wait_for_timeout(3000)
    page.mouse.click(500, 500)
    page.wait_for_timeout(500)