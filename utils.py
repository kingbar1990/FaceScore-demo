from os import listdir


VALID_TYPES = ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']
DATASET_PATH = "input/"


def get_images(person):
    imgs_path = DATASET_PATH+person

    imgs = [f for f in listdir(imgs_path)
            if f.split(".")[-1] in VALID_TYPES]

    # sorted_imgs = sorted(imgs, key=lambda n: int(n.split(".")[0]) if n.split(".")[0].isnumeric() else n)
    return ["{}/{}".format(imgs_path, img) for img in sorted(imgs)]


def create_full_report(report_data: dict) -> None:
    print("Creating report.")
    with open("output/full_report.txt", "w+") as f:
        for person, images in report_data.items():
            f.write(person + "\n")

            for image, data in images.items():
                f.write(f"\t{image} \n")

                for info, value in data.items():
                    f.write(f"\t\t{info}: {value} \n")
    print("Report created!")


def create_report(report_data: dict) -> None:
    print("Creating report.")
    with open("output/report.txt", "w+") as f:
        for person, images in report_data.items():
            f.write(person + "\n")

            ages = [images[img]["age"] for img in images]
            genders = [images[img]["gender"] for img in images]
            races = [images[img]["dominant_race"] for img in images]
            emotions = [images[img]["dominant_emotion"] for img in images]

            age = sum(ages) / len(images)
            gender = max(set(genders), key = genders.count)
            race = max(set(races), key = races.count)
            emotion = max(set(emotions), key = emotions.count)

            summary = {
                "age": age,
                "gender": gender,
                "race": race,
                "emotion": emotion,
            }
            for info, value in summary.items():
                f.write(f"\t{info}: {value} \n")

    print("Report created!")


def crop_image(image):
    cropper = Cropper()
    cropped_array = cropper.crop(image)

    return cropped_array


def detect_face(preprocess_face, image):
    if image is None:
        return False

    try:
        preprocess_face(image, target_size=(48, 48),
                        grayscale=True, enforce_detection=True)
        preprocess_face(image, target_size=(224, 224),
                        grayscale=True, enforce_detection=True)
    except ValueError:
        return False

    return True


# def find_similar_people(img: object) -> Any:  # This method isn't tested.
#     """ Finds similar people by photo.

#     Args:
#         img (object): [description]

#     Returns:
#         Any: [description]

#     Comment:
#         * This method only needs database of faces (folder with images).
#     """
#     faces = deepface.DeepFace.find(img_path="bin.jpg", db_path="./images")

#     return faces
