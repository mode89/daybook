import application
from unittest import mock

@given("not implemented")
def step_impl(context):
    raise NotImplemented

@given("application")
def step_impl(context):
    context.application = application.Application()

@given("composed text is")
def step_impl(context):
    context.application.edit = mock.Mock(return_value=context.text)

@given("time is \"{time}\"")
def step_impl(context, time):
    context.application.time = mock.Mock(return_value=time)

@when("run application")
def step_impl(context):
    context.application.run()

@then("should edit text")
def step_impl(context):
    assert context.application.edit.call_count == 1

@then("content of journal is")
def step_impl(context):
    assert context.application.journal == context.text, \
        "{0} != {1}".format(context.application.journal, context.text)
