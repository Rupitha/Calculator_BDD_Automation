from behave import given, when, then
from Page.Calc_page import calcpage


@then(u'returns {expected_result}')
def step_impl_check_result(context, expected_result):
    calcpage.check_result(expected_result)