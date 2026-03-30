import os

def tflite_to_c_array(tflite_path, output_path):
    with open(tflite_path, 'rb') as f:
        data = f.read()
    
    var_name = os.path.basename(tflite_path).replace('.', '_').replace('-', '_')
    
    with open(output_path, 'w') as f:
        f.write(f'unsigned char {var_name}[] = {{\n')
        for i, byte in enumerate(data):
            f.write(f' 0x{byte:02x},')
            if (i + 1) % 12 == 0:
                f.write('\n')
        f.write('\n};\n')
        f.write(f'unsigned int {var_name}_len = {len(data)};\n')

if __name__ == "__main__":
    tflite_to_c_array("output/deepvog_light_vela.tflite", "output/model_data.cc")
    print("✅ model_data.cc updated!")
