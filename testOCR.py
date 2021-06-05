# Imports
import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound

# Connects pytesseract(wrapper) to the trained tesseract module
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# # Video feed
# video = cv2.VideoCapture(0)
#
# # Setting width and height for video feed
# video.set(3, 640)
# video.set(4, 480)

# Image feeds
img1 = cv2.imread('Capture_1.JPG')
img2 = cv2.imread('Capture_2.JPG')
img3 = cv2.imread('Capture_3.JPG')
# Obtains only the string from images without visual feedback
# print(pytesseract.image_to_string(img1))
# print(pytesseract.image_to_string(img2))
# print(pytesseract.image_to_string(img3))

# Obtain the height and width for each image 3rd value is not needed
# ONLY FOR CHARACTER
h1Img, w1Img, none1 = img1.shape
h2Img, w2Img, none2 = img2.shape
h3Img, w3Img, none3 = img3.shape
# print(img1.shape)
# print(img2.shape)
# print(img3.shape)

# Convert images into bounding box values: x, y, width and height
# ONLY FOR CHARACTERS
box1 = pytesseract.image_to_boxes(img1)
box2 = pytesseract.image_to_boxes(img2)
box3 = pytesseract.image_to_boxes(img3)
# print(box1)
# print(box2)
# print(box3)

# Convert images into bound data values: level, page no, block no, paragraph no,
# line no, word no, x, y, width, height, conf, value
# ONLY FOR WORDS
data1 = pytesseract.image_to_data(img1)
data2 = pytesseract.image_to_data(img2)
data3 = pytesseract.image_to_data(img3)
# print(data1)
# print(data2)
# print(data3)


