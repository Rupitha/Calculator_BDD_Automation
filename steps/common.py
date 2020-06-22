import logging
from behave import given, when, then
from Calculator.Calculator_app import calcapp
from selenium.webdriver.common.keys import Keys

@given(u'I load the website')
def step_impl_load_website(context):
    calcapp.load_website()


@when(u'Calc {ops}')
def step_impl_do_math(context, ops):
    # logging.info("I got ops\n")
    ops.replace(" ", "")
    # logging.info(ops)
    key_ops = []
    for item in ops:
        key_ops.append(send_keys_dict[item])
    # logging.info("ha ha")
    # logging.info("key_ops")
    # logging.info(key_ops)
    calcapp.do_math(key_ops)



send_keys_dict = {
    "*": Keys.MULTIPLY,
    "0": Keys.NUMPAD0,
    "1": Keys.NUMPAD1,
    "2": Keys.NUMPAD2,
    "3": Keys.NUMPAD3,
    "4": Keys.NUMPAD4,
    "5": Keys.NUMPAD5,
    "6": Keys.NUMPAD6,
    "7": Keys.NUMPAD7,
    "8": Keys.NUMPAD8,
    "9": Keys.NUMPAD9,
    "+": Keys.ADD,
    "-": Keys.SUBTRACT,
    ".": Keys.DECIMAL,
    "/": Keys.DIVIDE,
    "=": Keys.EQUALS
}