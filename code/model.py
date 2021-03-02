from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D, Activation, Flatten, Dropout, Lambda
from tensorflow.keras.layers import Dense

def get_nVidia_model():
    model = Sequential()

    model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape = (66, 200, 3)))

    model.add(Conv2D(filters = 24, kernel_size = (5, 5), strides=(2, 2), activation='relu', padding='valid'))
    model.add(Conv2D(filters = 36, kernel_size = (5, 5), strides=(2, 2), activation='relu',  padding='valid'))
    model.add(Conv2D(filters = 48, kernel_size = (5, 5), strides=(2, 2), activation='relu',  padding='valid'))
    
    model.add(Conv2D(filters = 64, kernel_size = (3, 3), activation='relu', padding='valid'))
    model.add(Conv2D(filters = 64, kernel_size = (3, 3), activation='relu', padding='valid'))

    model.add(Flatten())

    model.add(Dense(100))
    model.add(Dense(50))
    model.add(Dense(10))
    model.add(Dense(1))

    return model