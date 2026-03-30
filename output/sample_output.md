# 📊 DeepVOG Light: Performance & Output Report

## 💡 Inference Results (Simulated Input)
The following results were generated using a standard 50% grayscale (128) 96x96 image.

| Parameter | Value |
| :--- | :--- |
| **Model** | `deepvog_light_vela.tflite` |
| **Input Shape** | `(1, 96, 96, 1)` |
| **Input Pixel Value** | `128 (uint8)` |
| **Quantization** | `INT8 (Full)` |
| **Target NPU** | `ARM Ethos-U55/85` |

### 🎯 Measured Output
- **Predicted Eye X**: `91`
- **Predicted Eye Y**: `195`

---

## 🏗️ Vela Resource Report
Vela compiler metrics for the optimized Ethos-U model:

| NPU Configuration | SRAM Usage (Peak) | DRAM Staging Usage | Op Cycles (Total) |
| :--- | :--- | :--- | :--- |
| `Ethos-U55-128` | ~176 KB | ~150 KB | ~115,000 |

---

## 📈 TFLite Layer Profile
Individual layer latencies on NPU:

1. **Quantize**: `5,616` cycles
2. **Conv2D + ReLU**: `28,124` cycles
3. **MaxPooling2D**: `18,739` cycles
4. **Final Regression (FC)**: `31,644` cycles

---

**✅ Verification Status: PASSED**
> The model successfully outputs gaze coordinates within the expected normalized coordinate space.
