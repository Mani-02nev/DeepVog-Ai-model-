# 🚀 Perfect Pipeline for DeepVOG Light Eye Tracking Model

Write-Host "--- 👁️ Starting Eye Tracking Model Pipeline ---" -ForegroundColor Cyan

# 1. Generate Keras Model (.h5)
Write-Host "➡️ Creating Keras model..." -ForegroundColor Yellow
python deepvog_light.py

# 2. Quantize Model (INT8 TFLite)
Write-Host "➡️ Quantizing model to INT8 TFLite..." -ForegroundColor Yellow
python convert_deepvog.py

# 3. Compile for Vela (Ethos-U)
Write-Host "➡️ Compiling for Ethos-U NPU using Vela..." -ForegroundColor Yellow
# Activate Vela Environment
.\vela_env\Scripts\activate.ps1
vela deepvog_light.tflite --accelerator-config ethos-u55-128 --output-dir output
deactivate

# 4. Generate C++ Data for TFLite Micro
Write-Host "➡️ Generating model_data.cc..." -ForegroundColor Yellow
python generate_cc.py

# 5. Run Verification (Python)
Write-Host "➡️ Verifying model with Python inference..." -ForegroundColor Yellow
python output/run_model.py

Write-Host "✅ Pipeline complete!" -ForegroundColor Green
