#!/usr/bin/env python3
from task_04_flyingfish import Fish, FlyingFish

print(FlyingFish.mro())
flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

