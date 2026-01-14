from playwright.sync_api import sync_playwright

# Official Wordle game URL
WORDLE_URL = "https://www.nytimes.com/games/wordle/index.html"


def launch_browser(headless=False):
    # Start Playwright and launch chromium
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=headless)

    # Create a fresh browser context and page
    context = browser.new_context()
    page = context.new_page()

    # Open the Wordle page
    page.goto(WORDLE_URL)

    # Give the page time to fully load
    page.wait_for_timeout(3000)

    # Return everything so main.py can control it
    return playwright, browser, page
