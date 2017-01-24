import yaml

# Set up a few classes for us to work with

class PlayerChoice:
    def __init__(self, configuration):
        self.description = configuration['description']
        self._next_level = configuration['next_level']


class Level:
    def __init__(self, configuration):
        self.description = configuration['description']
        self.choices = []

        for choice in configuration['options']:
            self.choices.append(PlayerChoice(choice))


# Actual run-time stuff
with open("level.yaml", 'r') as stream:
    try:
        level_data = yaml.load(stream)
        level = Level(level_data)
    except yaml.YAMLError as exc:
        print(exc)


print(level.description)

for choice in level.choices:
    print(choice.description)
