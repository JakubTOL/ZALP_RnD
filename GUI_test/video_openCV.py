import cv2

# directory path to video file
videoPath = "C:/zf-adas-learning-platform/resources/Driving_50kph.mp4"
# higher value means slower playback speed
frame_rate = 25
global_allow = True
while global_allow:
    # create video object
    video_player = cv2.VideoCapture(videoPath)

    # check if video player opened successfully
    if not video_player.isOpened():
        print("Error, couldn't open video file!")

    # read video frames till end of file
    while video_player.isOpened():
        ret, frame = video_player.read()
        if ret:
            # display result in full-screen
            cv2.namedWindow(videoPath, cv2.WND_PROP_FULLSCREEN)
            # move player with name to right and up
            cv2.moveWindow(videoPath, -30, 0)
            cv2.setWindowProperty(videoPath, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow(videoPath, frame)

            # detect if 'q' key pressed to exit video player and add frame speed control by .waitkey()
            if cv2.waitKey(frame_rate) & 0xFF == ord('q'):
                global_allow = False
                break

            # detect if 'ESC' key pressed to exit video player
            # can't identify working unicode for 'esc'
            # if cv2.waitKey(frame_rate) & 0x27 == ord('ESC'):
            # break

        else:
            break

    # after all frames release the video object
    video_player.release()
    # close all frames form video file
    cv2.destroyAllWindows()
