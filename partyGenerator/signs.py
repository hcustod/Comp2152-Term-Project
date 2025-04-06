import random

AWAKENING_SIGNS = {
    "The Seer": "May grant insight to Humans, but can cloud strength in others.",
    "The Juggernaut": "Bolsters HP at the cost of raw strength for most heroes.",
    "The Phoenix": "Can trigger wild health shifts in the Fae, between renewal or ruin.",
    "The Serpent": "Offers greater strength to the weak. Others feel its sting.",
    "The Warden": "Boosts health and strength, favoring noble races. Dislikes brute force.",
    "The Reaper": "Strengthens Orcs with ruthless precision. Others are merely watched.",
    "The Architect": "Unlocks full power if stats are high enough. Otherwise, nothing yet.",
    "The Vagabond": "Teaches strength to Humans and grants stamina to Fae."
}

def assign_random_sign():
    sign = random.choice(list(AWAKENING_SIGNS.keys()))
    return sign, AWAKENING_SIGNS[sign]