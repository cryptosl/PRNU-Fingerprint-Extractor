import cv2
import numpy as np
import os

def extract_noise_residual(image_path):
    """
    Extracts the noise residual from an image (basic PRNU fingerprint)
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Load image as grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = img.astype(np.float32)
    
    # Simple denoising using Gaussian blur
    denoised = cv2.GaussianBlur(img, (3, 3), 0)
    
    # Noise residual = original - denoised
    residual = img - denoised
    
    # Normalize residual for visualization (optional)
    residual_norm = cv2.normalize(residual, None, 0, 255, cv2.NORM_MINMAX)
    residual_norm = residual_norm.astype(np.uint8)
    
    return residual_norm

def save_prnu_fingerprint(image_path, output_path="prnu_fingerprint.png"):
    """
    Extracts the PRNU fingerprint from a local image and saves it
    """
    fingerprint = extract_noise_residual(image_path)
    cv2.imwrite(output_path, fingerprint)
    print(f"PRNU fingerprint saved to: {output_path}")

# -------------------- Main --------------------
if __name__ == "__main__":
    # Replace this path with your local image
    local_image_path = "example.jpg"
    
    # Optional: specify output fingerprint file
    output_fingerprint_path = "prnu_fingerprint.png"
    
    save_prnu_fingerprint(local_image_path, output_fingerprint_path)
