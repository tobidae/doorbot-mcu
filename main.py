import cv2
import imutils
import time


def main():
    haar_classifier = cv2.CascadeClassifier("helpers/haarcascade_upperbody.xml")

    # video_cam = cv2.VideoCapture(0)
    video_cam = cv2.VideoCapture("helpers/video2.mp4")
    video_width = video_cam.get(3)
    video_height = video_cam.get(4)

    start_of_detect = None
    elapsed_time = None

    while True:
        ret, frame = video_cam.read()

        if not ret:
            break

        frame = imutils.resize(frame, width=720)       # resize original video for better viewing performance
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert video to grayscale

        upper_body = haar_classifier.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5,
            minSize=(50, 100),  # Min size for valid detection
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if upper_body and not start_of_detect:
            start_of_detect = time.time()

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
        for (x, y, w, h) in upper_body:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(frame, "Person Detected", (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('Video', frame)  # Display video

        # stop script when "q" key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release capture
    video_cam.release()
    cv2.destroyAllWindows()


main()
