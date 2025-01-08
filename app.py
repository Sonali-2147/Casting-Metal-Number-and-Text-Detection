import easyocr
import cv2
import matplotlib.pyplot as plt
import csv

# Initialize the EasyOCR Reader
reader = easyocr.Reader(['en'])  

# Load the image using OpenCV
image_path = 'image2.png'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image (optional)
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

# Perform text detection
results = reader.readtext(image_path)

# Save detected text and confidence scores to CSV
csv_path = 'detected_text.csv'
with open(csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text', 'Confidence'])
    for (bbox, text, prob) in results:
        writer.writerow([text, prob])

# Print detected text and draw bounding boxes
for (bbox, text, prob) in results:
    print(f'Detected text: {text} (Confidence: {prob:.2f})')
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image_rgb, text, (top_left[0], top_left[1] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 4)

# Display the image with annotations
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

print(f"Detected text saved to {csv_path}")
