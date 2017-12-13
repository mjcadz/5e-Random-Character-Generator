import random, sys, time
from random import randint
import string
import argparse, os

pointBuyCost = {8:0,9:1,10:2,11:3,12:4,13:5,14:7,15:9}
pointBuyMax = 27


Class = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

Background = ['Acolyte', 'Charlatan', 'City Watch', 'Clan Crafter', 'Cloistered Scholar', 'Courtier', 'Criminal', 'Criminal (Spy)', 'Entertainer', 'Entertainer (Gladiator)', 'Faction Agent', 'Far Traveler', 'Folk Hero', 'Guild Artisan', 'Guild Artisan (Guild Merchant)', 'Haunted One', 'Hermit', 'Inheritor', 'Inquisitor', 'Investigator', 'Knight of the Order', 'Mercenary Veteran', 'Noble', 'Noble (Knight)', 'Outlander', 'Sage', 'Sailor', 'Sailor (Pirate)', 'Soldier', 'Urban Bounty Hunter', 'Urchin', 'Uthgardt Tribe Member', 'Waterdhavian Noble']

BackgroundPHB = ['Acolyte', 'Charlatan', 'Criminal', 'Criminal (Spy)', 'Entertainer', 'Entertainer (Gladiator)', 'Folk Hero', 'Guild Artisan', 'Guild Artisan (Guild Merchant)', 'Hermit', 'Noble', 'Noble (Knight)', 'Outlander', 'Sage', 'Sailor', 'Sailor (Pirate)', 'Soldier', 'Urchin']

Race      =['Aarakocra', 'Aasimar', 'Dragonborn', 'Dwarf', 'Elf', 'Genasi', 'Gnome', 'Goliath', 'HalfElf', 'Half-Orc', 'Halfling', 'Human', 'Human (Variant)', 'Kenku', 'Lizardfolk', 'Orc', 'Tabaxi', 'Tiefling', 'Triton', 'Warforged', 'Yuan-ti Pureblood']
RacePHB =['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Human (Variant)', 'Tiefling (Infernal)']

#subraces
Aasimar =['Aasimar (DMG)', 'Aasimar (Fallen)', 'Aasimar (Protector)', 'Aasimar (Scourge)']
Dwarf =['Dwarf (Duergar)', 'Dwarf (Hill)', 'Dwarf (Mountain)']
DwarfPHB =['Dwarf (Hill)', 'Dwarf (Mountain)']
Elf =['Elf (Bishatar and Tirahar)', 'Elf (Drow)', 'Elf (Eladrin)', 'Elf (High)', 'Elf (Vadahar)', 'Elf (Wood)']
ElfPHB =['Elf (Drow)', 'Elf (High)','Elf (Wood)']
Genasi =['Genasi (Air)', 'Genasi (Earth)', 'Genasi (Fire)', 'Genasi (Water)']
Gnome =['Gnome (Deep)', 'Gnome (Forest)', 'Gnome (Rock)']
GnomePHB =['Gnome (Forest)', 'Gnome (Rock)']
HalfElf =['Half-Elf', 'Half-Elf (Aquatic Elf Descent)', 'Half-Elf (Drow Descent)', 'Half-Elf (Moon Elf or Sun Elf Descent)', 'Half-Elf (Wood Elf Descent)']
Halfling =['Halfling (Ghostwise)', 'Halfling (Lightfoot)', 'Halfling (Stout)']
HalflingPHB =['Halfling (Lightfoot)', 'Halfling (Stout)']
Tiefling =[ 'Tiefling (Abyssal)', 'Tiefling (Infernal)']

Age =['Child', 'Youth', 'Adult', 'Mature', 'Old']

Gender =['Male', 'Female']