def charone():
    for a in box1.splitlines():
        # Converts 'box1' string into a list stored in 'a'
        a = a.split()
        # Storing values in the right variables
        x, y = int(a[1]), int(a[2])
        w, h = int(a[3]), int(a[4])
        # Display bounding box of each letter
        cv2.rectangle(img1, (x, h1Img - y), (w, h1Img - h), (0, 0, 255), 1)
        # Display detected letter under each bounding box
        cv2.putText(img1, a[0], (x, h1Img - y - 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
    # Output the bounding box with the image
    cv2.imshow('Image Output', img1)
    cv2.waitKey(0)


def chartwo():
    for a in box2.splitlines():
        # Converts 'box2' string into a list stored in 'a'
        a = a.split()
        # Storing values in the right variables
        x, y = int(a[1]), int(a[2])
        w, h = int(a[3]), int(a[4])
        # Display bounding box of each letter
        cv2.rectangle(img2, (x, h2Img - y), (w, h2Img - h), (0, 128, 0), 1)
        # Display detected letter under each bounding box
        cv2.putText(img2, a[0], (x, h2Img - y - 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 128, 0), 1)
    # Output the bounding box with the image
    cv2.imshow('Image Output', img2)
    cv2.waitKey(0)


def charthree():
    for a in box3.splitlines():
        # Converts 'box3' string into a list stored in 'a'
        a = a.split()
        # Storing values in the right variables
        x, y = int(a[1]), int(a[2])
        w, h = int(a[3]), int(a[4])
        # Display bounding box of each letter
        cv2.rectangle(img3, (x, h3Img - y), (w, h3Img - h), (255, 0, 0), 1)
        # Display detected letter under each bounding box
        cv2.putText(img3, a[0], (x, h3Img - y - 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 1)
    # Output the bounding box with the image
    cv2.imshow('Image Output', img3)
    cv2.waitKey(0)


def wordone():
    for z, a in enumerate(data1.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data1' string into a list stored in 'a'
            a = a.split()
            # Checking if array contains a word
            if len(a) == 12:
                # Storing values in the right variables
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word
                cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # Display detected word under each bounding box
                cv2.putText(img1, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
    # Output the bounding box with the image
    cv2.imshow('Image output', img1)
    cv2.waitKey(0)


def wordtwo():
    for z, a in enumerate(data2.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data1' string into a list stored in 'a'
            a = a.split()
            # Checking if array contains a word
            if len(a) == 12:
                # Storing values in the right variables
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word
                cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 1)
                # Display detected word under each bounding box
                cv2.putText(img2, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)
    # Output the bounding box with the image
    cv2.imshow('Image output', img2)
    cv2.waitKey(0)


def wordthree():
    for z, a in enumerate(data3.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data1' string into a list stored in 'a'
            a = a.split()
            # Checking if array contains a word
            if len(a) == 12:
                # Storing values in the right variables
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word
                cv2.rectangle(img3, (x, y), (x + w, y + h), (255, 0, 0), 1)
                # Display detected word under each bounding box
                cv2.putText(img3, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 1)
    # Output the bounding box with the image
    cv2.imshow('Image output', img3)
    cv2.waitKey(0)


def startvideofeed():
    # Video feed
    video = cv2.VideoCapture("https://10.4.183.8:8080/video")

    # Setting width and height for video feed
    video.set(3, 640)
    video.set(4, 480)

    # Allows continuous frames
    while True:
        # Capture each frame from the video feed
        extra, frames = video.read()
        data4 = pytesseract.image_to_data(frames)
        for z, a in enumerate(data4.splitlines()):
            # Counter
            if z != 0:
                # Converts 'data1' string into a list stored in 'a'
                a = a.split()
                # Checking if array contains a word
                if len(a) == 12:
                    # Storing values in the right variables
                    x, y = int(a[6]), int(a[7])
                    w, h = int(a[8]), int(a[9])
                    # Display bounding box of each word
                    cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    # Display detected word under each bounding box
                    cv2.putText(frames, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
        # Output the bounding box with the image
        cv2.imshow('Video output', frames)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            video.release()
            cv2.destroyAllWindows()
            break


def startimagefeed():
    # Video feed
    video = cv2.VideoCapture("https://10.4.183.8:8080/video")

    # Setting width and height for video feed
    video.set(3, 640)
    video.set(4, 480)

    # Capture one frame from the video feed
    extra, frames = video.read()
    data4 = pytesseract.image_to_data(frames)
    for z, a in enumerate(data4.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data1' string into a list stored in 'a'
            a = a.split()
            # Checking if array contains a word
            if len(a) == 12:
                # Storing values in the right variables
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word
                cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # Display detected word under each bounding box
                cv2.putText(frames, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
    # Output the bounding box with the image
    cv2.imshow('Image output', frames)
    cv2.waitKey(0)
    video.release()

def texttospeech():
    # Open the file with write permission
    filewrite = open("String.txt", "w")
    for z, a in enumerate(data1.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data1' string into a list stored in 'a'
            a = a.split()
            # Checking if array contains a word
            if len(a) == 12:
                # Storing values in the right variables
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word
                cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # Display detected word under each bounding box
                cv2.putText(img1, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
                # Writing to the file
                filewrite.write(a[11] + " ")
    filewrite.close()
    # Open the file with read permission
    fileread = open("String.txt", "r")
    language = 'en'
    line = fileread.read()
    if line != " ":
        fileread.close()
        speech = gTTS(text=line, lang=language, slow=False)
        speech.save("test.mp3")
    # Output the bounding box with the image
    cv2.imshow('Image output', img1)
    cv2.waitKey(0)
    playsound("test.mp3")


# Calling character methods
while True:
    option = input("Which option do you choose (1 - 9): ")
    print("\n")
    if option == '1':
        charone()
    elif option == '2':
        chartwo()
    elif option == '3':
        charthree()
    elif option == '4':
        wordone()
    elif option == '5':
        wordtwo()
    elif option == '6':
        wordthree()
    elif option == '7':
        startvideofeed()
    elif option == '8':
        startimagefeed()
    elif option == '9':
        texttospeech()
    else:
        print("Thank you for using the the OCR program")
        break
