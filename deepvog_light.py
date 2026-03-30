import tensorflow as tf

# Lightweight DeepVOG-style model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(96, 96, 1)),

    tf.keras.layers.Conv2D(8, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(16, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(2)  # Output: Eye X, Eye Y
])

model.save("deepvog_light.h5")

print("Lightweight DeepVOG model created!")