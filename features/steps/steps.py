import application

@given("not implemented")
def step_impl(context):
    raise NotImplemented

@given("application")
def step_impl(context):
    context.application = application.Application()

@when("run application")
def step_impl(context):
    context.application.run()

@then("should edit text")
def step_impl(context):
    assert context.application.edit.call_count == 1
