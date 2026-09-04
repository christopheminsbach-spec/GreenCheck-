import csv

from django.core.management.base import BaseCommand

from plants.models import Plant


class Command(BaseCommand):

    help = "Importe les plantes depuis dataset/plants.csv"


    def handle(self, *args, **options):

        file_path = "dataset/plants.csv"


        Plant.objects.all().delete()


        with open(
            file_path,
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            plants = []


            for row in reader:

                plants.append(
                    Plant(
                        name=row.get("name", ""),
                        scientific_name=row.get(
                            "scientific_name",
                            ""
                        ),
                        family=row.get(
                            "family",
                            ""
                        ),
                        origin=row.get(
                            "origin",
                            ""
                        ),
                        description=row.get(
                            "description",
                            ""
                        ),
                        care=row.get(
                            "care",
                            ""
                        ),
                        image_url=row.get(
                            "image_url",
                            ""
                        )
                    )
                )


            Plant.objects.bulk_create(
                plants
            )


        self.stdout.write(
            self.style.SUCCESS(
                f"{len(plants)} plantes importées"
            )
        )