import easyocr
import cv2
import matplotlib.pyplot as plt
import csv

# Initialize the EasyOCR Reader
reader = easyocr.Reader(['en'])  

# Load the image 
image_path = 'image2.png'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image with zoom functionality
def zoom_factory(ax, base_scale=1.1):
    def zoom(event):
        scale_factor = base_scale if event.step > 0 else 1 / base_scale
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        xdata, ydata = event.xdata, event.ydata
        ax.set_xlim([xdata - (xdata - xlim[0]) * scale_factor, xdata + (xlim[1] - xdata) * scale_factor])
        ax.set_ylim([ydata - (ydata - ylim[0]) * scale_factor, ydata + (ylim[1] - ydata) * scale_factor])
        plt.draw()

    return zoom

fig, ax = plt.subplots()
ax.imshow(image_rgb)
zoom_callback = zoom_factory(ax)
fig.canvas.mpl_connect('scroll_event', zoom_callback)
plt.axis('off')
plt.show()

# Perform text detection
results = reader.readtext(image_path)

# Save detected text to CSV
csv_path = 'detected_text.csv'
with open(csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    for (bbox, text, prob) in results:
        writer.writerow([text])

# Print detected text and draw bounding boxes
for (bbox, text, prob) in results:
    print(f'Detected text: {text}')
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 0), 2)
   
    cv2.putText(image_rgb, text, (top_left[0] - 55, top_left[1] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 4)

# Display the image with annotations and zoom
fig, ax = plt.subplots()
ax.imshow(image_rgb)
zoom_callback = zoom_factory(ax)
fig.canvas.mpl_connect('scroll_event', zoom_callback)
plt.axis('off')
plt.show()

print(f"Detected text saved to {csv_path}")
