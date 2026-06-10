import cv2
import numpy as np

# Color Tracking Example with static HSV ranges
# This script is intended to be run locally

def run_tracking():
    cap = cv2.VideoCapture(0)
    
    # Static HSV ranges for a typical red object
    # Red often sits at the ends of the Hue scale (0-10 and 160-180)
    LOWER_RED = np.array([0, 120, 70])
    UPPER_RED = np.array([10, 255, 255])
    
    print("Running Simple Red Color Tracking...")
    print("Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        # Convert to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Create mask
        mask = cv2.inRange(hsv, LOWER_RED, UPPER_RED)
        
        # Apply mask
        result = cv2.bitwise_and(frame, frame, mask=mask)
        
        # Display
        cv2.imshow('Original', frame)
        cv2.imshow('Red Tracking', result)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_tracking()
