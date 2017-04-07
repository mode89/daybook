import unittest

def after_scenario(context, scenario):
    unittest.mock.patch.stopall()
