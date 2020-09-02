from os import listdir

from typing import Any

from PIL import Image
from autocrop import Cropper

from deepface import DeepFace
from deepface.commons.functions import detectFace


DATASET_PATH = "../input/"


def get_images(person):
    imgs_path = DATASET_PATH+person
    imgs = [f for f in listdir(imgs_path)]
    sorted_imgs = sorted(imgs, key=lambda num: int(num.split(".")[0]))
    return ["{}/{}".format(imgs_path, img) for img in sorted_imgs]


def create_report(report_data: dict) -> None:
    # TODO make report for every person
    print("Creating report.")
    with open("../output/report.txt", "w+") as f:
        for person, images in report_data.items():
            f.write(person + "\n")

            for image, data in images.items():
                f.write(f"\t{image} \n")

                for info, value in data.items():
                    f.write(f"\t\t{info}: {value} \n")
    print("Report created!")


def crop_image(image: Image) -> Image:
    """ Crop the photo automatically.
        * Returns a cropped image around the largest detected face.

    Args:
        image (Image): [numpy array of the image]

    Returns:
        Image: [numpy array of the image] or [None]
        * A cropped numpy array if face detected, else None.
    """
    cropper = Cropper()
    cropped_array = cropper.crop(image)

    return cropped_array


def detect_face(image: Any) -> bool:
    """Сhecks the photo for a face.

    Args:
        image (object): [description]

    Returns:
        bool: False - face not found
              True  - image valid

    TODO:
        check method for several faces on image
        test method
    """
    if image is None:
        return False

    try:
        detectFace(image, target_size=(48, 48), grayscale=True, enforce_detection=True)
        detectFace(image, target_size=(224, 224), grayscale=True, enforce_detection=True)
    except ValueError:
        return False

    return True


def get_face_info(image: object) -> Any:
    ""
    data = DeepFace.analyze(
        image, actions=['emotion', 'age', 'gender', 'race'])
    # print(data)
    # print("{} | Age: {} Gender: {} Race: {} Emotion: {}".format(
    #     image,
    #     demography.get("age"),
    #     demography.get("gender"),
    #     demography.get("dominant_emotion"),
    #     demography.get("dominant_race"),
    # ))
    return data


def rate_face(img: object) -> float:
    """Evaluates the beauty of the face from 0.01% to 100%

    Args:
        img (object): [description]

    Returns:
        float: from 0.01 to 100.00
    """
    pass


def find_similar_people(img: object) -> Any:  # This method isn't tested.
    """ Finds similar people by photo.

    Args:
        img (object): [description]

    Returns:
        Any: [description]

    Comment:
        * This method only needs database of faces (folder with images).
    """
    faces = DeepFace.find(img_path="bin.jpg", db_path="./images")

    return faces
