from django.urls import path,include
from .views import index,create,detail,enrollment,advise,delete

urlpatterns=[
    path('',index,name='index'),
    path('create/',create,name='create'),
    path('detail/<int:content_id>/',detail,name='detail'),
    path('enrollment/<int:timeslot_id>/',enrollment,name='enrollment'),
    path('adivse/<int:timeslot_id>/',advise,name='advise'),
    path('delete/<int:timeslot_id>/',delete,name='delete'),
]