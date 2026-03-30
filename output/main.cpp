#include <stdio.h>
#include <stdint.h>

// Your model
#include "model_data.cc"

// TFLite Micro
#include "tensorflow/lite/micro/all_ops_resolver.h"
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/schema/schema_generated.h"

constexpr int tensor_arena_size = 200 * 1024;
uint8_t tensor_arena[tensor_arena_size];

int main() {

    // 1️⃣ Load model
    const tflite::Model* model = tflite::GetModel(deepvog_light_vela_tflite);

    if (model->version() != TFLITE_SCHEMA_VERSION) {
        printf("Model version mismatch!\n");
        return -1;
    }

    // 2️⃣ Resolver (operators)
    tflite::AllOpsResolver resolver;

    // 3️⃣ Interpreter
    tflite::MicroInterpreter interpreter(
        model, resolver, tensor_arena, tensor_arena_size
    );

    // 4️⃣ Allocate memory
    interpreter.AllocateTensors();

    // 5️⃣ Get input
    TfLiteTensor* input = interpreter.input(0);

    // Fill input (dummy image)
    for (int i = 0; i < input->bytes; i++) {
        input->data.uint8[i] = 128;  // gray image
    }

    // 6️⃣ Run model
    if (interpreter.Invoke() != kTfLiteOk) {
        printf("Invoke failed!\n");
        return -1;
    }

    // 7️⃣ Get output
    TfLiteTensor* output = interpreter.output(0);

    printf("Eye X: %d\n", output->data.uint8[0]);
    printf("Eye Y: %d\n", output->data.uint8[1]);

    return 0;
}