Personality=['Accusative', 'Active', 'Adventurous', 'Affable', 'Aggressive',
    'Agreeable', 'Aimless', 'Aloof', 'Altruistic', 'Analytical', 'Angry',
    'Animated', 'Annoying', 'Anxious', 'Apathetic', 'Apologetic',
    'Apprehensive', 'Argumentative', 'Arrogant', 'Articulate', 'Attentive',
    'Bigoted', 'Bitter', 'Blustering', 'Boastful', 'Bookish', 'Bossy',
    'Braggart', 'Brash', 'Brave', 'Bullying', 'Callous', 'Calm', 'Candid',
    'Cantankerous', 'Capricious', 'Careful', 'Careless', 'Caring', 'Casual',
    'Catty', 'Cautious', 'Cavalier', 'Charming', 'Chaste', 'Chauvinistic',
    'Cheeky', 'Cheerful', 'Childish', 'Chivalrous', 'Clueless', 'Clumsy',
    'Cocky', 'Comforting', 'Communicative', 'Complacent', 'Condescending',
    'Confident', 'Conformist', 'Confused', 'Conscientious', 'Conservative',
    'Contentious', 'Contrary', 'Contumely', 'Conventional', 'Cooperative',
    'Courageous', 'Courteous', 'Cowardly', 'Coy', 'Crabby', 'Cranky',
    'Critical', 'Cruel', 'Cultured', 'Curious', 'Cynical', 'Daring',
    'Deceitful', 'Deceptive', 'Defensive', 'Defiant', 'Deliberate', 'Deluded',
    'Depraved', 'Discreet', 'Discreet', 'Dishonest', 'Disingenuous',
    'Disloyal', 'Disrespectful', 'Distant', 'Distracted', 'Distraught',
    'Docile', 'Doleful', 'Dominating', 'Dramatic', 'Drunkard', 'Dull',
    'Earthy', 'Eccentric', 'Elitist', 'Emotional', 'Energetic', 'Enigmatic',
    'Enthusiastic', 'Epicurean', 'Excited', 'Expressive', 'Extroverted',
    'Faithful', 'Fanatical', 'Fastidious', 'Fatalistic', 'Fearful', 'Fearless',
    'Feral', 'Fierce', 'Feisty', 'Flamboyant', 'Flippant', 'Flirtatious',
    'Foolhardy', 'Foppish', 'Forgiving', 'Friendly', 'Frightened', 'Frivolous',
    'Frustrated', 'Funny', 'Furtive', 'Generous', 'Genial', 'Gentle', 'Gloomy',
    'Goofy', 'Gossip', 'Graceful', 'Gracious', 'Grave', 'Gregarious',
    'Grouchy', 'Groveling', 'Gruff', 'Gullible', 'Happy', 'Harsh', 'Hateful',
    'Helpful', 'Honest', 'Hopeful', 'Hostile', 'Humble', 'Humorless',
    'Humorous', 'Idealistic', 'Idiosyncratic', 'Imaginative', 'Imitative',
    'Impatient', 'Impetuous', 'Implacable', 'Impractical', 'Impulsive',
    'Inattentive', 'Incoherent', 'Indifferent', 'Indiscreet', 'Individualist',
    'Indolent', 'Indomitable', 'Industrious', 'Inexorable', 'Inexpressive',
    'Insecure', 'Insensitive', 'Instructive', 'Intolerant', 'Intransigent',
    'Introverted', 'Irreligious', 'Irresponsible', 'Irreverent', 'Irritable',
    'Jealous', 'Jocular', 'Joking', 'Jolly', 'Joyous', 'Judgmental', 'Jumpy',
    'Kind', 'Know-it-all', 'Languid', 'Lazy', 'Lethargic', 'Lewd', 'Liar',
    'Likable', 'Lippy', 'Listless', 'Loquacious', 'Loving', 'Loyal', 'Lust',
    'Madcap', 'Magnanimous', 'Malicious', 'Maudlin', 'Mean', 'Meddlesome',
    'Melancholy', 'Melodramatic', 'Merciless', 'Merry', 'Meticulous',
    'Mischievous', 'Miscreant', 'Miserly', 'Modest', 'Moody', 'Moralistic',
    'Morbid', 'Morose', 'Mournful', 'Mousy', 'Mouthy', 'Mysterious', 'Naive',
    'Narrow-minded', 'Needy', 'Nefarious', 'Nervous', 'Nettlesome', 'Neurotic',
    'Noble', 'Nonchalant', 'Nurturing', 'Obdurate', 'Obedient', 'Oblivious',
    'Obnoxious', 'Obsequious', 'Obsessive', 'Obstinate', 'Obtuse', 'Odd',
    'Ornery', 'Optimistic', 'Organized', 'Ostentatious', 'Outgoing',
    'Overbearing', 'Paranoid', 'Passionate', 'Pathological', 'Patient',
    'Peaceful', 'Pensive', 'Pertinacious', 'Pessimistic', 'Philanderer',
    'Philosophical', 'Phony', 'Pious', 'Playful', 'Pleasant', 'Poised',
    'Polite', 'Pompous', 'Pondering', 'Pontificating', 'Practical',
    'Prejudiced', 'Pretentious', 'Preoccupied', 'Promiscuous', 'Proper',
    'Proselytizing', 'Proud', 'Prudent', 'Prudish', 'Prying', 'Puerile',
    'Pugnacious', 'Quiet', 'Quirky', 'Racist', 'Rascal', 'Rash', 'Realistic',
    'Rebellious', 'Reckless', 'Refined', 'Repellent', 'Reserved', 'Respectful',
    'Responsible', 'Restless', 'Reticent', 'Reverent', 'Rigid', 'Risk-taking',
    'Rude', 'Sadistic', 'Sarcastic', 'Sardonic', 'Sassy', 'Savage', 'Scared',
    'Scolding', 'Secretive', 'Self-effacing', 'Selfish', 'Selfless', 'Senile',
    'Sensible', 'Sensitive', 'Sensual', 'Sentimental', 'Serene', 'Serious',
    'Servile', 'Sexist', 'Sexual', 'Shallow', 'Shameful', 'Shameless',
    'Shifty', 'Shrewd', 'Shy', 'Sincere', 'Slanderous', 'Sly', 'Smug',
    'Snobbish', 'Sober', 'Sociable', 'Solemn', 'Solicitous', 'Solitary',
    'Solitary', 'Sophisticated', 'Spendthrift', 'Spiteful', 'Stern', 'Stingy',
    'Stoic', 'Stubborn', 'Submissive', 'Sultry', 'Superstitious', 'Surly',
    'Suspicious', 'Sybarite', 'Sycophantic', 'Sympathetic', 'Taciturn',
    'Tactful', 'Tawdry', 'Teetotaler', 'Temperamental', 'Tempestuous',
    'Thorough', 'Thrifty', 'Timid', 'Tolerant', 'Transparent', 'Treacherous',
    'Troublemaker', 'Trusting', 'Truthful', 'Uncommitted', 'Understanding',
    'Unfriendly', 'Unhinged', 'Uninhibited', 'Unpredictable', 'Unruly',
    'Unsupportive', 'Vague', 'Vain', 'Vapid', 'Vengeful', 'Vigilant',
    'Violent', 'Vivacious', 'Vulgar', 'Wanton', 'Wasteful', 'Weary',
    'Whimsical', 'Whiny', 'Wicked', 'Wisecracking', 'Wistful', 'Witty',
    'Zealous']
    


