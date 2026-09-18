import cv2
import os
import glob

# ==============================
# Traffic Management Parameters
# ==============================

IMAGE_FOLDER = "traffic_images"

# Threshold for considering a lane congested
CONGESTION_THRESHOLD = 8

# ==============================
# Vehicle Detection
# ==============================

def detect_vehicles(image):
    """
    Detect vehicles in the input image.

    This function can be connected to a trained
    object detection model such as YOLO.
    """

    # Placeholder for the vehicle detection model.
    # Replace this section with the trained YOLO model.

    detected_vehicles = []

    return detected_vehicles


# ==============================
# Lane Density Calculation
# ==============================

def calculate_lane_density(vehicles, image_width):
    """
    Calculate the number of vehicles in the
    left and right lanes.
    """

    middle_point = image_width // 2

    left_lane = 0
    right_lane = 0

    for vehicle in vehicles:

        x_center = vehicle["x_center"]

        if x_center < middle_point:
            left_lane += 1
        else:
            right_lane += 1

    return left_lane, right_lane


# ==============================
# Traffic Decision
# ==============================

def analyze_traffic(left_lane, right_lane):
    """
    Determine whether traffic congestion exists
    and which lane is more congested.
    """

    if left_lane >= CONGESTION_THRESHOLD and left_lane > right_lane:
        return "LEFT_CONGESTED"

    if right_lane >= CONGESTION_THRESHOLD and right_lane > left_lane:
        return "RIGHT_CONGESTED"

    return "NORMAL"


# ==============================
# Lane Management
# ==============================

def manage_lanes(traffic_status):
    """
    Manage lane allocation according to
    the detected traffic condition.
    """

    if traffic_status == "LEFT_CONGESTED":

        print("Left lane is congested.")
        print("Incoming traffic is temporarily stopped.")
        print("Waiting for vehicles inside the intersection to clear.")
        print("Switching lane allocation.")
        print("Left lane -> Right lane")
        print("Right lane -> Left lane")
        print("Traffic flow resumed.")

    elif traffic_status == "RIGHT_CONGESTED":

        print("Right lane is congested.")
        print("Incoming traffic is temporarily stopped.")
        print("Waiting for vehicles inside the intersection to clear.")
        print("Switching lane allocation.")
        print("Right lane -> Left lane")
        print("Left lane -> Right lane")
        print("Traffic flow resumed.")

    else:

        print("Traffic is normal.")
        print("Current lane configuration maintained.")


# ==============================
# Image Processing
# ==============================

def process_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print(f"Could not read image: {image_path}")
        return

    height, width = image.shape[:2]

    vehicles = detect_vehicles(image)

    left_lane, right_lane = calculate_lane_density(
        vehicles,
        width
    )

    traffic_status = analyze_traffic(
        left_lane,
        right_lane
    )

    print("\n------------------------------")
    print(f"Image: {image_path}")
    print(f"Left lane vehicles: {left_lane}")
    print(f"Right lane vehicles: {right_lane}")
    print(f"Traffic status: {traffic_status}")

    manage_lanes(traffic_status)


# ==============================
# Main Program
# ==============================

def main():

    image_files = glob.glob(
        os.path.join(IMAGE_FOLDER, "*.jpg")
    )

    image_files += glob.glob(
        os.path.join(IMAGE_FOLDER, "*.png")
    )

    if not image_files:
        print("No traffic images found.")
        return

    for image_path in image_files:

        process_image(image_path)


if __name__ == "__main__":
    main()
