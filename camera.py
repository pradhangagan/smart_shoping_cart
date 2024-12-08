import cv2

# Initialize the video capture object
video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Set camera properties to match supported formats
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
video_capture.set(cv2.CAP_PROP_FPS, 30)

if not video_capture.isOpened():
    print("Failed to open camera.")
else:
    print("Press 'q' to quit the video stream.")

while True:
    result, video_frame = video_capture.read()

    if result:
        # Display the captured frame
        cv2.imshow("USB Camera Test", video_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting video stream...")
            break
    else:
        print("Failed to capture frame. Exiting...")
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
