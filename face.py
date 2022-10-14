import face_recognition
import cv2
import numpy as np
from knownfaces import *
from images import *
from file_functions import *
import os

#video_capture = cv2.VideoCapture(0)

def start():

    known_face_encodings = []

    for i in image:
        a = face_recognition.load_image_file(i)
        a_encoding = face_recognition.face_encodings(a)[0]
        known_face_encodings.append(a_encoding)



    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []

    image_path = read_Image()
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    #cv2.imshow("image", img)
    
    # Grab a single frame of video
        #ret, frame = video_capture.read(1)

        # Only process every other frame of video to save time

    if True: #process_this_frame:

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []

        for face_encoding in face_encodings:

            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
        
        print(face_names)
        writeInFile(face_names)
        os.remove(image_path)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return "Done"
