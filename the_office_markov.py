import markovify, csv, random, tweepy
from os import environ
print(environ)
PREFERRED_FOR_RATIO = 35 

PREFERRED_FOR = {
	"dwight": [
		"angela",
		"jim",
		"mose",
	],
	"michael": [
		"oscar",
		"toby",
		"kevin",
		"jim",
		"jan",
		"holly",
		"todd packer"
	],
	"jim": [
		"pam",
		"ryan",
		"darryl",
		"roy",
	],
	"angela": [
		"kevin",
		"dwight",
		"stanley",
		"phyllis",
		"creed",
	],
	"pam": [
		"jim",
		"michael",
	],
	"ryan": [
		"kelly",
		"michael",
	]
}
LEAD_CHARACTERS = [
	"michael",
	"dwight",
	"jim",
]
MAIN_CHARACTERS = [
	"pam",
	"andy",
	"kevin",
	"angela",
	"oscar",
	"erin",
	"ryan",
	"darryl",
	"phyllis",
	"kelly",
	"jan",
	"toby",
	"stanley",
	"meredith",
	"holly",
	"creed",
	"gabe",
	"robert",
	"nellie",
]
OTHER_CHARACTERS = [
	"david",
	"karen",
	"clark",
	"roy",
	"deangelo",
	"charles",
	"pete",
	"jo",
	"david wallace",
	"katy",
	"carol",
	"donna",
	"todd packer",
	"val",
	"danny",
	"josh",
	"all",
	"mose"
]

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

def main():
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth, wait_on_rate_limit=True)

	with open("the_office_script.csv", "r") as f:
		reader = csv.reader(f)
		character_lines = dict()
		for _id, season, episode, scene, text, speaker, deleted in reader:
			if speaker in ["Miichael", "Michae"]:
				speaker = "Michael"
			if speaker in ["Everyone"]:
				speaker = "All"
			speaker = speaker.lower()
			if speaker in character_lines.keys():
				character_lines[speaker].append(text)
			else:
				character_lines[speaker] = [text]
	
	scene = generate_scene(character_lines)
	print(scene)
	print("TOTAL CHARS: {}".format(len(scene)))
	api.update_status(scene)
	print("tweeted!")

def generate_scene(character_lines):
	"""Generate the full scene.
	"""
	script = ""
	current_characters = []
	last_to_speak = ""
	remaining_chars = 280
	for _ in range(random.randint(2,5)):
		if not remaining_chars:
			break
		character = select_character(current_characters, last_to_speak)
		
		line = generate_line(character, character_lines, remaining_chars)
		if line and len(line) < remaining_chars:
			if character not in current_characters:
				current_characters.append(character)
			last_to_speak = character
			script += line.replace("���","'").replace("��","e")
			remaining_chars-=len(line)
	return script

def generate_line(character, character_lines, remaining_chars):
	"""Generate a single line.
	"""
	character_model = markovify.Text(character_lines[character])
	if remaining_chars < 80:
		sentence = character_model.make_short_sentence(remaining_chars-(len(character)+3))
	else:
		sentence = character_model.make_sentence()

	if sentence:
		return "{}: {}\n".format(character.upper(), sentence)
	else:
		return None

def select_character(current_characters, last_to_speak):
	"""Choose the character to speak.
	"""
	if not current_characters:
		potentials_list = basic_random_character_list()
	elif len(current_characters) == 1:
		potentials_list = possible_preferred_character(current_characters[0])
	elif len(current_characters) == 2:
		potentials_list = limit_characters(current_characters)
	else:
		potentials_list = current_characters

	if not potentials_list:
		potentials_list = basic_random_character_list()

	if None in potentials_list:
		potentials_list.remove(None)

	if last_to_speak in potentials_list:
		potentials_list.remove(last_to_speak)

	return potentials_list[random.randint(0,len(potentials_list)-1)]

def limit_characters(current_characters):
	random_int = random.randint(1,100)
	if random_int <= 70:
		return current_characters
	elif random_int <= 90:
		first_preferred = PREFERRED_FOR.get(current_characters[0], [])
		second_preferred = PREFERRED_FOR.get(current_characters[1], [])
		combined_preferred = first_preferred + second_preferred

		if combined_preferred:
			return combined_preferred
		else:
			return basic_random_character_list()
	else:
		return basic_random_character_list()


def possible_preferred_character(first_character):
	if first_character in PREFERRED_FOR.keys():
		random_int = random.randint(1,100)
		if random_int <= PREFERRED_FOR_RATIO:
			return PREFERRED_FOR[first_character]
		else:
			return basic_random_character_list()

def basic_random_character_list():
	random_int = random.randint(1,100)
	if random_int < 50:
		return LEAD_CHARACTERS
	elif random_int < 90:
		return MAIN_CHARACTERS
	else:
		return OTHER_CHARACTERS

main()