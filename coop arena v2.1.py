#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     07/06/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

boss = 'a'
while boss != '1' and boss != '2':
	boss = input('Selct boss fight:\n-1: Ogre\n-2: spectral king\n')
if boss == '1':
	boss = 'ogre'
elif boss == '2':
	boss = 'spec_king'
print ('\n\n\n')


#setup
import random, time, sys

Game_over = False
pl1_bat_count = 0
pl2_bat_count = 0
pl1_curse_count = 0
pl2_curse_count = 0
boss_move = 'dh'
roar = False
cloak_count = 0
player_1 ='a'
player_2 = 'b'
pl1_drk_orb_dmg = 0
pl2_drk_orb_dmg = 0


#character selection
while player_1 != '1' and player_1 != '2' and player_1 != '3' and player_1 != '4':
    player_1 = input('Player 1, Which character would you like to be:\n-1:paladin\n-2:mage\n-3:vampire\n-4:guardian\n')
    print ('\n')
while player_2 != '1' and player_2 != '2'and player_2 != '3' and player_2 != '4':
	player_2 = input('Player 2, Which character would you like to be:\n-1:paladin\n-2:mage\n-3:vampire\n-4:guardian\n')
	print ('\n')


if player_1 == '1':
    pl1_char = 'paladin'
    pl1_health = 100
    pl1_defense = 15
    pl1_mv1 = 'greatsword'
    pl1_mv1_dmg = 35
    pl1_mv2 = 'war hammer: will break your opponents armour'
    pl1_mv2_dmg = 25
    pl1_mv2_efct = 'armr_brk'
    pl1_mv3 = 'armr_repair'
    pl1_mv3_nme = 'armour repair'

elif player_1 == '2':
    pl1_char = 'mage'
    pl1_health = 100
    pl1_defense = 5
    pl1_mv1 = 'fireball'
    pl1_mv1_dmg = 45
    pl1_mv2 = 'cursed beam: will inflict a curse onto your opponent'
    pl1_mv2_dmg = 35
    pl1_mv2_efct = 'curse'
    pl1_mv3 = 'heal'
    pl1_mv3_nme = 'heal'

elif player_1 == '3':
    pl1_char = 'vampire'
    pl1_health = 100
    pl1_defense = 10
    pl1_mv1 = 'sacrificial warblade'
    pl1_mv1_dmg = 55
    pl1_mv2 = 'blood knife: a knife that steals the life from your  opponent'
    pl1_mv2_dmg = 30
    pl1_mv2_efct = 'life steal'
    pl1_mv3 = 'blood shift'
    pl1_mv3_nme = 'blood shift: grants the ability to steal more life with your blood knife'

elif player_1 == '4':
    pl1_char = 'guardian'
    pl1_health = 100
    pl1_defense = 10
    pl1_mv1 = 'ultimate healing: Heals both you and your partner\n'
    pl1_mv1_dmg = 0
    pl1_mv2 = 'Shield replenish: Partly replenishes both you and your partners armour\n'
    pl1_mv2_dmg = 0
    pl1_mv2_efct = 'drk_orb'
    pl1_mv3 = 'dark_orb'
    pl1_mv3_nme = 'dark orb: Charges an orb that deals damage to the enemy but it slowly depletes'
    pl1_drk_orb_dmg = 0



if player_2 == '2':
    pl2_char = 'mage'
    pl2_health = 100
    pl2_defense = 5
    pl2_mv1 = 'fireball'
    pl2_mv1_dmg = 45
    pl2_mv2 = 'cursed beam: will inflict a curse onto your opponent'
    pl2_mv2_dmg = 35
    pl2_mv2_efct = 'curse'
    pl2_mv3 = 'heal'
    pl2_mv3_nme = 'heal'

elif player_2 == '1':
    pl2_char = 'paladin'
    pl2_health = 100
    pl2_defense = 15
    pl2_mv1 = 'greatsword'
    pl2_mv1_dmg = 35
    pl2_mv2 = 'war hammer: will break your opponents armour'
    pl2_mv2_dmg = 25
    pl2_mv2_efct = 'armr_brk'
    pl2_mv3 = 'armr_repair'
    pl2_mv3_nme = 'armour repair'

