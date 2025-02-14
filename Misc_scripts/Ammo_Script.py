
#goal of this is to make this again in c++
#make more guns, should be ez after the class system.
#add a player class, could make nested classes, might be harder.
#import random #rng backfire, addition
#add info for the class, do the amouint of bullets shot per time shoot(). makes it easier to impliment less elif statements and make the code more modular. this can be sick.
#add a way to store the current info for ammo in gun, like if i holster with 10 bullets it stays at 10 when i  get it back out

class Gun():
    def __init__(self, name, ammo, mag_size, burst, ammo_type):
        self.name = name
        self.ammo = ammo
        self.mag_size = mag_size
        self.burst = burst
        self.ammo_type = ammo_type

#uses active_gun, to see what gun is currently being used
revolver = Gun("revolver", 6, 6, 1, "bullets")
smg = Gun("smg", 30, 30, 3, "bullets")
shotgun = Gun("shotgun", 2, 2, 1, "shells")


empty = 0
command = ""


def start_game():
    active_gun = choose_gun()
    combat(active_gun)


def shoot(active_gun):
    if active_gun.ammo >= active_gun.burst:
        active_gun.ammo -= active_gun.burst
        print(f"Buddy: you shot me {active_gun.burst} times")
        print(f"you have {active_gun.ammo} {active_gun.ammo_type} left")
    else:
        print("Buddy: seems like you're outta ammo")
        reload(active_gun)


def gun_text(active_gun):
    if active_gun == revolver:
        print("(shoot) (reload) (fanning) (holster) (exit)\n")
    elif active_gun == smg:
        print("(shoot) (reload) (fullauto) (holster) (exit)\n")
    elif active_gun == shotgun:
        print("(shoot) (reload) (double) (holster) (exit)\n")
    else:
        print("???")


def bone_dye():
    pass


def full_auto(active_gun):
    if active_gun == smg and active_gun.ammo >= 9:
        active_gun.ammo -= 9
        print("Buddy: why'd you blast me")
        print(f"you have {active_gun.ammo} bullets left")
    elif active_gun != smg:
        print("wrong gun bud")
    else:
        print("not enough ammo")
        reload(active_gun)


def double_shot(active_gun):
    if active_gun == shotgun and active_gun.ammo > active_gun.burst:
        active_gun.ammo -= 2
        print("Buddy: both at once!?")
        print(f"you have {active_gun.ammo} bullets left")
    elif active_gun != shotgun:
        print("wrong gun bud")
    else:
        print("not enough ammo")
        reload(active_gun)


def fanning(active_gun):
    if active_gun == revolver and active_gun.ammo > 1:
        fired = active_gun.ammo
        print(f"Buddy: how did you shoot {fired} bullets at me so fast")
        active_gun.ammo = empty
        print(f"you have {active_gun.ammo} bullets left")
    elif active_gun != revolver:
        print("wrong gun bud")
    else:
        print("Buddy: seems like you're outta ammo")
        reload(active_gun)


def reload(active_gun):
    if active_gun.ammo != active_gun.mag_size:
        loaded = active_gun.mag_size - active_gun.ammo
        active_gun.ammo = active_gun.mag_size
        print(f"you reloaded {loaded} {active_gun.ammo_type}")
    else:
        print("Buddy: You can't load a full mag")


def choose_gun():
    weapon = ""
    while weapon != "exit":
        weapon = input("choose a gun: (revolver), (smg), (shotgun).\n")

        if weapon == "revolver":
            active_gun = revolver
            print(f"you have {active_gun.mag_size} bullets")
            return active_gun

        elif weapon == "smg":
            active_gun = smg
            print(f"you have {active_gun.mag_size} bullets")
            return active_gun

        elif weapon == "shotgun":
            active_gun = shotgun
            print(f"you have {active_gun.mag_size} shells")
            return active_gun

        elif weapon == "exit":
            break
        else:
            print("Choose a gun first, or (exit)")
    return active_gun


def combat(active_gun):
    command = ""
    while command != "exit":
        gun_text(active_gun)
        command = input("")

        if command == "shoot":
            shoot(active_gun)
        elif command == "fanning" or command == "fan":
            fanning(active_gun)
        elif command == "reload":
            reload(active_gun)
        elif command == "fullauto" or command == "full auto":
            full_auto(active_gun)
        elif command == "double":
            double_shot(active_gun)
        elif command == "exit":
            print("Leaving the simulation")
            break
        elif command == "holster":
            active_gun = choose_gun()
        else:
            print("What did you say?")


start_game()
