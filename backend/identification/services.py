
import requests


PLANTNET_API_KEY = "TON_API_KEY"


def identify_plant(image):

    url = (
        "https://my-api.plantnet.org/v2/identify"
    )


    files = {
        "images": image
    }


    params = {
        "api-key": PLANTNET_API_KEY,
        "organs": "leaf"
    }


    response = requests.post(
        url,
        files=files,
        params=params
    )


    return response.json()