elif player_2 == '3':
    pl2_char = 'vampire'
    pl2_health = 100
    pl2_defense = 5
    pl2_mv1 = 'sacrificial warblade'
    pl2_mv1_dmg = 55
    pl2_mv2 = 'blood knife: a knife that steals the life from your  opponent'
    pl2_mv2_dmg = 30
    pl2_mv2_efct = 'life steal'
    pl2_mv3 = 'blood shift'
    pl2_mv3_nme = 'blood shift: grants the ability to steal more life with your blood knife'

elif player_2 == '4':
    pl2_char = 'guardian'
    pl2_health = 100
    pl2_defense = 10
    pl2_mv1 = 'ultimate healing: Heals you and your partner\n'
    pl2_mv1_dmg = 0
    pl2_mv2 = 'Shield replenish: Partly replenishes you and your partners armour, but weakens your dark orb\n'
    pl2_mv2_dmg = 0
    pl2_mv2_efct = 'drk_orb'
    pl2_mv3 = 'dark_orb'
    pl2_mv3_nme = 'dark orb: Charges an orb that deals damage to the enemy but it slowly depletes'
    pl2_drk_orb_dmg = 0

#boss

if boss == 'ogre':
    boss_health = 180
    boss_defense = 20
    boss_mv1 = 'club'
    boss_mv1_dmg = 35
    boss_mv2 = 'roar'
    boss_mv2_dmg = 20
    boss_mv3 = 'swamp elixir'
elif boss == 'spec_king':
    boss_health = 160
    boss_defense = 25
    boss_mv1 = 'dark scythe'
    boss_mv1_dmg = 45
    boss_mv2 = 'dual beam'
    boss_mv2_dmg = 25
    boss_mv3 = 'shadow cloak'


battle_pl1_1 = ('move1 = ' + pl1_mv1)
battle_pl1_2 = (', move2 = ' + pl1_mv2)
battle_pl1_3 = (', move3 = ' + pl1_mv3_nme + '\n')

battle_pl2_1 = ('move1 = ' + pl2_mv1)
battle_pl2_2 = (', move2 = ' + pl2_mv2)
battle_pl2_3 = (', move3 = ' + pl2_mv3_nme + '\n')

battle_plan_pl1_pt1 = (battle_pl1_1 + battle_pl1_2)
battle_plan_pl2_pt1 = (battle_pl2_1 + battle_pl2_2)

#fight
print ('\n')
while Game_over == False:

#boss move

    #choose target

    if pl1_health != 0 and pl2_health != 0:
        target = random.randint(1, 2)
    if pl1_health != 0 and pl2_health == 0:
        target = 1
    if pl1_health == 0 and pl2_health != 0:
        target = 2

	#attack target

    move = random.randint(1, 14)
    if target == 1:
        if move <= 8:# move1
            boss_move = boss_mv1
            dmg = boss_mv1_dmg
            dmg = dmg - pl1_defense
            if dmg < 0:
                dmg = 0
            pl1_health = pl1_health - dmg
        elif move <= 12:#move 2
            boss_move = boss_mv2
            dmg = boss_mv2_dmg
            if dmg < 0:
                dmg = 0
            dmg = dmg - pl1_defense
            pl1_health = pl1_health - dmg
            if boss == 'ogre':
                roar = True
            elif boss == 'spec_king':
                dmg = boss_mv2_dmg - pl1_defense
                if dmg < 0:
                    dmg = 0
                pl1_health -= dmg
        else:#move 3
            boss_move = boss_mv3
            if boss == 'ogre':
                boss_health = boss_health + 80
                if boss_health > 200:
                    boss_health = 200
            elif boss == 'spec_king':
                cloak_count = 2


    elif target == 2:
        if move <= 7:#move1
            boss_move = boss_mv1
            dmg = boss_mv1_dmg
            dmg = dmg - pl2_defense
            if dmg < 0:
                dmg = 0
            pl2_health = pl2_health - dmg
        elif move <= 10:#move2
            boss_move = boss_mv2
            dmg = boss_mv2_dmg
            dmg = dmg - pl2_defense
            if dmg < 0:
                dmg = 0
            pl2_health = pl2_health - dmg
            if boss == 'ogre':
                roar = True
            if boss == 'spec_king':
                dmg = boss_mv2_dmg - pl1_defense
                if dmg < 0:
                    dmg = 0
                pl1_health -= dmg


        else:#move3
            boss_move = boss_mv3
            if boss == 'ogre':
                boss_health = boss_health + 80
            if boss_health >= 200:
                boss_health = 200
            if boss == 'spec_king':
                cloak_count = 2

    print ('boss move =', boss_move)
    print ('boss target = player', target)


