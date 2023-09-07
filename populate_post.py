import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

import django

django.setup()

from faker import factory, Faker
from post.models import Post

fake = Faker()
images = [
    "post/Geopark-Cliff.jpg",
    "post/Everest-0.jpg",
    "post/Kitchen-At-Holmes-JustinDeSouza-60.jpg",
    "post/Verbier_raphaelsurmont_20230614.jpg",
    "post/hello_ai_blog_WO4k60A.png",
]


for k in range(20):
    Post.objects.create(
        title=fake.sentence(),
        content=fake.paragraph(nb_sentences=100),
        image=random.choice(images),
    )
