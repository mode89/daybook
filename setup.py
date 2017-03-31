from setuptools import setup

setup(
    name="journal",
    description="Command-line journal application",
    url="https://github.com/mode89/journal",
    author="Mode",
    author_email="mode89@mail.ru",
    license="MIT",
    packages=["journal"],
    entry_points={
        "console_scripts": [
            "journal = journal.cli:main"
        ]
    }
)
