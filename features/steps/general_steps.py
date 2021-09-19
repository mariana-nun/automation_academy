from behave import step
from hamcrest import assert_that, equal_to


@step("I am on the Home page")
@step("I go to the Home page")
def step_impl(context):
    context.page.go_to_the_home_page()
    context.page.wait_until_page_load()


@step("I search an hotel in {location}")
def step_impl(context, location):
    context.page = context.page.sent_travel_data(location)


@step("I search for a car form {origin} to {destination}")
def step_impl(context, origin, destination):
    context.page= context.page.search_cars(origin, destination)


@step("I see the first {quantity} results listed for that {type} search")
def step_impl(context, quantity, type):
    results = context.page.get_search_results(type)
    assert_that(len(results), equal_to(int(quantity)))


@step("I see the no {type} results message")
def step_impl(context, type):
    error_message = {
        "hotel": "Sorry, we couldn’t find any results. Try adjusting your search.",
        "car": "Sorry, there are no cars available at this location for your selected dates and time."
    }
    assert_that(context.page.get_the_no_result_message(type), equal_to(error_message[type]))
