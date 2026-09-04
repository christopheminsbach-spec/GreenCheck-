import requests

import os



def analyse_image(image):


    url = os.getenv(

        "AI_SERVICE_URL"

    )



    response = requests.post(

        f"{url}/predict",

        files={

        "image":
        image

        }

    )


    return response.json()