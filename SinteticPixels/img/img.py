import numpy as np

from SinteticPixels.img import types

class Image():
    """
    A cointainer for image information for use that in procces and convertions
    """
    def __init__(self, data, name, img_type = None, has_alpha = False):
        """
        the image constructor with auto inferentiation of image type
        """
        #ensure the ndim of data array is equal to 3
        if  data.ndim == 2:
            data = data[..., np.newaxis] #check if this is a view or what
        assert data.ndim == 3, "ndim of data ndarray parameter should be 2 or 3"

        channels = data.shape[2]
        data_dtype = data.dtype


        #inferetiantion img type

        #is a binary image?
        if data_dtype in types.binary_image['valid_dtypes']:
            if channels in types.binary_image['valid_shapes']:
                img_type = types.binary_image

        #is a gray or rgb image?
        elif data_dtype in types.common_valid_dtypes:

            #the image has alpha?
            offset = 0
            if has_alpha:
                offset = 1

            #is a gray image?
            if channels == 1 + offset:
                img_type = types.gray_image
            #is a rbg image?
            elif channels == 3 + offset:
                img_type = types.rgb_image
        else:
            #no image type found assertion
            img_type = None
        assert img_type is not None, "data do not have valid properties"

        #menbers of class
        self.name = name
        self.data = np.copy(data)
        self.img_type = img_type
        self.has_alpha = has_alpha

        #scale of data
        self.scale = (0,1)

    def get_data(self, min_shape = False):
        """
        Get the ndarray object and if te min_shape parameter is true it will return 
        if is posible a ndim = 2 ndarray
        """
        if min_shape and self.data.shape[2] == 1:
            return self.data[:,:,0]
        return self.data
            
    def type_name(self):
        return self.img_type['type_name']

    def get_dtype(self):
        return self.data.dtype

    def channels(self):
        return self.data.shape[2]

    #general operations
    def convolution(self):
        pass
    
    def stamp(self):
        pass

    def masking(self):
        pass
    
    #int/ float types
    def fusion(self):
        pass
    def replace_color(self):
        pass


    #binary type only
    def union(self): 
        pass

    def interception(self): 
        pass

    def diference(self): 
        pass
    
    #convertion
    def convert(self, to_type):
        pass
    
    #load / save
    def save(self):
        pass

    def load(self):
        pass