# PRNU Fingerprint Extractor

This repository contains a simple Python script to extract the **PRNU (Photo Response Non-Uniformity) fingerprint** from a local image. The fingerprint represents the sensor noise pattern of the camera and can be used for educational purposes or forensic analysis.

## Files

1. **extract_prnu.py** – Python script to extract PRNU from a single image.
2. **example.jpg** – Sample image (replace with your own local images).
3. **README.md** – Instructions and overview.

## Usage

1. Install required packages:

```bash
pip install numpy opencv-python
```

2. Place your image in the repository folder and update the `local_image_path` in `extract_prnu.py`.

3. Run the script:

```bash
python extract_prnu.py
```

4. The PRNU fingerprint will be saved as `prnu_fingerprint.png`.

## Notes

* This is a **basic implementation** using Gaussian denoising. For more accurate results, use multiple reference images and advanced denoising techniques.
* The PRNU fingerprint is a **visual representation** of sensor noise, not a human-readable fingerprint.

## License

MIT License
