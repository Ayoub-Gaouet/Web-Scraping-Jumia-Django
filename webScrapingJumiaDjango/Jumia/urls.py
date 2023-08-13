from django.urls import path
from . import views

# urlpatterns is a list that maps URL paths to view functions
urlpatterns = [
    # Map the URL path 'smartphones/' to the view function 'smartphones' in the views module
    path('smartphones/', views.smartphones, name='smartphones'),

    # Map the URL path 'smartphone_details/' to the view function 'smartphone_details' in the views module
    path('smartphone_details/', views.smartphone_details, name='smartphone_details'),
]
