def farm(CURRENT_CROP, CURRENT_ITEM, LIMIT):
		while num_items(Items.Wood) > 5 and num_items(Items.Hay) > 5:
			for x in range(get_world_size()):
				for y in range(get_world_size()):	
					har()
					carrot_seed_check()		
					if limit(CURRENT_ITEM, CURRENT_CROP, LIMIT):
						return		
				move(East)
		return
