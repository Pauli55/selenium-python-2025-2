from behave import given, when, then
from selenium import webdriver
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_resuts_page import ImdbResultPage
from pages.imdb_movie_page import ImdbMoviePage

@given('el usuario está en el home page de imdb.com')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_home = ImdbHomePage(context.driver)

@when('el usuario busca la pelicula "{movie_name}"')
def step_search_page(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.imdb_result = ImdbResultPage(context.driver) 

@when('presiona el link del primer resultado de la pelicula')
def step_press_link(context):
    context.imdb_result.press_movie_link()
    context.imdb_movie = ImdbMoviePage(context.driver)

@then('el nombre de la pelicula debe ser "{expected_name}" y el raiting de la pelicula debe ser "{expected_rating}"')
def step_compare_names(context, expected_name,expected_rating):
    actual_name = context.imdb_movie.get_movie_name()
    actual_rating = context.imdb_movie.get_movie_rating()
    assert (actual_name == expected_name) and ( actual_rating == expected_rating), f"Expected name {expected_name}, but got {actual_name} Expected rating {expected_rating}, but got {actual_rating}"
    context.driver.quit()


