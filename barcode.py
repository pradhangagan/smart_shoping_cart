import cv2
from pyzbar.pyzbar import decode

def capture_and_decode():
    # Open webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    print("Press 'c' to capture the photo.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break
        
        # Display the webcam feed
        cv2.imshow("Webcam - Press 'c' to capture", frame)

        # Check for user input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):  # Press 'c' to capture
            break

    # Release the webcam and close the preview window
    cap.release()
    cv2.destroyAllWindows()

    # Save the captured image
    image_path = "captured_image.jpg"
    cv2.imwrite(image_path, frame)
    print(f"Photo saved as {image_path}")

    # Decode barcodes in the saved image
    print("Decoding barcodes...")
    decoded_barcodes = decode(frame)
    if decoded_barcodes:
        for barcode in decoded_barcodes:
            data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            print(f"Found Barcode: Data = {data}, Type = {barcode_type}")
    else:
        print("No barcodes found in the image.")

if __name__ == "__main__":
    capture_and_decode()
