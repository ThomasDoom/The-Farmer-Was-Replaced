def chop(CURRENT_CROP, CURRENT_ITEM, LIMIT):
	while num_items(CURRENT_ITEM) < LIMIT:
		i = 0
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				har()
				if i % 2 == 0:
					plant(CURRENT_CROP)
				else:
					plant(Entities.Bush)
				move(North)
				i += 1
				har()
			move(East)
			i += 1
				
