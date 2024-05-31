def current_crop(crop, LIMIT):
	if crop == "wood":
		return Entities.Tree
	elif crop == "carrot":
		return Entities.Carrots
	elif crop == "hay":
		return Entities.Grass
	elif crop == None:
		if num_items(Items.Hay) < LIMIT:
			return Entities.Grass
		elif num_items(Items.Wood) < LIMIT:
			return Entities.Tree
		elif num_items(Items.Carrot) < LIMIT:
			return Entities.Carrots
		else:
			return None


def current_item(CURRENT_CROP, LIMIT):
	if CURRENT_CROP == Entities.Tree:
		return Items.Wood
	elif CURRENT_CROP == Entities.Carrots:
		return Items.Carrot
	elif CURRENT_CROP == Entities.Grass:
		return Items.Hay


def har():
	if can_harvest():
		harvest()


def carrot_seed_check():
	if num_items(Items.Carrot_Seed) < 2:
		trade(Items.Carrot_Seed)


def carrot_till(CURRENT_CROP):
	if CURRENT_CROP == Entities.Carrots:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(CURRENT_CROP)
	else:
		plant(CURRENT_CROP)


def limit(CURRENT_ITEM, CURRENT_CROP, LIMIT):
	if num_items(CURRENT_ITEM) < LIMIT:
		har()
		carrot_till(CURRENT_CROP)
		move(North)
		har()
	else:
		return True


def origin():
	while get_pos_x() != 0:
		move(West)

	while get_pos_y() != 0:
		move(South)

	clear()