def main():

    #argument parser
    parser=argparse.ArgumentParser(prog = 'randnd.py',description = 'random character generator')
    
    parser.add_argument('-phb','--playershandbook',action="store_true",default=False,dest='phb', help = 'only content from the players handbook')
    global results    
    results =  parser.parse_args()
    
    PHB = results.phb
    
    print ""
    blah="\|/-\|/-"
    for l in blah:
        sys.stdout.write(l)
        sys.stdout.flush()
        sys.stdout.write('\b')
        time.sleep(0.1)
    
    print "Age:         " + random.choice(Age)
    
    print "Gender:      " + random.choice(Gender)
    
    if PHB:
        race = random.choice(RacePHB)
        if race in ['Dwarf','Elf','Gnome','Halfling']:
            race = random.choice(globals()[race+"PHB"])    
    else:    
        race = random.choice(Race)
        if race in ['Aasimar','Dwarf','Elf','Genasi','Gnome','HalfElf','Halfling','Tiefling']:
            race = random.choice(globals()[race])
    
    print "Race:        " + race
    
    print "Class:       " + random.choice(Class)
    
    if PHB:
        background = random.choice(BackgroundPHB)
    else:
        background = random.choice(Background)
    
    print "Background:  " + background
    
    print "Personality: " + random.choice(Personality) + " and " + random.choice(Personality)

    stat = []
    for i in range(0,6):
        stat1=[]
        stat1.append(randint(1,6))
        stat1.append(randint(1,6))
        stat1.append(randint(1,6))
        stat1.append(randint(1,6))
        stat1.sort(key=int)
        x=int(sum(stat1[1:]))
        stat.append(x)
        
    stat.sort(key=int)
    print "Stats:       " + str(stat)
        
        
if __name__ == "__main__":
    main()    
     