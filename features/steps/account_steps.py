from behave import step
from hamcrest import assert_that, equal_to


@step("I login with the following information")
def step_impl(context):
    context.page = context.page.go_to_login()
    context.page.wait_until_page_load()
    for row in context.table:
        context.user_data = {"username": row['username']}
        context.page.sign_in(row['email'], row['password'])


@step("Create an account with {email} email")
def step_impl(context, email):
    context.page.create_account(email)


@step("I complete the account creation form with default data")
def step_impl(context):
    context.user_data = {
        "gender": "mr",
        "first_name": "test",
        "last_name": "account",
        "username": "test account",
        "password": "Password123",
        "day": "10",
        "month": "2",
        "year": "1990",
        "address": "3408  Road",
        "city": "Stevensville",
        "state": "1",
        "country": "21",
        "postcode": "00000",
        "phone_mobile": "1234567890"
    }
    context.page.complete_account_creation_form(context.user_data)


@step("The login is done")
@step("The account creation finish successfully")
def step_impl(context):
    assert_that(context.page.check_correct_login(), equal_to(context.user_data["username"]))


@step("Create an account with default data")
def step_impl(context):
    context.execute_steps("""
        When I go to the login page
        And Create an account with random email
        And I complete the account creation form with default data
    """)
