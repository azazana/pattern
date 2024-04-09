import unittest


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            args[0](item)


class Game:
    def __init__(self):
        self.creatures = []
        self.queries = Event()

    def check_creatures(self, sender):
        self.creatures(sender)



class Creature:
    def __init__(self, game, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game

    @property
    def attack(self):
        self.game.check_creatures(self.handle)
        return self.initial_attack

    @property
    def defense(self):
        self.game.check_creatures(self.handle)
        return self.initial_defense

    def handle(self, sender, query):
        pass


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    def handle(self, sender):
        if isinstance(sender, GoblinKing):
            self.attack += 1
        if isinstance(sender, Goblin):
            print('Goblin')
            self.defense += 1


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)


class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)
        goblin2 = Goblin(game)
        game.creatures.append(goblin2)
        self.assertEqual(2, goblin2.defense)