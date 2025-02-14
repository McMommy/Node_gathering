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
        self.inventory = {}


class Nodes():
    def __init__(self, name, health, breaking_power, spawn_chance):
        self.name = name
        self.health = health
        self.breaking_power = breaking_power
        self.spawn_chance = spawn_chance


class Tools():
    def __init__(self, tool_type, name, damage, breakingpower,):
        self.tool_type = tool_type
        self.name = name
        self.damage = damage
        self.breakingpower = breakingpower

#player
player1 = Player("name", 100, 100, 100)

#nodes
#ores
iron = Nodes("iron", 60, 2, 1)
copper = Nodes("copper", 50, 1, 1)
stone = Nodes("stone", 40, 0, 1)
#wood
oak = Nodes("oak", 50, 1, 1)
chesnut = Nodes("chesnut", 30, 0, 1)

#tools
iron_pickaxe = Tools("pickaxe", "iron_pickaxe", 10, 5)
iron_axe = Tools("axe", "iron_axe", 10, 5)



#current_tool
command = ""




def start_game():
    current_tool = choose_tool()
    work(current_tool)


def mine(current_tool):
    pass
   # if current_tool.tool_type == "pickaxe" and current_tool.breaking_power >= current_node.breaking_power:
      #  current_node.health -= current_tool.damage


def chop(current_tool):
    pass
    #if current_tool.tool_type == "axe" and current_tool.breaking_power >= :
     #   current_node.health -= current_tool.damage


def node_info():
    pass


def text(current_tool):
    if current_tool.tool_type == "pickaxe":
        print("(mine)(rest)(inv)(swap)(home)")
    elif current_tool.tool_type == "axe":
        print("(chop)(rest)(inv)(swap)(home)")
    else:
        print("How did you obtain this")


#make it so i get food from trees, then can eat the food for stamina, return back to eat()
def rest():
    pass
    if player1.stamina >= 0:
        print("you sit down and take a short nap")
        gained = player1.max_stamina - player1.stamina
        player1.stamina = 100
        print(f"you gained {gained} stamina")
    else:
        print("You're not tired")


def access_inventory(current_tool):
    print(player1.inventory)


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



def work(current_tool):
    command = ""
    while command != "home" or command != "exit":
        text(current_tool)
        command = input()
        if command == "swap" or command == "swap tool" or command == "swaptool":
            current_tool = swap_tool(current_tool)
        elif command == "mine":
            mine(current_tool)
        elif command == "chop":
            chop(current_tool)
        elif command == "rest":
            rest()
        elif command == "inv" or command == "inventory":
            access_inventory(current_tool)
        elif command == "home" or command == "exit":
            print("Going Home!")
            break
        else:
            print("Invalid")

        



start_game()