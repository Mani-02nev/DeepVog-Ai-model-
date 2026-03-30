import tensorflow as tf
import numpy as np

# Load model
model = tf.keras.models.load_model("deepvog_light.h5")

# Converter
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# 🔥 Enable optimization
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# 🔥 REQUIRED for INT8
def representative_data_gen():
    for _ in range(100):
        # Dummy eye image (96x96 grayscale)
        data = np.random.rand(1, 96, 96, 1).astype(np.float32)
        yield [data]

converter.representative_dataset = representative_data_gen

# 🔥 Full INT8
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS_INT8
]

converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8

# Convert
tflite_model = converter.convert()

# Save
with open("deepvog_light.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ TFLite INT8 model created successfully!")