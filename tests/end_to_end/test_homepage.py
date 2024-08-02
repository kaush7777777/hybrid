import pytest

@pytest.mark.end_to_end
def test_homepage(home_page):
    assert home_page.title()== "Current weather and forecast - OpenWeatherMap", "Title is not as expected"

   
    
