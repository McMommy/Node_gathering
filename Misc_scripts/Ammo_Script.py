
#goal of this is to make this again in c++
#import random #rng backfire, addition

class Gun():
    def __init__(self, name, ammo, mag_size):
        self.name = name
        self.ammo = ammo
        self.mag_size = mag_size

revolver = Gun("revolver", 6, 6)
smg = Gun("smg", 30, 30)
shotgun = Gun("shotgun", 2, 2)


empty = 0
command = ""
gun = ""


def start_game():
    mag_size = choose_gun()
    combat(mag_size)


def shoot(mag_size):
    global ammo
    global gun
    if gun == "revolver" and ammo > empty:
        print()
        print("Buddy: ow, you shot me")
        ammo -= 1
        print(f"you have {ammo} bullets left")

    elif gun == "smg" and ammo > empty:
        print("Buddy: ow, you shot me")
        ammo -= 3
        print(f"you have {ammo} bullets left")

    elif gun == "shotgun" and ammo > empty:
        print("Buddy: ow, you shot me")
        ammo -= 1
        print(f"you have {ammo} shells left")
    else:
        print("Buddy: seems like you're outta ammo")
        reload(mag_size)


def gun_text():
    global gun
    if gun == "revolver":
        print("(shoot) (reload) (fanning) (holster) (exit)\n")
    elif gun == "smg":
        print("(shoot) (reload) (fullauto) (holster) (exit)\n")
    elif gun == "shotgun":
        print("(shoot) (reload) (double) (holster) (exit)\n")
    else:
        print("???")


def bone_dye():
    pass


def full_auto(mag_size):
    global ammo
    global gun
    if gun == "smg" and ammo >= 10:
        ammo -= 9
        print("Buddy: why'd you blast me")
        print(f"you have {ammo} bullets left")

    elif gun != "smg":
        print("wrong gun bud")
    else:
        print("not enough ammo")
        reload(mag_size)


def double_shot(mag_size):
    global ammo
    global gun
    if gun == "shotgun" and ammo >= 2:
        ammo -= 2
        print("Buddy: stop shooting so fast")
        print(f"you have {ammo} bullets left")
    elif gun != "shotgun":
        print("wrong gun bud")
    else:
        print("not enough ammo")
        reload(mag_size)


def fanning(mag_size):
    global ammo
    global gun
    if gun == "revolver" and ammo > 1:
        fired = ammo
        print(f"Buddy: how did you shoot {fired} bullets at me so fast")
        ammo = empty
        print(f"you have {ammo} bullets left")

    elif gun != "revolver":
        print("wrong gun bud")
    else:
        print("Buddy: seems like you're outta ammo")
        reload(mag_size)


def reload(mag_size):
    global ammo
    global gun
    if gun == "revolver" and ammo != mag_size:
        loaded = mag_size - ammo
        ammo = mag_size
        print(f"you reloaded {loaded} bullets")

    elif gun == "smg" and ammo != mag_size:
        loaded = mag_size - ammo
        ammo = mag_size
        print(f"you reloaded {loaded} bullets")

    elif gun == "shotgun" and ammo != mag_size:
        loaded = mag_size - ammo
        ammo = mag_size
        print(f"you reloaded {loaded} shells")
    else:
        print("erm sigma gun's full")


def choose_gun():
    global ammo
    global gun
    gun = ""
    while gun != "exit":
        gun = input("choose a gun: (revolver), (smg), (shotgun).\n")

        if gun == "revolver":
            mag_size = 6
            ammo = 6
            print(f"you have {mag_size} bullets")
            return mag_size

        elif gun == "smg":
            mag_size = 30
            ammo = 30
            print(f"you have {mag_size} bullets")
            return mag_size

        elif gun == "shotgun":
            mag_size = 2
            ammo = 2
            print(f"you have {mag_size} shells")
            return mag_size

        elif gun == "exit":
            break
        else:
            print("Choose a gun first, or (exit)")
    return mag_size


def combat(mag_size):
    global ammo
    global gun
    command = ""
    while command != "exit":
        gun_text()
        command = input("")

        if command == "shoot":
            shoot(mag_size)
        elif command == "fanning":
            fanning(mag_size)
        elif command == "reload":
            reload(mag_size)
        elif command == "fullauto":
            full_auto(mag_size)
        elif command == "double":
            double_shot(mag_size)
        elif command == "exit":
            print("Leaving the simulation")
            break
        elif command == "holster":
            mag_size = choose_gun()
        else:
            print("What did you say?")


start_game()
