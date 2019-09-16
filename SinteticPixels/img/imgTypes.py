#common scales and types
basic_float = (0, 1, float)
expanded_float = (0, 255, float)
normalized_float = (-1, 1, float)
basic_byte = (0, 255, 'byte')
basic_bool = (0, 1, bool)


#comon scale types for some imgs
universal_scales = (basic_float, expanded_float, basic_int, normalized_float, complete_float)


#propierties of the images
#convertion type
convertion_img = {
	'name': 'convertion',
	'scales': (basic_float),
	'channels': 3,
	'alpha': True,
	'operation_type': 'universal_operations',
	'to_conv': None,
	'from_conv': None
}

#general use images types
grayscale_img = {
	'name': 'gray_scale',
	'scales': universal_scales,
	'channels': 1,
	'alpha': True,
	'operation_type': 'universal_operations',
	'to_conv': None,
	'from_conv': None
}

rgb_img = {
	'name': 'rgb',
	'scales': universal_scales,
	'channels': 3,
	'alpha': True,
	'operation_type': 'universal_operations',
	'to_conv': None,
	'from_conv': None
}

bgr_img = {
	'name': 'bgr',
	'scales': universal_scales,
	'channels': 3,
	'alpha': True,
	'operation_type': 'universal_operations',
	'to_conv': None,
	'from_conv': None
}


indexed_img = {
	'name': 'indexed',
	'scales': (basic_int),
	'channels': 1,
	'alpha': False,
	'operation_type': 'indexed_operations',
	'to_conv': None,
	'from_conv': None
}


binary_img = {
	'name': 'binary',
	'scales': (basic_bool),
	'channels': 1,
	'alpha': False,
	'operation_type': 'boolean_operations',
	'to_conv': None,
	'from_conv': None
}

registertypes = (grayscale_img, rgb_img, bgr_img, indexed_img, binary_img)

operationtypes = (universal_operations ,boolean_operations, indexed_operations)