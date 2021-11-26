import main as db
import Attributes

def default_info(info, discord_id):
  return  "**"+str(info["display_name"]) + ":**\n" + \
          "Pantheon: " + str(db.get_pantheon_name(info["pantheon"])) + "\n" + \
          "Soldiers: " + str(db.get_army(discord_id)) + "\n"+\
          "Functionaries: " + str(db.get_attribute(discord_id,Attributes.FUNCTIONARIES)) + "\n"+ \
          "Priests: " + str(db.get_attribute(discord_id,Attributes.PRIESTS)) + "\n\n"+ \
          "**Battle statistics:**\n" + \
          "Attack: " + str(db.get_attribute(discord_id,Attributes.ATTACK)) + "\n" + \
          "Defense: " + str(db.get_attribute(discord_id, Attributes.DEFENSE)) + "\n" + \
          "Armor: " + str(db.get_attribute(discord_id, Attributes.ARMOR)) + "\n" + \
          "Initiative: " + str(db.get_attribute(discord_id, Attributes.INITIATIVE)) + "\n\n" + \
          "**Power:**\n" + \
          "Current DP: " + str(db.get_attribute(discord_id,Attributes.POWER)) + "\n"\
          "Income: " + str(db.calculate_income(discord_id)) + "\n"\
          "Remaining Priest Channeling Power: " + str(db.get_attribute(discord_id,Attributes.TOTAL_PRIEST_POWER))

def income_info(info, discord_id):
  return  "**" + str(info["display_name"]) + "\'s income:**\n" + \
          "Total DP: " + str(int(db.get_attribute(discord_id, Attributes.POWER))) + "\n\n" \
          "Income per functional: " + str(db.get_attribute(discord_id,Attributes.INCOME_PER_FUNCTIONAL)) + "\n"\
          "Income per soldier: " + str(db.get_attribute(discord_id, Attributes.INCOME_PER_SOLDIER)) + "\n"\
          "Income per priest: " + str(db.get_attribute(discord_id, Attributes.INCOME_PER_PRIEST)) + "\n"\
          "Base income per turn: " + str(db.get_attribute(discord_id,Attributes.INCOME_PER_FUNCTIONAL)+
                                          db.get_attribute(discord_id, Attributes.INCOME_PER_SOLDIER)+
                                          db.get_attribute(discord_id, Attributes.INCOME_PER_PRIEST))+"\n\n"\
          "Bonus income per functional: " + str(db.get_attribute(discord_id, Attributes.BONUS_POWER_PER_FUNCTIONAL)) + "\n"\
          "Bonus income per soldier: " + str(db.get_attribute(discord_id, Attributes.BONUS_POWER_PER_SOLDIER)) + "\n"\
          "Bonus income per priest: " + str(db.get_attribute(discord_id, Attributes.BONUS_POWER_PER_PRIEST)) + "\n"\
          "Priest income boost: " + str(db.get_attribute(discord_id, Attributes.PRIEST_INCOME_BOOST_RATE)) + \
          " DP for every unit of bonus income, up to a maximum of " + \
          str(db.get_attribute(discord_id,Attributes.PRIEST_INCOME_BOOST_CAPACITY)) + " per priest, or " + \
          str(db.get_attribute(discord_id,Attributes.PRIESTS)* db.get_attribute(discord_id,Attributes.PRIEST_INCOME_BOOST_CAPACITY)) + " total.\n\n" +\
          "Total income per turn: " + str(int(db.calculate_income(discord_id))) + "\n\n" + \
          "Passive population growth rate: " + str(db.get_attribute(discord_id,Attributes.PASSIVE_POPULATION_GROWTH_RATE)*100) + "%/turn"

