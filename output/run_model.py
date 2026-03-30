import numpy as np
import tensorflow as tf

# Load TFLite model
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "deepvog_light_vela.tflite")
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input/output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Create dummy input (same as embedded)
input_shape = input_details[0]['shape']
input_data = np.ones(input_shape, dtype=np.uint8) * 128

# Set input
interpreter.set_tensor(input_details[0]['index'], input_data)

# Run inference
interpreter.invoke()

# Get output
output_data = interpreter.get_tensor(output_details[0]['index'])

print("Eye X:", output_data[0][0])
print("Eye Y:", output_data[0][1])