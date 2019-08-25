from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers.core import Activation, Flatten, Dense
# from helpers import Singleton


# class First_CNN(metaclass=Singleton):
class First_CNN:

    def build():
        # initialize the model
        model = Sequential()

        # first set of CONV => RELU => POOL
        model.add(Convolution2D(20, kernel_size=(3, 3), input_shape=(6, 7, 1)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))

        # second set of CONV => RELU => POOL
        model.add(Convolution2D(20, kernel_size=(2, 2)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))

        # set of FC => RELU layers
        model.add(Flatten())
        model.add(Dense(40))
        model.add(Activation("relu"))

        # softmax classifier
        model.add(Dense(1))
        model.add(Activation("sigmoid"))

        # return the constructed network architecture
        return model
