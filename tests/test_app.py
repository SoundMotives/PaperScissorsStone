from playwright.sync_api import Page, expect

def test_get_home_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text("Welcome to Paper Scissors Stone") 

def test_home_page_submits_choice(page, test_web_address):
    page.set_default_timeout(5000)  # Set a timeout in milliseconds
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name=choice]", "Stone")
    page.click("button[type=submit]")
    response_text_locator = page.locator(".response")
    response_text = response_text_locator.text_content()
    responses = ["It's a tie!", "You lost!", "You won!"]
    assert any(response_text in response for response in responses) 

def test_home_page_returns_error(page, test_web_address):
    page.set_default_timeout(5000)  # Set a timeout in milliseconds
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name=choice]", "Stones")
    page.click("button[type=submit]")
    errors_locator = page.locator(".errors")
    expect(errors_locator).to_have_text("Your guess must be either 'paper', 'scissors' or 'stone' to play! Try again!")

