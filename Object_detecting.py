import cv2
# Load pre-trained Haar Cascade classifier for object detection
# You can replace "haarcascade_frontalface_default.xml" with the appropriate XML file for your object
cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)

# Load your video file
video_path = "D:\detecting_video_2.mp4"
video = cv2.VideoCapture(video_path)

# Check if the video is opened successfully
if not video.isOpened():
    print("Error: Couldn't open video file")
    exit()

while True:
    # Read a new frame from the video
    ret, frame = video.read()

    # If frame is not read correctly or end of video is reached, break the loop
    if not ret:
        break

    # Convert the frame to grayscale for object detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect objects in the frame using the Haar Cascade classifier
    # Change parameters as needed for your specific object and video
    objects = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected objects
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the frame with detected objects
    cv2.imshow("Object Detection", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
video.release()
cv2.destroyA
