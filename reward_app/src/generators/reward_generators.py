from random import randint
from abstracts.abstract_classes import ItemFabric
from src.rewards import reward_classes as reward

class GoldFactory(ItemFabric):
    val = 3

    def make_item(self):
        return reward.Gold()

class GemFactory(ItemFabric):
    val = 1

    def make_item(self):
        return reward.Gem()

class WeaponFactory(ItemFabric):
    val = 10

    def make_item(self):
        return reward.Weapon()

class ArmourFactory(ItemFabric):
    val = 10

    def make_item(self):
        return reward.Armour()

class PotionFactory(ItemFabric):
    val = 10

    def make_item(self):
        return reward.Potion()

class ExpFactory(ItemFabric):
    val = 10

    def make_item(self):
        return reward.Exp()

class JewerlyFactory(ItemFabric):
    val = 10

    def make_item(self):
        return reward.Jewerly()

TURNS = 20

REWARDS_FACTORIES = [GoldFactory(),
                      GemFactory(),
                      WeaponFactory(),
                      ArmourFactory(),
                      PotionFactory(),
                      ExpFactory(),
                      JewerlyFactory()]

ranked_rewards = [reward for reward in REWARDS_FACTORIES for _ in range(reward.rarity)]

for i in range(TURNS):
    ranked_rewards[randint(0, len(ranked_rewards) - 1)].create_item().open()
    