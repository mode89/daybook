import application
import tempfile
from unittest import mock

@given("not implemented")
def step_impl(context):
    raise NotImplemented

@given("application")
def step_impl(context):
    context.application = application.Application()

@given("application with temp journal and mocked config")
def step_impl(context):
    context.temp_journal = tempfile.NamedTemporaryFile()
    context.application = application.Application()
    context.application.load_config = mock.Mock(
        return_value={
            "journal": context.temp_journal.name
        })

@given("mock loading of configuration")
def step_impl(context):
    context.application.load_config = mock.Mock()

@given("mock composing of entry")
def step_impl(context):
    context.application.compose_entry = mock.Mock(return_value="")

@given("composed entry is")
def step_impl(context):
    context.application.compose_entry = \
        mock.Mock(return_value=context.text)

@given("time is \"{time}\"")
def step_impl(context, time):
    context.application.time = mock.Mock(return_value=time)

@given("load config from file \"{path}\"")
def step_impl(context, path):
    context.application.config_path = path

@given("content of journal file is")
def step_impl(context):
    with open(context.temp_journal.name, "w") as f:
        f.write(context.text)

@when("run application")
def step_impl(context):
    context.application.run()

@then("should compose entry")
def step_impl(context):
    assert context.application.compose_entry.call_count == 1

@then("content of journal is")
def step_impl(context):
    assert context.application.journal == context.text, \
        "{0} != {1}".format(context.application.journal, context.text)

@then("content of journal file is")
def step_impl(context):
    with open(context.application.config["journal"], "r") as f:
        text = f.read()
        assert text == context.text, \
            "{0} != {1}".format(text, context.text)

@then("journal file name is \"{name}\"")
def step_impl(context, name):
    assert context.application.config["journal"] == name
