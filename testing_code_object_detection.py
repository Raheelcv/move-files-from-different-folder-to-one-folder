# from ultralytics import YOLO

# # Load model
# model = YOLO(r'V1.3_loadingvehicle_surv1_epoch135_best.pt')

# results = model.predict(r'Surveillance_Main_Gate_Outside_1_YTM_9_GATE_MONITORING_YTM_9_GATE_MONITORING_20250210081542_20250210081617_135592.mp4', save = True)
# print(results[0])
# print("************")

# # Display results
# for box in results[0].boxes:
#     print(box)

###########################################################################################################

from ultralytics import YOLO  # Import YOLO from Ultralytics

# Load the pre-trained YOLO model
model = YOLO(r'V1.3_loadingvehicle_surv1_epoch135_best.pt')

# List of video file paths to process
video_files = [
    r'filled.mp4'
    # r'2.11.2.2025_11-05am.mp4',
    # r'2.11.2.2025_11-05am.mp4'
]

# Loop through each video file and apply object detection
for video in video_files:
    print(f"Processing video: {video}")

    # Perform object detection and save the annotated output
    results = model.predict(video, save=True)

    # Print detection results for the first frame of the video
    print(f"Results for {video}:")
    print(results[0])
    print("************")

    # Loop through detected objects in the first frame and print bounding box details
    for box in results[0].boxes:
        print(box)

    print(f"Finished processing {video}\n")

print("All videos processed successfully!")