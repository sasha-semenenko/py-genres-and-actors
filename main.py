import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:

    # Create
    genre_list = ["Western", "Action", "Dramma"]

    for genre in genre_list:
        Genre.objects.create(name=genre)

    actor_list = [
        "George Klooney",
        "Kianu Reaves",
        "Scarlett Keegan",
        "Will Smith",
        "Jaden Smith",
        "Scarlett Johansson",

    ]

    for actor in actor_list:
        actor_split = actor.split()
        Actor.objects.create(
            first_name=actor_split[0], last_name=actor_split[1]
        )

    # Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(
        first_name="George", last_name="Klooney"
    ).update(first_name="George", last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    # Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
