# FalconEdge Filter

🦅 **FalconEdge Filter** — "Strikes the edges, dodges the noise."

## Overview

FalconEdge is an adaptive edge sharpening filter designed to enhance edges and textures in high-resolution grayscale images while avoiding noise amplification. It balances edge enhancement with noise suppression by using a masked guided high-pass approach based on local variance.

---

## Features

- **Edge sharpening:** Emphasizes gradients to enhance edges and textures.
- **Noise-aware masking:** Suppresses sharpening in flat/noisy regions.
- **Adaptive boost:** Strengthens strong edges more than weak noisy details.
- **Optimized for high-resolution images:** Minimizes artifacts and aliasing.

---

## How It Works

1. **Low-frequency extraction:** Applies mild Gaussian blur to get the smooth base image.
2. **High-frequency isolation:** Subtracts the low-frequency component from the original to extract edges and noise.
3. **Noise suppression mask:** Computes local variance to detect textured areas; only these areas are sharpened.
4. **Edge sharpening:** Adds scaled high-frequency details back to the original image guided by the mask.

Mathematically:

\[
I_{\text{sharp}} = I + \alpha \cdot M \cdot (I - I_{\text{low}})
\]

Where:

- \( I_{\text{low}} \) is the Gaussian blurred image.
- \( M \) is a binary mask based on local variance thresholding.
- \( \alpha \) controls sharpening strength.

---

## Usage

### Requirements

- Python 3.6+
- OpenCV (`cv2`)
- NumPy
- Matplotlib

### Installation

```bash
pip install opencv-python numpy matplotlib
