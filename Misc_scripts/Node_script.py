#creating the mining system that ethan wanted
#fixing git


import time
import random


class Player():
    def __init__(self, name, health, stamina, max_stamina):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.max_stamina = max_stamina
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
player1 = Player("name", 100, 100, 100)

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




def start_game():
    current_tool = choose_tool()
    current_node = spawn_node()
    work(current_tool, current_node)


def mine(current_tool, current_node) :
    pass
    if current_tool.tool_type == "pickaxe" and player1.stamina > 0 and current_tool.breaking_power >= current_node.breaking_power:
        current_node.health -= current_tool.damage
        node_destroyed(current_node)
    #elif player1.stamina <= 0:
        #print("You're out of stamina, try taking a quick rest")
    else:
        print("can't do that right now")
def chop(current_tool, current_node):
    pass
    if current_tool.tool_type == "axe" and player1.stamina > 0 and current_tool.breaking_power >= current_node.breaking_power:
        current_node.health -= current_tool.damage
        player1.stamina -= 10
        node_destroyed(current_node)
    #elif player1.stamina <= 0:
        #print("You're out of stamina, try taking a quick rest")
    else:
        print("can't do that right now")


def node_destroyed(current_node):
    if current_node.health <= 0:
        collect_resource(current_node)
        current_node.health = current_node.max_health
        print(f"you broke {current_node.name} {current_node.node_type}")
        print("your walking to your next node")
        current_node = spawn_node()
    else:
        print(f"{current_node.name} has {current_node.health} health left")




def collect_resource(current_node):
    if current_node.node_type == "ore" and current_node.health <= 0 and current_node.name in player1.inventory:
        player1.inventory[current_node.name] += 10
        print(f"you gained 10 {current_node.resource}")
    elif current_node.node_type == "tree" and current_node.health <= 0 and current_node.name in player1.inventory:
        player1.inventory[current_node.name] += 10
    else:
        print("go to collect_resource()")


def spawn_node():
    farmable = [iron, copper, stone, oak, chesnut]
    current_node = random.choice(farmable)
    print(f"you find a {current_node.name} node")
    return current_node


def node_info():
    pass



def text(current_tool):
    if current_tool.tool_type == "pickaxe":
        print("(mine)(rest)(inv)(swap)(home)")
    elif current_tool.tool_type == "axe":
        print("(chop)(rest)(inv)(swap)(home)")
    else:
        print("How did you obtain this")


def choose_name():
    pass


#make it so i get food from trees, then can eat the food for stamina, return back to eat()
def rest():
    if player1.stamina >= 0:
        print("you sit down and take a short nap")
        gained = player1.max_stamina - player1.stamina
        player1.stamina = 100
        print(f"you gained {gained} stamina")
    else:
        print("You're not tired")


def access_inventory(current_tool):
    print(player1.inventory)


def craft():
    pass

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



def work(current_tool, current_node):
    command = ""
    while command != "home" or command != "exit":
        text(current_tool)
        #current_node = spawn_node() #FIX THIS IT RESETS THE ORE EVERYTIME
        command = input()
        if command in {"swap", "swap tool", "swaptool"}: #tring a different way other than spamming, or statements. "in" checks each value to see if one matches
            current_tool = swap_tool(current_tool)
        elif command == "mine":
            mine(current_tool, current_node)
        elif command == "chop":
            chop(current_tool, current_node)
        elif command == "rest":
            rest()
        elif command == "inv":
            access_inventory(current_tool)
        elif command == "home":
            print("Going Home!")
            break
        else:
            print("Invalid")

        




start_game()