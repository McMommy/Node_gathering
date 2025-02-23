#creating the mining system that ethan wanted
#fixing git


import time
import random


class Player():
    def __init__(self, name, health, mining_stamina, logging_stamina, max_mining_stamina, max_logging_stamina):
        self.name = name
        self.health = health
        self.mining_stamina = mining_stamina
        self.logging_stamina = logging_stamina
        self.max_mining_stamina = max_mining_stamina
        self.max_logging_stamina = max_logging_stamina
        self.inventory = {
            "iron": 0,
            "copper": 0,
            "stone": 0,
            "oak": 0,
            "chesnut": 0
        }


class Nodes():
    def __init__(self, node_type, name, health, max_health, breaking_power, spawn_chance, resource):
        self.node_type = node_type
        self.name = name
        self.health = health
        self.max_health = max_health
        self.breaking_power = breaking_power
        self.spawn_chance = spawn_chance
        self.resource = resource


class Tools():
    def __init__(self, tool_type, name, damage, breaking_power,):
        self.tool_type = tool_type
        self.name = name
        self.damage = damage
        self.breaking_power = breaking_power

#player
lumberjack = Player("", 100, 60, 160, 60, 160)
miner = Player("", 100, 160, 60, 160, 60)

#nodes
#ores
iron = Nodes("ore", "iron", 60, 60, 2, 1, "iron_ore")
copper = Nodes("ore", "copper", 50, 50, 1, 1, "copper_ore")
stone = Nodes("ore", "stone", 40, 40, 0, 1, "stone")
#wood
oak = Nodes("tree", "oak", 50, 50, 1, 1, "oak_wood")
chesnut = Nodes("tree", "chesnut", 30, 30, 0, 1, "chesnut_wood")

#tools
iron_pickaxe = Tools("pickaxe", "iron_pickaxe", 10, 5)
iron_axe = Tools("axe", "iron_axe", 10, 5)



#current_tool
command = ""
character = ""



def start_game():
    character = choose_character()
    current_tool = choose_tool()
    current_node = spawn_node()
    work(current_tool, current_node, character)


def mine(current_tool, current_node, character) :
    pass
    if current_tool.tool_type == "pickaxe" and character.mining_stamina > 0 and current_tool.breaking_power >= current_node.breaking_power:
        current_node.health -= current_tool.damage
        return node_destroyed(current_node, character)
    elif character.mining_stamina <= 0:
        print("You're out of stamina, try taking a quick rest")
    else:
        print("can't do that right now")
    return current_node, character


def chop(current_tool, current_node, character):
    pass
    if current_tool.tool_type == "axe" and character.logging_stamina > 0 and current_tool.breaking_power >= current_node.breaking_power:
        current_node.health -= current_tool.damage
        character.logging_stamina -= 10
        return node_destroyed(current_node, character)
    elif character.logging_stamina <= 0:
        print("You're out of stamina, try taking a quick rest")
    else:
        print("can't do that right now")
    return current_node, character


def node_destroyed(current_node, character):
    if current_node.health <= 0:
        collect_resource(current_node, character)
        current_node.health = current_node.max_health
        print(f"you broke {current_node.name} {current_node.node_type}")
        print("your walking to your next node")
        return spawn_node(), character
    else:
        print(f"{current_node.name} has {current_node.health} health left")
    return current_node, character



def collect_resource(current_node, character):
    if current_node.node_type == "ore" and current_node.health <= 0 and current_node.name in character.inventory:
        character.inventory[current_node.name] += 10
        print(f"you gained 10 {current_node.resource}")
        return character
    elif current_node.node_type == "tree" and current_node.health <= 0 and current_node.name in character.inventory:
        character.inventory[current_node.name] += 10
        return character
    else:
        print("go to collect_resource()")
    return character


def spawn_node():
    farmable = [iron, copper, stone, oak, chesnut]
    current_node = random.choice(farmable)
    print(f"you find a {current_node.name} node")
    return current_node



def text(current_tool):
    if current_tool.tool_type == "pickaxe":
        print("(mine)(rest)(inv)(swap)(home)")
    elif current_tool.tool_type == "axe":
        print("(chop)(rest)(inv)(swap)(home)")
    else:
        print("How did you obtain this")



#make it so i get food from trees, then can eat the food for stamina, return back to eat()
def rest(character):
    if character.logging_stamina >= 0 or character.mining_stamina >= 0:
        character.logging_stamina = character.max_logging_stamina
        character.mining_stamina = character.max_mining_stamina
        print(f"you sit down and take a short nap, you now have {character.max_logging_stamina} logging stamina and {character.max_mining_stamina} mining stamina")
    else:
        print("You don't need to rest")


def access_inventory(current_tool, character):
    print(character.inventory)
    return character


def craft():
    pass



def choose_character():
    character = ""
    character = input("choose a character\n(lumberjack)(miner)\n")
    if character == "lumberjack":
        character = lumberjack
        return character
    elif character == "miner":
        character = miner
        return character
    else:
        print("you have to choose a character")
    return character



def choose_tool():
    tool = ""
    while tool != "exit":
        tool = input("choose a tool\n(axe)(pickaxe)\n")
        if tool == "pickaxe":
            current_tool = iron_pickaxe
            return current_tool
        elif tool == "axe":
            current_tool = iron_axe
            return current_tool
        elif tool == "exit":
            break
        else:
            print("choose a valid tool")
    return current_tool


def swap_tool(current_tool):
    if current_tool.tool_type == "axe":
        current_tool = iron_pickaxe
        print(f"You have equipped a {current_tool.tool_type}")
        return current_tool
    elif current_tool.tool_type == "pickaxe":
        current_tool = iron_axe
        print(f"You have equipped an {current_tool.tool_type}")
        return current_tool
    else:
        print("you dont have a tool equipped")



def work(current_tool, current_node, character):
    command = ""
    while command != "home":
        text(current_tool)
        #current_node = spawn_node() #FIX THIS IT RESETS THE ORE EVERYTIME
        command = input()
        if command in {"swap", "swap tool", "swaptool"}: #trying a different way other than spamming, or statements. "in" checks each value to see if one matches
            current_tool = swap_tool(current_tool)
        elif command == "mine":
            current_node, character = mine(current_tool, current_node, character)
        elif command == "chop":
            current_node, character = chop(current_tool, current_node, character)
        elif command == "rest":
            rest(character)
        elif command == "inv":
            access_inventory(current_tool, character)
        elif command == "home":
            print("Going Home!")
            break
        else:
            print("Invalid")

        




start_game()