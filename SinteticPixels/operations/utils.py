

from SinteticPixels.img import types


def validate_img_type(valid_types, actual_type, name):
    assert (actual_type in valid_types), "invalid img_type not can be {} for {} operation".format(actual_type, name)
