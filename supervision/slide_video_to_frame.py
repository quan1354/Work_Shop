import cv2 as cv
import os


video_path = 'sample_video.mp4'


output_dir = './sample_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


cap = cv.VideoCapture(video_path)


frame_count = 0


while True:
    ret, frame = cap.read()


    # Check if frame is not read properly then break the loop
    if not ret:
        break
   
    # Save frame as image
    output_path = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
    cv.imwrite(output_path, frame)
    print(f'Saved {output_path}')
   
    frame_count += 1


# Release the video capture object
cap.release()
print('Done extracting frames.')









