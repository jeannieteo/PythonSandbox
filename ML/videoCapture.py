import cv2
# open the video
capture = cv2.VideoCapture(r'Minecraft 2023-05-24 08-40-31.mp4')
# frame counter
counter = 0
# while file is open
while (capture.isOpened()):
    # read a frame
    ret, frame = capture.read()
    # write a number number
    counter += 1
    print(counter)
    # convert to grayscale
    new_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # show every 10th frame
    if counter % 30 == 0:
        plt.imshow(new_frame)
        plt.show()
capture.release()