# import os
# import cv2
# from ultralytics import YOLO

# def annotate_truck_frames_with_yolov8(frames_dir, output_dir, model_path):
#     # Load the YOLOv8 model
#     model = YOLO(model_path)
    
#     # Create output directory for annotations if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Define the class index for "truck" (COCO index is 7)
#     target_class = 7  # Original index for "truck"
#     new_class_id = 0  # The new index for "truck" in the output annotations
    
#     # Loop through all image files in the frames directory
#     for frame_file in os.listdir(frames_dir):
#         if frame_file.endswith((".jpg", ".png")):
#             frame_path = os.path.join(frames_dir, frame_file)
#             output_txt_path = os.path.join(output_dir, os.path.splitext(frame_file)[0] + ".txt")
            
#             # Read the frame
#             frame = cv2.imread(frame_path)
#             if frame is None:
#                 print(f"Error reading frame: {frame_path}")
#                 continue
            
#             # Perform object detection using YOLOv8
#             results = model(frame)
#             detections = results[0].boxes  # Get bounding boxes
            
#             with open(output_txt_path, "w") as f:
#                 for box in detections:
#                     # Extract bounding box info
#                     cls, conf, (x1, y1, x2, y2) = int(box.cls), box.conf, box.xyxy[0]
                    
#                     # Filter for truck class only
#                     if cls == target_class:
#                         # Convert to YOLO format (class, x_center, y_center, width, height)
#                         img_height, img_width, _ = frame.shape
#                         x_center = ((x1 + x2) / 2) / img_width
#                         y_center = ((y1 + y2) / 2) / img_height
#                         width = (x2 - x1) / img_width
#                         height = (y2 - y1) / img_height
                        
#                         # Write to the annotation file with the new class ID
#                         f.write(f"{new_class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
            
#             print(f"Annotated: {frame_file} -> {output_txt_path}")
#     print("Annotation complete.")

# # Usage example
# frames_dir = r"C:\Users\rahee\Desktop\zip_folders\all_frames_ytml9"  # Replace with the directory containing your frames
# output_dir = r"C:\Users\rahee\Desktop\zip_folders\all_frames_ytml9\Result"  # Replace with the directory for annotation files
# model_path = "truck_detection_yolov8m.pt"  # Replace with your YOLOv8 model path

# annotate_truck_frames_with_yolov8(frames_dir, output_dir, model_path)

###############################################################################################################################

import os
import cv2
from ultralytics import YOLO

def extract_frames_from_videos(videos_dir, frames_dir, frame_interval=10):
    """Extract frames from all videos in a directory."""
    os.makedirs(frames_dir, exist_ok=True)
    
    for video_file in os.listdir(videos_dir):
        if video_file.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_path = os.path.join(videos_dir, video_file)
            cap = cv2.VideoCapture(video_path)
            
            frame_count = 0
            video_name = os.path.splitext(video_file)[0]
            video_frames_dir = os.path.join(frames_dir, video_name)
            os.makedirs(video_frames_dir, exist_ok=True)

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                if frame_count % frame_interval == 0:
                    frame_name = f"{video_name}frame{frame_count:04d}.jpg"
                    frame_path = os.path.join(video_frames_dir, frame_name)
                    cv2.imwrite(frame_path, frame)

                frame_count += 1

            cap.release()
            print(f"Extracted frames from {video_file} into {video_frames_dir}")

def annotate_truck_frames_with_yolov8(frames_dir, output_dir, model_path):
    """Annotate frames with YOLOv8 and save annotations."""
    # Load the YOLOv8 model
    model = YOLO(model_path)

    # Create output directory for annotations if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Define the class index for "truck" (COCO index is 7)
    target_class = 0  
    new_class_id = 0  # The new index for "truck" in the output annotations

    for video_frames_dir in os.listdir(frames_dir):
        video_frames_path = os.path.join(frames_dir, video_frames_dir)
        if not os.path.isdir(video_frames_path):
            continue

        video_output_dir = os.path.join(output_dir, video_frames_dir)
        os.makedirs(video_output_dir, exist_ok=True)

        for frame_file in os.listdir(video_frames_path):
            if frame_file.endswith(('.jpg', '.png')):
                frame_path = os.path.join(video_frames_path, frame_file)
                output_txt_path = os.path.join(video_output_dir, os.path.splitext(frame_file)[0] + ".txt")

                # Read the frame
                frame = cv2.imread(frame_path)
                if frame is None:
                    print(f"Error reading frame: {frame_path}")
                    continue

                # Perform object detection using YOLOv8
                results = model(frame)
                detections = results[0].boxes  # Get bounding boxes

                with open(output_txt_path, "w") as f:
                    for box in detections:
                        # Extract bounding box info
                        cls, conf, (x1, y1, x2, y2) = int(box.cls), box.conf, box.xyxy[0]

                        # Filter for truck class only
                        if cls == target_class:
                            # Convert to YOLO format (class, x_center, y_center, width, height)
                            img_height, img_width, _ = frame.shape
                            x_center = ((x1 + x2) / 2) / img_width
                            y_center = ((y1 + y2) / 2) / img_height
                            width = (x2 - x1) / img_width
                            height = (y2 - y1) / img_height

                            # Write to the annotation file with the new class ID
                            f.write(f"{new_class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

                print(f"Annotated: {frame_file} -> {output_txt_path}")

    print("Annotation complete.")

# Usage example
videos_dir = r"D:\YTML9-ANPR Camera Requirement\YTML9_Project\Raw_Data\8.2.2025\Surveillance_cars"  # Replace with the directory containing your videos
frames_dir = r"D:\YTML9-ANPR Camera Requirement\YTML9_Project\Raw_Data\8.2.2025\frames"  # Replace with the directory to save extracted frames
output_dir = r"D:\YTML9-ANPR Camera Requirement\YTML9_Project\Raw_Data\8.2.2025\txt"  # Replace with the directory for annotation files
model_path = "V1.2_loadingvehicle_surv1_100ep_best.pt" 

# Extract frames from videos
extract_frames_from_videos(videos_dir, frames_dir, frame_interval=10)

# Annotate extracted frames
annotate_truck_frames_with_yolov8(frames_dir, output_dir, model_path)

