from setuptools import setup

setup(
    name="daybook",
    description="Command-line journal application",
    url="https://github.com/mode89/daybook",
    author="Mode",
    author_email="mode89@mail.ru",
    license="MIT",
    packages=["daybook"],
    entry_points={
        "console_scripts": [
            "daybook = daybook.cli:main"
        ]
    }
)
