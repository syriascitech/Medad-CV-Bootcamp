import cv2

# Threshold Example with static values
# This script is intended to be run locally

def run_threshold():
    # Load image (or use camera)
    cap = cv2.VideoCapture(2)
    
    # Static Threshold value
    THRESHOLD_VALUE = 127 
    
    print("Running Simple Thresholding...")
    print("Static Threshold set to:", THRESHOLD_VALUE)
    print("Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        # Convert to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply Static Threshold
        _, thresh = cv2.threshold(gray, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
        
        # Display
        cv2.imshow('Simple Threshold', thresh)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_threshold()
