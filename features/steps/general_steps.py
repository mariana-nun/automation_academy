from behave import step
from hamcrest import assert_that, equal_to


@step("I am on the Home page")
@step("I go to the Home page")
def step_impl(context):
    context.page.go_to_the_home_page()
    context.page.wait_until_page_load()


@step('I search "{term}"')
def step_impl(context, term):
    context.term = term
    context.page = context.page.search(context.term)


@step("I see the first {quantity} results listed for that search")
def step_impl(context, quantity):
    results = context.page.get_search_results()
    assert_that(context.page.get_result_quantity(), equal_to(f"{quantity} results have been found."))
    assert_that(len(results), equal_to(int(quantity)))


@step("I see no results message")
def step_impl(context):
    assert_that(context.page.get_no_result_message(), equal_to(f'No results were found for your search "{context.term}"'))


@step("I go to the login page")
def step_impl(context):
    context.page = context.page.go_to_login()
    context.page.wait_until_page_load()
