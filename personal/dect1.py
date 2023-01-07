aquarium_creatures = [
  {"name": "sammy", "species": "shark", "tank number": "11", "type": "fish"},
  {"name": "ashley", "species": "crab", "tank number": "25", "type": "shellfish"},
  {"name": "jo", "species": "guppy", "tank number": "18", "type": "fish"},
  {"name": "jackie", "species": "lobster", "tank number": "21", "type": "shellfish"},
  {"name": "charlie", "species": "clownfish", "tank number": "12", "type": "fish"},
  {"name": "olly", "species": "green turtle", "tank number": "34", "type": "turtle"}
]
def filter_set(aquarium_creatures, search_string):
	def iterator_func(x):
		for v in x.values():
			if search_string in v:
				return True
		return False
	return filter(iterator_func, aquarium_creatures)

filtered_records = filter_set(aquarium_creatures, "2")

print(list(filtered_records))