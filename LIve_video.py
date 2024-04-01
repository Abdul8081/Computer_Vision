import cv2
#Create a VideoCapture object to capture video from the default camera (usually webcam)
cap = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    # Loop to read frames from the camera
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Display the frame in a window
        cv2.imshow('Live Video', frame)

        # Check for key press (wait for 1 millisecond)
        # If 'q' key is pressed, break the loop and exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the VideoCapture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()