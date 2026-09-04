from plants.models import Disease



def find_disease(label):


    mapping={


        "leaf_spot":

        "Leaf Spot",



        "powdery_mildew":

        "Powdery Mildew",



        "healthy":

        "Healthy",



        "nutrient_deficiency":

        "Nutrient Deficiency"

    }



    name=mapping.get(label)



    return Disease.objects.filter(

        name=name

    ).first()
