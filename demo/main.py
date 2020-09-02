from os import listdir

from cv2 import imread
from PIL import Image
from numpy import asarray

from utils import DATASET_PATH, get_images, create_report, crop_image, detect_face, get_face_info, rate_face


if __name__ == "__main__":
    # Get path to images
    dataset = {person: get_images(person)
               for person in listdir(DATASET_PATH)}

    report_data = {}

    for person_name, person_images in dataset.items():
        from deepface import DeepFace

        report_data[person_name] = {}
        # faces_list = []
        # for person_image in person_images:
        #     person_info = {
        #         "age": None,
        #         "gender": None,
        #         "race": None,
        #         "emotion": None,
        #         "score": None,
        #         "features": None,
        #     }
        #     image = Image.open(person_image)
        #     image = asarray(image)

        #     croped_image = crop_image(image)
        #     cv_image = imread(person_image)

        #     if detect_face(cv_image):
        #         faces_list.append(person_image)

        # print(person_images)
        person_images = [face for face in person_images
                         if detect_face(image=face)]
        
        print("person_images "*50)
        print(person_images)
        face_info = DeepFace.analyze(person_images)

        # person_info.update(face_info)

        # print(face_info)

        d = dict(zip(face_info.keys(), person_images))

        for face in face_info:  # Can't use dict.values() because values size is too big.
            report_data[person_name][d[face]] = face_info[face]

        print(type(face_info))
        print(face_info)
        del face_info

    create_report(report_data)
