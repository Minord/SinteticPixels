"""
here are the functions for expand an image.
"""
import numpy as np

from SinteticPixels.img import types
from SinteticPixels.operations import utils
#i dont need import Image class ?


import pdb


supporter_img_types = ('gray_scale', 'rgb', 'binary')

#principal function in the module
#TODO: implement the expand value functionality
def expand_image(image, left = 0, right = 0, top = 0, down = 0, expand_value = None):
    """
    Expand the size of a image with the information of the borders
    can handle images with a ndim of 2 or 3
    Parameters
    -----------
    - image - Image object SinteticPixels.img.img.Image
        this image is for get access to the ndarray and get it propierties.
        the supporter images types are ('gray_scale', 'rgb', 'binary')

    - left - int - has to be positive and mayor to cero

    - right - int - has to be positive and mayor to cero

    - top - int - has to be positive and mayor to cero

    - down - int - has to be positive and mayor to cero
    
    Return
    -------
    -image - the new Image object with the same format but with the expanded image
    """
    #validate the type
    utils.validate_img_type(supporter_img_types, image.type_name(), 'expand')

    original_data = np.copy(image.data)

    expand_with_border_info = True

    horizontal = 1 #for axis
    vertical = 0 #for axis
    last_one = -1 #for indexing readability
    
    if left > 0:
        #create the array.
        to_add = None
        if expand_with_border_info: 
            to_add = original_data[:,0,:]
            to_add = to_add[:, np.newaxis, :]
            to_add = np.repeat(to_add, left, axis = horizontal) 
        else: 
            #implementation default value
            pass
        
        #concatenate to_add to original data
        original_data = np.concatenate((to_add, original_data), axis = horizontal)
        

    if right > 0:
        to_add = None
        #create right array
        if expand_with_border_info:
            to_add = original_data[:,last_one,:]
            to_add = to_add[: ,np.newaxis, :]
            to_add = np.repeat(to_add, right, axis = horizontal) 
        else: 
            #implementation default value
            pass
        #concatenate original_data to_add
        original_data = np.concatenate((original_data, to_add), axis = horizontal)

    if top > 0:
        to_add = None
        #create top array
        if expand_with_border_info: 
            to_add = original_data[0,:,:]
            to_add = to_add[np.newaxis, ...]
            to_add = np.repeat(to_add, top, axis = vertical) 
        else: 
            #implementation default value
            pass
        #concatenate to_add to original_data
        original_data = np.concatenate((to_add, original_data), axis = vertical)

    if down > 0:
        to_add = None
        #create button array
        if expand_with_border_info: 
             to_add = original_data[last_one,:,:]
             to_add = to_add[np.newaxis, ...]
             to_add = np.repeat(to_add, down, axis = vertical)
        else: 
            #implementation default value
            pass
        #concatenate original to_add
        original_data = np.concatenate((original_data, to_add), axis = vertical)

    #build new expanded_image
    image.data = original_data
    return image