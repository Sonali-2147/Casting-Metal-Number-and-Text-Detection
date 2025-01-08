# Cating-Metal-Number-and-Text-Detection

# EasyOCR Text Detection and CSV Export

This project demonstrates how to use EasyOCR and OpenCV for text detection in images. Detected text is saved to a CSV file along with confidence scores.

## Requirements
Ensure you have the following libraries installed:

- Python 3.x
- easyocr
- opencv-python
- matplotlib

You can install them using:
```bash
pip install easyocr opencv-python matplotlib
```

## Project Structure
- `image2.png`: Input image for text detection.
- `detected_text.csv`: CSV file where detected text and confidence scores will be saved.
- `app.py`: Python script containing the text detection logic.

## Usage
1. Place your input image in the project directory and name it `image2.png`.
2. Run the script using:
   ```bash
   python app.py
   ```
3. The script will:
   - Load the image using OpenCV.
   - Perform text detection using EasyOCR.
   - Save detected text and confidence scores in `detected_text.csv`.
   - Display the image with detected text and bounding boxes.

## How the Script Works
1. **Initialize EasyOCR Reader:**
   ```python
   reader = easyocr.Reader(['en'])
   ```
2. **Load the Image:**
   ```python
   image = cv2.imread('image2.png')
   image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   ```
3. **Perform Text Detection:**
   ```python
   results = reader.readtext('image2.png')
   ```
4. **Save Results to CSV:**
   ```python
   with open('detected_text.csv', mode='w', newline='') as file:
       writer = csv.writer(file)
       writer.writerow(['Text', 'Confidence'])
       for (bbox, text, prob) in results:
           writer.writerow([text, prob])
   ```
5. **Display Image with Annotations:**
   ```python
   for (bbox, text, prob) in results:
       top_left, top_right, bottom_right, bottom_left = bbox
       top_left = tuple(map(int, top_left))
       bottom_right = tuple(map(int, bottom_right))
       cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 0), 2)
       cv2.putText(image_rgb, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 4)

   plt.imshow(image_rgb)
   plt.axis('off')
   plt.show()
   ```

## Output
- The detected text and confidence scores will be saved in `detected_text.csv`.
- The image with text annotations will be displayed.

## Output Screenshot

![Screenshot 2025-01-08 145825](https://github.com/user-attachments/assets/9f82af05-47ed-4c11-b55a-c52296908484)


## Contact
For any queries or feedback, please email me at kadamsonali2147@gmail.com.
