import numpy as np
import cv2
import matplotlib.pyplot as plt

def gaussian_blur(I, sigma=1.0):
    return cv2.GaussianBlur(I, (5, 5), sigma)

def local_variance(I, ksize=7):
    """Calculate local variance using a sliding window."""
    mean = cv2.blur(I, (ksize, ksize))
    mean_sq = cv2.blur(I * I, (ksize, ksize))
    variance = mean_sq - mean * mean
    return variance

def falcon_edge_filter(I, alpha=1.2, sigma_blur=1.0, var_threshold=500, ksize=7):
    """
    FalconEdge Filter:
    - I: Grayscale image (float32)
    - alpha: sharpening strength (1.0 - 1.5 recommended)
    - sigma_blur: Gaussian blur sigma for low-frequency component
    - var_threshold: threshold to detect edges (higher = fewer edges)
    - ksize: window size for local variance calculation
    """
    I_low = gaussian_blur(I, sigma=sigma_blur)
    I_high = I - I_low

    variance = local_variance(I, ksize=ksize)
    mask = (variance > var_threshold).astype(np.float32)

    I_sharp = I + alpha * (mask * I_high)

    # Clip to valid range
    I_sharp = np.clip(I_sharp, 0, 255)
    return I_sharp

def main():
    image_path = 'image.jpg'  # Recommended test image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"Error: Could not load image '{image_path}'. Please check the file exists.")
        return

    image = image.astype(np.float32)

    filtered = falcon_edge_filter(image, alpha=1.2, sigma_blur=1.0, var_threshold=500, ksize=7)

    # Convert to uint8 for display
    original_display = np.clip(image, 0, 255).astype(np.uint8)
    filtered_display = filtered.astype(np.uint8)

    # Show side-by-side with matplotlib
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].imshow(original_display, cmap='gray')
    axs[0].set_title('Original Image')
    axs[0].axis('off')

    axs[1].imshow(filtered_display, cmap='gray')
    axs[1].set_title('FalconEdge Filtered Image')
    axs[1].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