def war_info(info, discord_id):
  return  "**{name}'s army:**\n" \
          "Soldiers: {soldiers} \n" \
          "Available attackers: {attackers} \n" \
          "Attacks per soldier per turn: {attacks_per_turn} \n\n" \
          "Attack: {attack} \n" \
          "Defense: {defense} \n" \
          "Armor: {armor} \n" \
          "Initiative: {initiative}\n\n"\
          "Soldier cost: {soldier_cost}\n"\
          "Soldier disband cost: {soldier_disband_cost}\n\n"\
          "Functionary defense: {functionary_defense}\n"\
          "Functionary armor: {functionary_armor}\n"\
          .format(
              name=info["display_name"],
              soldiers= int(db.get_attribute(discord_id,Attributes.SOLDIERS)),
              attackers=int(db.get_attribute(discord_id,Attributes.ATTACK_ELIGIBLE_SOLDIERS)),
              attacks_per_turn=db.get_attribute(discord_id,Attributes.ATTACKS_PER_TURN),
              attack=db.get_attribute(discord_id,Attributes.ATTACK),
              defense=db.get_attribute(discord_id, Attributes.DEFENSE),
              armor=db.get_attribute(discord_id,Attributes.ARMOR),
              initiative=db.get_attribute(discord_id,Attributes.INITIATIVE),
              soldier_cost=int(db.get_attribute(discord_id,Attributes.SOLDIER_COST)),
              soldier_disband_cost=int(db.get_attribute(discord_id,Attributes.SOLDIER_DISBAND_COST)),
              functionary_defense=db.get_attribute(discord_id,Attributes.FUNCTIONARY_DEFENSE),
              functionary_armor=db.get_attribute(discord_id,Attributes.FUNCTIONARY_ARMOR)
          )


def conversion_info(info, discord_id):
  return  "**{name}'s conversion metrics:**\n" \
          "Enemy follower conversion: {enemy_rate:.1%}, {enemy_cost} DP \n" \
          "Enemy priest conversion: {priest_convert_rate:.1%}, {priest_convert_cost} DP \n" \
          "Neutral conversion: {neutral_rate:.1%}, {neutral_cost} DP \n\n" \
          "Priest cost: {priest_cost} \n" \
          "Max priest channeling per turn: {channeling} \n".format(
            name=info["display_name"],
            enemy_rate=int(db.get_attribute(discord_id, Attributes.ENEMY_CONVERSION_RATE)),
            enemy_cost=int(db.get_attribute(discord_id, Attributes.ENEMY_CONVERSION_COST)),
            priest_convert_rate=db.get_attribute(discord_id, Attributes.ENEMY_PRIEST_CONVERSION_RATE),
            priest_convert_cost=db.get_attribute(discord_id, Attributes.ENEMY_PRIEST_CONVERSION_COST),
            neutral_rate=db.get_attribute(discord_id, Attributes.NEUTRAL_CONVERSION_RATE),
            neutral_cost=db.get_attribute(discord_id, Attributes.NEUTRAL_CONVERSION_COST),
            priest_cost=db.get_attribute(discord_id, Attributes.PRIEST_COST),
            channeling=int(db.get_attribute(discord_id, Attributes.MAXIMUM_PRIEST_CHANNELING))
        )


def research_info(info, discord_id):
  return  "**{name}'s research metrics:**\n" \
          "Divine inspiration: {inspiration_rate:.1%}, {inspiration_cost} DP/attempt \n" \
          "Revelation (asleep): {asleep_rate:.1%}, {asleep_cost} DP/attempt \n" \
          "Revelation (awake): {awake_rate:.1%}, {awake_cost} DP/attempt \n" \
          "Divine avatar: {avatar_rate:.1%}, {avatar_cost} DP/attempt \n\n" \
          "Priest research bonus: +{priest_bonus:.0%} \n\n" \
          "Research cost multiplier (increases proportional to population): {multiplier}".format(
            name=info["display_name"],
            inspiration_rate=int(db.get_attribute(discord_id, Attributes.DIVINE_INSPIRATION_RATE)),
            inspiration_cost=int(db.get_attribute(discord_id, Attributes.DIVINE_INSPIRATION_COST)),
            asleep_rate=db.get_attribute(discord_id, Attributes.ASLEEP_REVELATION_RATE),
            asleep_cost=db.get_attribute(discord_id, Attributes.ASLEEP_REVELATION_COST),
            awake_rate=db.get_attribute(discord_id, Attributes.AWAKE_REVELATION_RATE),
            awake_cost=db.get_attribute(discord_id, Attributes.AWAKE_REVELATION_COST),
            avatar_rate=db.get_attribute(discord_id, Attributes.DIVINE_AVATAR_RATE),
            avatar_cost=int(db.get_attribute(discord_id, Attributes.DIVINE_AVATAR_COST)),
            priest_bonus=db.get_attribute(discord_id, Attributes.PRIEST_RESEARCH_BONUS),
            multiplier=db.get_attribute(discord_id, Attributes.RESEARCH_COST_MULTIPLIER)
          )
