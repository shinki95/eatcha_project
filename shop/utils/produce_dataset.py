from django.contrib.auth.models import User
#from django.conf import settings

#print(settings.AUTH_USER_MODEL)

def produce_dataset():
    dataset = {}

    for user in User.objects.all():
        rating_dict = {}
        for rating in user.rating_set.all().order_by('shop'):
            rating_dict[rating.shop.name] = rating.score
        dataset[user.username] = rating_dict
    return dataset


