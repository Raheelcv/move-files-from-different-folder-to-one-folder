import os
import cv2
from ultralytics import YOLO

# Path to the folder containing videos
video_folder = r"C:\Users\rahee\Desktop\Python_Script\make_annotation_yolov8_truck\ANPR_1and2\New folder"
# Output folder for frames and annotations
output_folder = r"C:\Users\rahee\Desktop\Python_Script\make_annotation_yolov8_truck\frames_ANPR1and2"
# Create output folders if they don't exist
os.makedirs(output_folder, exist_ok=True)
frames_folder = os.path.join(output_folder, "frames")
os.makedirs(frames_folder, exist_ok=True)
annotations_folder = os.path.join(output_folder, "annotations")
os.makedirs(annotations_folder, exist_ok=True)

# Specify model path and class index dynamically
custom_model_path = "V1_loadingvehicle_epoch100.pt"  # Change this to "yolov8n.pt" for pretrained model
DETECTION_CLASS_ID = 0  # Adjust this based on your model's class index (e.g., 7 for truck in YOLOv8 COCO, 0 for custom class)

# Load the YOLO model
model = YOLO(custom_model_path)

# Function to process each video
def process_video(video_path):
    video_name = os.path.basename(video_path).split(".")[0]  # Get video name without extension
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect objects in the frame
        results = model.predict(frame, conf=0.5)  # Confidence threshold set to 0.5
        detections = results[0].boxes.data  # Extract detection data

        # Prepare annotation data
        annotation_lines = []
        for det in detections:
            class_id, conf, x1, y1, x2, y2 = int(det[5]), float(det[4]), *det[:4]
            if class_id == DETECTION_CLASS_ID:
                # Normalize coordinates for YOLO format
                img_height, img_width = frame.shape[:2]
                x_center = ((x1 + x2) / 2) / img_width
                y_center = ((y1 + y2) / 2) / img_height
                width = (x2 - x1) / img_width
                height = (y2 - y1) / img_height
                annotation_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

        # Save frame and annotation if detections are found
        if annotation_lines:
            frame_filename = f"{video_name}_frame{frame_count:04d}.jpg"
            annotation_filename = f"{video_name}_frame{frame_count:04d}.txt"

            # Save frame
            cv2.imwrite(os.path.join(frames_folder, frame_filename), frame)

            # Save annotation
            with open(os.path.join(annotations_folder, annotation_filename), "w") as f:
                f.write("\n".join(annotation_lines))

        frame_count += 1

    cap.release()

# Process all videos in the folder
for video_file in os.listdir(video_folder):
    if video_file.endswith((".mp4", ".avi", ".mov", ".mkv")):
        print(f"Processing video: {video_file}")
        process_video(os.path.join(video_folder, video_file))

print("Processing complete. Frames and annotations saved.")
