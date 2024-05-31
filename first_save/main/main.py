# SPECIFY CROP TYPE FOR FARMING // None for all
crop = None

while True:
	origin()
	LIMIT = 18000
	
	# PRIORITIZE WOOD AND GRASS IF LOW
	if num_items(Items.Wood) < 8:
		CURRENT_CROP = Entities.Tree
		LIMIT = 1000 # MAX REQ BEFORE RETURING TO ORIGINAL TASK 
	elif num_items(Items.Hay) < 8:
		CURRENT_CROP = Entities.Grass
		LIMIT = 1000
	else:
		# PICK CURRENT CROP BASED ON LIMIT OR SPECIFICATION
		CURRENT_CROP = current_crop(crop, LIMIT)
		
	# MATCH ITEM TO CROP
	CURRENT_ITEM = current_item(CURRENT_CROP, LIMIT)
	
	# BREAK MAIN LOOP IF LIMIT REACHED
	if crop == None:
		if CURRENT_CROP == None:
			break
	else:
		if num_items(CURRENT_ITEM) > LIMIT:
			break
			
	if CURRENT_CROP != Entities.Tree:		
		farm(CURRENT_CROP, CURRENT_ITEM, LIMIT)
			
	else:
		chop(CURRENT_CROP, CURRENT_ITEM, LIMIT)
					
