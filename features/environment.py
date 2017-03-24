from unittest import mock

def after_step(context, step):
    if context.feature.name == "Core functionality" and \
        context.scenario.name == "edit text" and \
        step.name == "application":
        context.application.edit = mock.Mock(return_value=str())
