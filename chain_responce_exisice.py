import unittest


class Creature:
    def __init__(self, game, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game

    @property
    def attack(self):
        return self.initial_attack

    @property
    def defense(self):
        return self.initial_defense


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)


class Game:
    def __init__(self):
        self.creatures = []


class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)
