from faker import Faker
import random
from post.models import Post

images = [
    "post/Geopark-Cliff.jpg",
    "post/Everest-0.jpg",
    "post/Kitchen-At-Holmes-JustinDeSouza-60.jpg",
    "post/Verbier_raphaelsurmont_20230614.jpg",
    "post/hello_ai_blog_WO4k60A.png",
]


def insert_fake_data_in_post():
    fake = Faker()
    for i in range(40):
        Post.objects.create(
            title=fake.sentence(),
            content=fake.paragraph(nb_sentences=20),
            image=random.choice(images),
        )
