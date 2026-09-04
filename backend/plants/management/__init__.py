import csv

from django.core.management.base import BaseCommand  # pyright: ignore[reportMissingModuleSource]

from plants.models import Plant


class Command(BaseCommand):

    help = "Importe les plantes depuis dataset/plants.csv"


    def handle(self, *args, **options):

        file_path = "dataset/plants.csv"


        with open(
            file_path,
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)


            count = 0


            for row in reader:

                Plant.objects.create(
                    name=row["name"],
                    scientific_name=row["scientific_name"]
                )

                count += 1


        self.stdout.write(
            self.style.SUCCESS(
                f"{count} plantes importées"
            )
        )