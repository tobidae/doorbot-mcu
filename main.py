import cv2
import imutils
import time
import firebase


def main():
    haar_classifier = cv2.CascadeClassifier("helpers/haarcascade_upperbody.xml")
    cloud_storage = firebase.Storage()

    # video_cam = cv2.VideoCapture(0)
    video_cam = cv2.VideoCapture("helpers/video2.mp4")
    video_width = video_cam.get(3)
    video_height = video_cam.get(4)

    start_of_detect = None
    elapsed_time = 0
    video_clip = None

    while True:
        ret, frame = video_cam.read()

        if not ret:
            break

        frame = imutils.resize(frame, width=720)       # resize original video for better viewing performance
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert video to grayscale

        persons = haar_classifier.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5,
            minSize=(50, 100),  # Min size for valid detection
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if persons and len(persons) > 0 and not start_of_detect:
            start_of_detect = time.time()
            size = (video_width, video_height)
            video_clip = cv2.VideoWriter('clip.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 15, size)

        """
        Logic:
        - Get the upper bodies in a video sequence
        - On upper body, create a 5 second video and get a frame as the thumbnail
        - Send a timestamp and alert that a person was detected
        - Upload the 5 second video and frame to storage
        - Wait 20 seconds and start observing again
        Bonus:
        - Once a person is detected in frame, turn on a light on our network
        - Turn on the TV plug
        """
        # Draw a rectangle around the upper bodies
        if start_of_detect and elapsed_time < 5:
            video_clip.write(frame)
            elapsed_time = time.time() - start_of_detect

        if elapsed_time >= 5:
            start_of_detect = None
            elapsed_time = 0
            video_clip.release()

        # stop script when "q" key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release capture
    video_cam.release()
    video_clip.release()
    cv2.destroyAllWindows()


main()
