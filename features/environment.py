import cli
from unittest import mock

def before_scenario(context, scenario):
    if scenario.feature.name == "Core functionality" and \
        scenario.name == "compose text":
        context.patchComposeText = mock.patch("cli.compose_text")
        context.patchComposeText.start()

def after_scenario(context, scenario):
    if scenario.feature.name == "Core functionality" and \
        scenario.name == "compose text":
        context.patchComposeText.stop()
