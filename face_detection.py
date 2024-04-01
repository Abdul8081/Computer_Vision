import cv2

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    
    # Draw bounding boxes around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 1)
    
    # Resize the image for better visualization
    resized_image = cv2.resize(image, (600, 600))  # You can adjust the size as needed
    
    # Display the resized image with bounding boxes around faces
    cv2.imshow("Face Detection", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the image
image_path = "D:\my_pic.jpg"

# Detect faces in the image
detect_faces(image_path)
