from keras.optimizers import rmsprop
from cnn_definition import First_CNN
from helpers import convert_2Dmatrix_to_np
import numpy as np

# Prepare CNN
print("=======" * 10)

model = First_CNN.build()
opt = rmsprop(lr=0.001, decay=1e-5)
model.compile(loss='binary_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

# Get board and cast to numpy array
board = [[0, 1, 1, 1, -1, -1, -1], [0, 1, -1, -1, 1, 1, -1],
        [0, 0, 1, 1, -1, 1, 0], [0, 0, -1, 0, 1, 0, 0],
        [0, 0, 1, 0, -1, 0, 0], [0, 0, 1, 0, -1, 0, 0]]
x_1 = np.array(convert_2Dmatrix_to_np([board])).reshape((6, 7, 1))
x_1 = np.expand_dims(x_1, axis=0)

x_batch = [x_1]
y_batch = [1]

model.train_on_batch(x_batch, y_batch)
model.train_on_batch(x_batch, y_batch)
model.train_on_batch(x_batch, y_batch)
model.train_on_batch(x_batch, y_batch)
print(model.predict(x_1))

# Evaluate performances
loss_and_metrics = model.evaluate(x_batch, y_batch)