#player 1 move
    mv_choice = 'a'

    if pl1_health != 0:
        while mv_choice != '1' and mv_choice != '2' and mv_choice != '3':
            print (battle_pl1_1 + battle_pl1_2 + battle_pl1_3)
            mv_choice = input('Player 1 make your move, enter either 1, 2 or 3.  ')

        if mv_choice == '1':
            dmg = (pl1_mv1_dmg + pl1_drk_orb_dmg) - boss_defense
            if pl1_curse_count:
                dmg = dmg + 10
            if roar == True:
                dmg = dmg - 5
            if cloak_count:
                dmg = 0
            boss_health = boss_health - dmg
            if dmg < 0:
                dmg = 0
            if pl1_char == 'vampire':
                pl1_health = pl1_health - 10
            if pl1_char == 'guardian':
                pl1_health += 5
                pl2_health += 15

        if mv_choice == '2':
            dmg = (pl1_mv2_dmg + pl1_drk_orb_dmg) - boss_defense
            if pl1_curse_count:
                dmg = dmg + 5
            if roar == True:
                dmg = dmg - 5
            if cloak_count:
                dmg = 0
            boss_health = boss_health - dmg
            if dmg < 0:
                dmg = 0
            if pl1_mv2_efct == 'armr_brk':
                boss_defense = boss_defense - 5
                if boss_defense <= 1:
                    boss_defense = 0
            elif pl1_mv2_efct == 'curse':
                pl1_curse_count = 3
            elif pl1_mv2_efct == 'life steal':
                if pl1_bat_count == True:
                    pl1_health += 25
                else:
                    pl1_health += 15
            elif pl1_char == 'guardian':
                pl1_defense += 5
                pl2_defense += 5
                pl1_drk_orb_dmg -= 5
                if pl1_drk_orb_dmg < 0:
                    pl1_drk_orb_dmg = 0

        if mv_choice == '3':
            if pl1_mv3 == 'armr_repair':
                pl1_defense += 5
            elif pl1_mv3 == 'heal':
                if pl1_curse_count:
                    dmg = 5
                    boss_health = boss_health - dmg
                pl1_health = pl1_health + 20
            elif pl1_mv3 == 'blood shift':
                pl1_bat_count = 3
            elif pl1_char == 'guardian':
                pl1_drk_orb_dmg += 15
                pl1_health -= 10
                if pl1_drk_orb_dmg > 40:
                    pl1_drk_orb_dmg = 40
                dmg = pl1_drk_orb_dmg - boss_defense
                boss_health -= dmg

#player2 move

    mv_choice = 1

    if pl2_health != 0:
        while mv_choice != '1' and mv_choice != '2' and mv_choice != '3':
            print (battle_pl2_1 + battle_pl2_2 + battle_pl2_3)
            mv_choice = input('Player 2 make your move, enter either 1, 2 or 3.  ')

        if mv_choice == '1':
            dmg = (pl2_mv1_dmg + pl2_drk_orb_dmg) - boss_defense
        if dmg < 0:
            dmg = 0
            if pl2_curse_count:
                dmg += 5
            if roar == True:
                dmg -= 5
            if pl2_char == 'vampire':
                pl2_health = pl2_health - 10
            if cloak_count:
                dmg = 0
            boss_health = boss_health - dmg
            if pl2_char == 'guardian':
                pl2_health += 5
                pl1_health += 15

        if mv_choice == '2':
            dmg = (pl2_mv2_dmg + pl2_drk_orb_dmg) - boss_defense
            if pl2_curse_count:
                dmg += 5
            if roar == True:
                dmg -= 5
            if cloak_count:
                dmg = 0
            boss_health = boss_health - dmg
            if dmg < 0:
                dmg = 0
            if pl2_mv2_efct == 'armr_brk':
                boss_defense = boss_defense - 5
                if boss_defense <= 1:
                    boss_defense = 0
            elif pl2_mv2_efct == 'curse':
                pl2_curse = True
                pl2_curse_count = 3
            elif pl2_mv2_efct == 'life steal':
                if pl2_bat_count == True:
                    pl2_health += 20
                else:
                    pl2_health += 15
            elif pl2_char == 'guardian':
                pl2_defense += 5
                pl1_defense += 5
                pl2_drk_orb_dmg -= 5
                if pl2_drk_orb_dmg < 0:
                    pl2_drk_orb_dmg = 0

        if mv_choice == '3':
            if pl2_mv3 == 'armr_repair':
                pl2_defense += 5
            elif pl2_mv3 == 'heal':
                if pl2_curse_count:
                    dmg = 5
                boss_health = boss_health - dmg
                pl2_health = pl2_health + 25
            elif pl2_mv3 == 'blood shift':
                pl2_bat_count = 3
            elif pl2_char == 'guardian':
                pl2_drk_orb_dmg += 15
                pl2_health -= 10
                if pl2_drk_orb_dmg > 40:
                    pl2_drk_orb_dmg = 40
                dmg = pl2_drk_orb_dmg - boss_defense
                boss_health -= dmg
