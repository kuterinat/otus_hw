import pytest

BREEDS_URL = 'https://images.dog.ceo/breeds/'
JPG = '.jpg'

SUCC_STATUS = 'success'
SUCC_STATUS_CODE = 200

ERR_STATUS = 'error'
ERR_STATUS_CODE = 404
ERR_MSG = 'Breed not found (master breed does not exist)'

ALL_BREEDS = {
        "affenpinscher": [],
        "african": [],
        "airedale": [],
        "akita": [],
        "appenzeller": [],
        "australian": [
            "shepherd"
        ],
        "basenji": [],
        "beagle": [],
        "bluetick": [],
        "borzoi": [],
        "bouvier": [],
        "boxer": [],
        "brabancon": [],
        "briard": [],
        "buhund": [
            "norwegian"
        ],
        "bulldog": [
            "boston",
            "english",
            "french"
        ],
        "bullterrier": [
            "staffordshire"
        ],
        "cattledog": [
            "australian"
        ],
        "chihuahua": [],
        "chow": [],
        "clumber": [],
        "cockapoo": [],
        "collie": [
            "border"
        ],
        "coonhound": [],
        "corgi": [
            "cardigan"
        ],
        "cotondetulear": [],
        "dachshund": [],
        "dalmatian": [],
        "dane": [
            "great"
        ],
        "deerhound": [
            "scottish"
        ],
        "dhole": [],
        "dingo": [],
        "doberman": [],
        "elkhound": [
            "norwegian"
        ],
        "entlebucher": [],
        "eskimo": [],
        "finnish": [
            "lapphund"
        ],
        "frise": [
            "bichon"
        ],
        "germanshepherd": [],
        "golden": [],
        "greyhound": [
            "italian"
        ],
        "groenendael": [],
        "havanese": [],
        "hound": [
            "afghan",
            "basset",
            "blood",
            "english",
            "ibizan",
            "plott",
            "walker"
        ],
        "husky": [],
        "keeshond": [],
        "kelpie": [],
        "komondor": [],
        "kuvasz": [],
        "labradoodle": [],
        "labrador": [],
        "leonberg": [],
        "lhasa": [],
        "malamute": [],
        "malinois": [],
        "maltese": [],
        "mastiff": [
            "bull",
            "english",
            "tibetan"
        ],
        "mexicanhairless": [],
        "mix": [],
        "mountain": [
            "bernese",
            "swiss"
        ],
        "newfoundland": [],
        "otterhound": [],
        "ovcharka": [
            "caucasian"
        ],
        "papillon": [],
        "pekinese": [],
        "pembroke": [],
        "pinscher": [
            "miniature"
        ],
        "pitbull": [],
        "pointer": [
            "german",
            "germanlonghair"
        ],
        "pomeranian": [],
        "poodle": [
            "medium",
            "miniature",
            "standard",
            "toy"
        ],
        "pug": [],
        "puggle": [],
        "pyrenees": [],
        "redbone": [],
        "retriever": [
            "chesapeake",
            "curly",
            "flatcoated",
            "golden"
        ],
        "ridgeback": [
            "rhodesian"
        ],
        "rottweiler": [],
        "saluki": [],
        "samoyed": [],
        "schipperke": [],
        "schnauzer": [
            "giant",
            "miniature"
        ],
        "segugio": [
            "italian"
        ],
        "setter": [
            "english",
            "gordon",
            "irish"
        ],
        "sharpei": [],
        "sheepdog": [
            "english",
            "shetland"
        ],
        "shiba": [],
        "shihtzu": [],
        "spaniel": [
            "blenheim",
            "brittany",
            "cocker",
            "irish",
            "japanese",
            "sussex",
            "welsh"
        ],
        "springer": [
            "english"
        ],
        "stbernard": [],
        "terrier": [
            "american",
            "australian",
            "bedlington",
            "border",
            "cairn",
            "dandie",
            "fox",
            "irish",
            "kerryblue",
            "lakeland",
            "norfolk",
            "norwich",
            "patterdale",
            "russell",
            "scottish",
            "sealyham",
            "silky",
            "tibetan",
            "toy",
            "welsh",
            "westhighland",
            "wheaten",
            "yorkshire"
        ],
        "tervuren": [],
        "vizsla": [],
        "waterdog": [
            "spanish"
        ],
        "weimaraner": [],
        "whippet": [],
        "wolfhound": [
            "irish"
        ]
    }


def test_get_list_all_breeds(dog_api):

    resp = dog_api.get('breeds/list/all')
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"

    resp_j = resp.json()
    assert resp_j['status'] == SUCC_STATUS, f"Wrong status in response code: {resp_j['status']}"
    assert resp_j['message'] == ALL_BREEDS, f"Wrong list of breeds: {resp_j['message']}"


def test_get_random_dog(dog_api):

    resp = dog_api.get('breeds/image/random')
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"

    resp_j = resp.json()
    assert resp_j['status'] == SUCC_STATUS, f"Wrong status in response code: {resp_j['status']}"
    assert resp_j['message'].startswith(BREEDS_URL), f"Wrong breeds url in response message: {resp_j['message']}"
    assert resp_j['message'].endswith(JPG), f"Wrong file format in response message: {resp_j['message']}"


@pytest.mark.parametrize("breed", [
    "akita",
    "hound",
    "husky",
    "labrador",
    "pomeranian",
    "spaniel",
    "australian",
    "pointer",
    "terrier",
    "rottweiler"
])
def test_get_list_breed_images(dog_api, breed):

    resp = dog_api.get(f'breed/{breed}/images/')
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"

    resp_j = resp.json()
    assert resp_j['status'] == SUCC_STATUS, f"Wrong status in response code: {resp_j['status']}"
    assert type(resp_j['message']) is list, f"Wrong type of message in response: {type(resp_j['message'])}"
    for image in resp_j['message']:
        assert image.startswith(BREEDS_URL), f"Wrong image url in response message: {image}"
        assert image.endswith(JPG), f"Wrong file format for image in response message: {image}"
        assert breed in image, f"Breed name is absent in image url in response message: {image}"
        if ALL_BREEDS[breed]:
            assert any(sub_breed in image for sub_breed in ALL_BREEDS[breed])


@pytest.mark.parametrize("breed", ALL_BREEDS.keys())
def test_get_list_sub_breed(dog_api, breed):

    resp = dog_api.get(f'breed/{breed}/list')
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code, received {resp.status_code}"

    resp_j = resp.json()
    assert resp_j['status'] == SUCC_STATUS, f"Wrong status in response code: {resp_j['status']}"
    assert resp_j['message'] == ALL_BREEDS[breed], f"Wrong list of sub-breeds in response message: {resp_j['message']}"


@pytest.mark.parametrize("breed", ['qqqq', 1234, None, True])
def test_get_rand_image_of_breed_incorrect(dog_api, breed):

    resp = dog_api.get(f'breed/{breed}/images/random')
    assert resp.status_code == ERR_STATUS_CODE, f"Wrong response code, received {resp.status_code}"

    resp_j = resp.json()
    assert resp_j['status'] == ERR_STATUS, f"Wrong status in response code: {resp_j['status']}"
    assert resp_j['message'] == ERR_MSG, f"Wrong response message: {resp_j['message']}"
