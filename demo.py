import cv2
import time
import numpy as np

# Load the mouth images (with alpha channel)
mouth_open_img = cv2.imread('mouth_open.png', cv2.IMREAD_UNCHANGED)  # Mouth open (with alpha channel)
mouth_closed_img = cv2.imread('mouth_closed.png', cv2.IMREAD_UNCHANGED)  # Mouth closed (with alpha channel)

# Function to resize overlay image dynamically
def resize_overlay(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Function to overlay an image on top of another
def overlay_image(base_img, overlay_img, x, y):
    """Overlay overlay_img on top of base_img at position (x, y)."""
    h, w = overlay_img.shape[:2]
    base_h, base_w = base_img.shape[:2]

    # Adjust overlay dimensions if they exceed base image bounds
    if y < 0: y = 0
    if x < 0: x = 0
    if y + h > base_h:
        h = base_h - y
        overlay_img = overlay_img[:h, :, :]
    if x + w > base_w:
        w = base_w - x
        overlay_img = overlay_img[:, :w, :]

    roi = base_img[y:y+h, x:x+w]

    if overlay_img.shape[2] == 4:  # If the overlay image has an alpha channel
        for c in range(3):  # Loop through RGB channels
            roi[:, :, c] = (
                overlay_img[:, :, c] * (overlay_img[:, :, 3] / 255.0) +
                roi[:, :, c] * (1.0 - overlay_img[:, :, 3] / 255.0)
            )
    else:  # If no alpha channel, just overlay RGB channels directly
        roi[:, :, :] = overlay_img

    base_img[y:y+h, x:x+w] = roi
    return base_img

# Main function to simulate speaking avatar
def simulate_speaking():
    # Default mouth size and position
    mouth_width, mouth_height = 500, 250  # Increased size

    # Create a blank canvas of the desired size
    canvas_width = 800  # Canvas width
    canvas_height = 600  # Canvas height
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    # Center the mouth on the canvas
    mouth_x = (canvas_width - mouth_width) // 2  # Center horizontally
    mouth_y = (canvas_height - mouth_height) // 2  # Center vertically

    # Flag to control when avatar starts speaking
    speaking = False

    while True:
        # Capture key press
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):  # Press 's' to start speaking
            speaking = True

        if speaking:
            for mouth_img in [mouth_open_img, mouth_closed_img]:
                # Resize the mouth image to the desired size
                resized_mouth = resize_overlay(mouth_img, mouth_width, mouth_height)
                
                # Start with the blank canvas, and only overlay the mouth on it
                speaking_face = canvas.copy()  # Blank canvas, no static face

                # Overlay the resized mouth image on the blank canvas
                speaking_face = overlay_image(speaking_face, resized_mouth, mouth_x, mouth_y)

                # Display only the mouth animation (no static face in the background)
                cv2.imshow("Speaking Avatar", speaking_face)
                
                if cv2.waitKey(200) & 0xFF == ord('q'):  # Press 'q' to exit
                    return
            time.sleep(0.1)  # Short pause to simulate speaking

        else:
            # Display static screen with instructions when not speaking
            cv2.putText(canvas, "Press 'S' to make the avatar speak", (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("Speaking Avatar", canvas)

        # Exit when 'q' is pressed
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

# Run the speaking avatar simulation
simulate_speaking()
