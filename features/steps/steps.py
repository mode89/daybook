from daybook.application import Application
import random
import string
import tempfile
from unittest import mock

def random_string(length):
    lst = [random.choice(string.ascii_letters) for n in range(length)]
    return ''.join(lst)

@given("not implemented")
def step_impl(context):
    raise NotImplemented

@given("application")
def step_impl(context):
    context.application = Application()

@given("application with temp journal and mocked config")
def step_impl(context):
    context.temp_journal = tempfile.NamedTemporaryFile()
    context.application = Application()
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

@given("mock text editing")
def step_impl(context):
    context.application.edit_text = mock.Mock(return_value="")

@then("should edit text")
def step_impl(context):
    assert context.application.edit_text.call_count == 1

@given("command line is \"{text}\"")
def step_impl(context, text):
    context.application.args = text.split()

@given("edited text is")
def step_impl(context):
    context.application.edit_text = mock.Mock(return_value=context.text)

@then("run and catch {class_name}(\"{message}\")")
def step_impl(context, class_name, message):
    try:
        context.application.run()
    except Exception as e:
        context.exception = e
        assert e.__class__.__name__ == class_name
        assert str(e) == message
    finally:
        assert context.exception is not None

@given("journal with random content")
def step_impl(context):
    length = random.randint(10, 100)
    context.journal = random_string(length)
    context.application.journal = context.journal

@given("random password")
def step_impl(context):
    length = random.randint(5, 15)
    context.password = random_string(length)
    context.application.password = context.password

@when("encrypt journal")
def step_impl(context):
    context.application.encrypt_journal()

@then("content of journal is not identical to initial content")
def step_impl(context):
    assert context.application.journal != context.journal.encode("utf-8")

@when("decrypt journal")
def step_impl(context):
    context.application.decrypt_journal()

@then("content of journal is identical to initial content")
def step_impl(context):
    assert context.application.journal == context.journal, \
        context.application.journal + " != " + context.journal
