
# # Resize images
# def resize_image(image, width, height):
#     return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# face = resize_image(face, 600, 600)  # Resize face
# mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
# mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# # Global variables
# canvas = np.zeros((800, 800, 3), dtype="uint8")
# canvas[:] = (255, 255, 255)  # White background
# button_clicked = False  # Flag to detect button clicks

# # Draw the static avatar (face + button)
# def draw_avatar():
#     global canvas
#     canvas[:] = (255, 255, 255)  # Clear canvas
#     # Draw face
#     face_x, face_y = 100, 50
#     canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
#     # Draw button
#     button_color = (0, 255, 0)  # Green
#     cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
#     cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# # Mouse callback function to detect clicks
# def on_mouse(event, x, y, flags, param):
#     global button_clicked
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # Check if the button is clicked
#         if 300 <= x <= 500 and 700 <= y <= 750:
#             button_clicked = True

# # Initialize avatar
# draw_avatar()

# # Set up mouse callback
# cv2.namedWindow("Avatar")
# cv2.setMouseCallback("Avatar", on_mouse)

# # Main loop
# while True:
#     if button_clicked:
#         # Display speaking animation with text
#         message = "Hello, welcome to Chainworks!"
#         for i in range(5):  # Number of mouth movements
#             # Draw face with mouth open and display text
#             mouth_x, mouth_y = 250, 450  # Mouth position
#             canvas[mouth_y:mouth_y+100, mouth_x:mouth_x+200] = mouth_open[:, :, :3]
#             cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#             cv2.imshow("Avatar", canvas)
#             cv2.waitKey(300)  # Delay for animation
#             # Draw face with mouth closed and display text
#             canvas[mouth_y:mouth_y+100, mouth_x:mouth_x+200] = mouth_closed[:, :, :3]
#             cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
#             cv2.imshow("Avatar", canvas)
#             cv2.waitKey(300)  # Delay for animation
#         button_clicked = False  # Reset button click
#         draw_avatar()  # Restore the static avatar

#     # Show the canvas
#     cv2.imshow("Avatar", canvas)

#     # Exit on 'q'
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()


import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)  # Resize face
mouth_open = resize_image(mouth_open, 200, 100)  # Resize mouth open
mouth_closed = resize_image(mouth_closed, 200, 100)  # Resize mouth closed

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        # Increase avatar size after button click
        face = resize_image(face, 800, 800)  # Resize face to larger size
        mouth_open = resize_image(mouth_open, 300, 150)  # Resize mouth open to larger size
        mouth_closed = resize_image(mouth_closed, 300, 150)  # Resize mouth closed to larger size

        # Hide the static avatar (clear the canvas)
        canvas[:] = (255, 255, 255)  # Clear the canvas to hide the static face and button
        
        # Display speaking animation with text
        message = "Hello, welcome to Chainworks!"
        for i in range(5):  # Number of mouth movements
            # Draw face with mouth open and display text
            mouth_x, mouth_y = 250, 450  # Mouth position
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_open[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation

            # Draw face with mouth closed and display text
            canvas[mouth_y:mouth_y+150, mouth_x:mouth_x+300] = mouth_closed[:, :, :3]
            cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(300)  # Delay for animation
        
        button_clicked = False  # Reset button click

    # Show the canvas
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
