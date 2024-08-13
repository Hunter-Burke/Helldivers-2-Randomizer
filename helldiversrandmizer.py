from random import choice
from time import sleep
import os

def generate_random_loadout():
  gun = [
    "AR-23 Liberator", "AR-23P Liberator Penetrator", "AR-23C Liberator Concussive", "R-63 Diligence", "R-63CS Diligence Counter Sniper", "SMG-37 Defender", "SG-8 Punisher", "SG-8S Slugger", "SG-451 Cookout", "SG-225 Breaker", "SG-225SP Breaker Spray&Pray", "SG-225IE Breaker Incendiary", "LAS-5 Scythe", "LAS-16 Sickle", "PLAS-1 Scorcher"]
  gun2 = [
    "P-2 Peacemaker", "P-19 Redeemer", "P-4 Senator"]
  grenade = [
    "G-6 Frag", "G-12 High Explosive", "G-10 Incendiary", "G-16 Impact", "G-3 Smoke"]
  armor_passive = [
    "Scout", "Servo-Assisted", "Engineering Kit", "Med-Kit", "Fortified", "Democracy Protects", "Extra Padding", "Peak Physique"]
  stratagem_1 = [
    "Machine Gun", "Anti-Materiel Rifle", "Stalwart", "Expendable Anti-Tank", "Recoilless Rifle", "Flamethrower", "Autocannon", "Heavy Machine Gun", "Airburst Rocket Launcher", "Commando", "Railgun", "Spear", "Orbital Gatling Barrage", "Orbital Airburst Strike", "Orbital 120MM HE Barrage", "Orbital 380MM HE Barrage", "Orbital Waling Barrage", "Orbital Laser", "Orbital Railcannon Strike", "Eagle Strafing Run", "Eagle Airstrike", "Eagle Cluster Bomb", "Eagle Napalm Airstrike", "Eagle 110MM Rocket Pods", "Eagle 500KG Bomb", "Orbital Precision Strike", "Orbital Gas Strike", "Orbital EMS Strike", "Orbital Smoke Strike", "HMG Emplacement", "Shield Generator Relay", "Tesla Tower", "Anti-Personnel Minefield", "Supply Pack", "Grenade Launcher", "Laser Cannon", "Incendiary Mines", "\"Guard Dog\" Rover", "Ballistic Shield Backpack", "Arc Thrower", "Anti-Tank Mines", "Quasar Cannon", "Shield Generator Pack", "Machine Gun Sentry", "Gatling Sentry", "Mortar Sentry", "\"Guard Dog\"", "Autocannon Sentry", "Rocket Sentry", "EMS Mortar Sentry", "Patriot Exosuit", "Emancipator Exosuit"]
  stratagem_2 = [
    "Machine Gun", "Anti-Materiel Rifle", "Stalwart", "Expendable Anti-Tank", "Recoilless Rifle", "Flamethrower", "Autocannon", "Heavy Machine Gun", "Airburst Rocket Launcher", "Commando", "Railgun", "Spear", "Orbital Gatling Barrage", "Orbital Airburst Strike", "Orbital 120MM HE Barrage", "Orbital 380MM HE Barrage", "Orbital Waling Barrage", "Orbital Laser", "Orbital Railcannon Strike", "Eagle Strafing Run", "Eagle Airstrike", "Eagle Cluster Bomb", "Eagle Napalm Airstrike", "Eagle 110MM Rocket Pods", "Eagle 500KG Bomb", "Orbital Precision Strike", "Orbital Gas Strike", "Orbital EMS Strike", "Orbital Smoke Strike", "HMG Emplacement", "Shield Generator Relay", "Tesla Tower", "Anti-Personnel Minefield", "Supply Pack", "Grenade Launcher", "Laser Cannon", "Incendiary Mines", "\"Guard Dog\" Rover", "Ballistic Shield Backpack", "Arc Thrower", "Anti-Tank Mines", "Quasar Cannon", "Shield Generator Pack", "Machine Gun Sentry", "Gatling Sentry", "Mortar Sentry", "\"Guard Dog\"", "Autocannon Sentry", "Rocket Sentry", "EMS Mortar Sentry", "Patriot Exosuit", "Emancipator Exosuit"]
  stratagem_3 = [
    "Machine Gun", "Anti-Materiel Rifle", "Stalwart", "Expendable Anti-Tank", "Recoilless Rifle", "Flamethrower", "Autocannon", "Heavy Machine Gun", "Airburst Rocket Launcher", "Commando", "Railgun", "Spear", "Orbital Gatling Barrage", "Orbital Airburst Strike", "Orbital 120MM HE Barrage", "Orbital 380MM HE Barrage", "Orbital Waling Barrage", "Orbital Laser", "Orbital Railcannon Strike", "Eagle Strafing Run", "Eagle Airstrike", "Eagle Cluster Bomb", "Eagle Napalm Airstrike", "Eagle 110MM Rocket Pods", "Eagle 500KG Bomb", "Orbital Precision Strike", "Orbital Gas Strike", "Orbital EMS Strike", "Orbital Smoke Strike", "HMG Emplacement", "Shield Generator Relay", "Tesla Tower", "Anti-Personnel Minefield", "Supply Pack", "Grenade Launcher", "Laser Cannon", "Incendiary Mines", "\"Guard Dog\" Rover", "Ballistic Shield Backpack", "Arc Thrower", "Anti-Tank Mines", "Quasar Cannon", "Shield Generator Pack", "Machine Gun Sentry", "Gatling Sentry", "Mortar Sentry", "\"Guard Dog\"", "Autocannon Sentry", "Rocket Sentry", "EMS Mortar Sentry", "Patriot Exosuit", "Emancipator Exosuit"]
  stratagem_4 = [
    "Machine Gun", "Anti-Materiel Rifle", "Stalwart", "Expendable Anti-Tank", "Recoilless Rifle", "Flamethrower", "Autocannon", "Heavy Machine Gun", "Airburst Rocket Launcher", "Commando", "Railgun", "Spear", "Orbital Gatling Barrage", "Orbital Airburst Strike", "Orbital 120MM HE Barrage", "Orbital 380MM HE Barrage", "Orbital Waling Barrage", "Orbital Laser", "Orbital Railcannon Strike", "Eagle Strafing Run", "Eagle Airstrike", "Eagle Cluster Bomb", "Eagle Napalm Airstrike", "Eagle 110MM Rocket Pods", "Eagle 500KG Bomb", "Orbital Precision Strike", "Orbital Gas Strike", "Orbital EMS Strike", "Orbital Smoke Strike", "HMG Emplacement", "Shield Generator Relay", "Tesla Tower", "Anti-Personnel Minefield", "Supply Pack", "Grenade Launcher", "Laser Cannon", "Incendiary Mines", "\"Guard Dog\" Rover", "Ballistic Shield Backpack", "Arc Thrower", "Anti-Tank Mines", "Quasar Cannon", "Shield Generator Pack", "Machine Gun Sentry", "Gatling Sentry", "Mortar Sentry", "\"Guard Dog\"", "Autocannon Sentry", "Rocket Sentry", "EMS Mortar Sentry", "Patriot Exosuit", "Emancipator Exosuit"]
  booster = [
    "Vitality Enhancement", "Stamina Enhancement", "Muscle Enhancement", "UAV Recon Booster", "Increased Reinforcement Budget", "Hellpod Space Optimization", "Flexible Reinforcement Budget"]
  return "Primary: " + choice(gun) + "\nSecondary: " + choice(gun2) + "\nThrowable: " + choice(grenade) + "\nArmor Passive: " + choice(armor_passive) + "\nStratagem One: " + choice(stratagem_1) + "\nStratagem Two: " + choice(stratagem_2) + "\nStratagem Three: " + choice(stratagem_3) + "\nStratagem Four: " + choice(stratagem_4) + "\nBooster: " + choice(booster)
print("How many loadouts do you want to generate?\n")
num_of_loadouts = input("> ")
print("")
if num_of_loadouts == "infinite":
  sleep(0.5)
  print("Hehe...")
  sleep(3)
  while True:
    print(f"{generate_random_loadout()}")
    print(" ")
else:
  for i in range(int(num_of_loadouts.strip())):
    print(f"{generate_random_loadout()}")
    os.system('pause')
    print(" ")