#summary

    if boss_health <= 1:
        boss_health = 0
    if boss_defense >= 50:
        boss_defense = 50
    if boss_health >= 250:
        boss_health = 250

    if pl1_health < 1:
        pl1_health = 0
    if pl1_defense > 25:
        pl1_defense = 25
    if pl1_health > 125:
        pl1_health = 125

    if pl2_health < 1:
        pl2_health = 0
    if pl2_defense > 25:
        pl2_defense = 25
    if pl2_health > 125:
        pl2_health = 125


    print ('\n\nboss health = ' + str(boss_health) + '    boss defense = ' + str(boss_defense))
    print ('player 1 health = ' + str(pl1_health) + '    player 1 defense = ' + str(pl1_defense))
    print ('player 2 health = ' + str(pl2_health) + '    player 2 defense = ' + str(pl2_defense))

    if pl1_char == 'guardian':
        print("player 1's dark orb charge =", pl1_drk_orb_dmg)


    if pl2_char == 'guardian':
        print("player 2's dark orb charge =", pl2_drk_orb_dmg)

    if pl1_curse_count:
        pl1_curse_count -= 1
        if pl1_curse_count < 1:
            print("Player 1's curse has EXPIRED")
        else:
            print("Player 1's curse is ACTIVE")

    if pl2_curse_count:
        pl2_curse_count -= 1
        if pl2_curse_count < 1:
            print("Player 2's curse has EXPIRED")
        else:
            print("Player 2's curse is ACTIVE")

    if pl1_bat_count:
        pl1_bat_count -= 1
        if pl1_bat_count < 1:
            print("Player 1's blood shift mode has EXPIRED")
        else:
            print("Player 1's blood shift mode is ACTIVE")

    if pl2_bat_count:
        pl2_bat_count -= 1
        if pl2_bat_count < 1:
            print("Player 2's blood shift mode has EXPIRED")
        else:
            print("Player 2's blood shift mode is ACTIVE")

    if pl1_drk_orb_dmg:
        pl1_drk_orb_dmg -= 5
        if pl1_drk_orb_dmg < 0:
            pl1_drk_orb_dmg = 0

    if pl2_drk_orb_dmg:
        pl2_drk_orb_dmg -= 5
        if pl2_drk_orb_dmg < 0:
            pl2_drk_orb_dmg = 0

    if cloak_count:
        cloak_count -= 1
        if cloak_count == 0:
            print("The Spectral King's shadow cloak has worn off")

    if pl1_health == 0 and pl2_health == 0:
        Game_over = True
    if boss_health == 0:
        Game_over = True


#win/lose
if boss_health == 0 and pl1_health == 0 and pl2_health != 0:
    print ('\n\nYou win, but sadly player 1 died.')
elif boss_health == 0 and pl2_health == 0 and pl1_health != 0:
    print ('\n\nYou win but sadly player 2 died.')
elif boss_health == 0 :
    print ('\n\nYou win!')
elif pl1_health == 0 and pl2_health == 0 and boss_health != 0:
    print ('\n\nYou lose...')
elif boss_health == 0 and pl1_health == 0 and pl2_health == 0:
    print ('\n\ndraw')

try:
    if sys.stdout.isatty(): #if run in terminal
        mode = 1
except:
    mode = 0

if mode == 1: #if in terminal sleep so window does not dissapear
    while True:
        time.sleep(1)
else:
    pass
