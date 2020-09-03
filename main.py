import sys

from os import listdir

from typing import Any

from cv2 import imread
from PIL import Image
from numpy import asarray

from utils import VALID_TYPES, DATASET_PATH, get_images, create_report, create_full_report, crop_image, detect_face

from autocrop import Cropper

from deepface import DeepFace
from deepface.commons.functions import preprocess_face


if __name__ == "__main__":
    # Get path to images
    dataset = {person: get_images(person)
               for person in listdir(DATASET_PATH)}

    report_data = {}
    for person_name, person_images in dataset.items():
        report_data[person_name] = {}

        # Filter photo without faces
        person_images = [face for face in person_images
                         if detect_face(preprocess_face, face)]
        
        # Analize valid faces
        face_info = DeepFace.analyze(person_images)

        d = dict(zip(face_info.keys(), person_images))

        for face in face_info:  # Can't use dict.values() because values size is too big.
            report_data[person_name][d[face]] = face_info[face]

    create_report(report_data)
    create_full_report(report_data)
