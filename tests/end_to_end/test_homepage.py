import pytest

import pytest

@pytest.mark.end_to_end
def test_homepage(home_page):
    page = home_page

    assert page.title() == "Current weather and forecast - OpenWeatherMap", "Title is not as expected"
    page.click('button:has-text("Accept")')  # Example button click, adjust the selector as needed
    page.click('a:has-text("Sign in")')
    page.get_by_label("Email").fill("charith.sliit@gmail.com")
    page.get_by_placeholder("Password").fill("123456789")
    page.get_by_role("button", name="Submit").click()
    page.get_by_text("Invalid Email or password.").click()
    page.get_by_role("link", name="Create an Account.").click()


   
