import cli

@given("not implemented")
def step_impl(context):
    raise NotImplemented

@when("run application")
def step_impl(context):
    cli.main()

@then("compose text")
def step_impl(context):
    assert cli.compose_text.call_count == 1
