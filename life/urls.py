# api/urls.py reduce_digit_view,index,
from django.urls import path
from .views import index2,destiny_number_view,privacy_page
from . import views

urlpatterns = [
    # path('home/', reduce_digit_view, name='reduce_digit'),
    # path('', index, name='index'),
    path('index2/', index2, name='index2'),
    path('list',index2 , name='list'),
    path('jewish_birth', views.all_period, name='all_period'),
    path('yearly_cycle/', views.yearly_cycle, name='yearly_cycle'),
    # path('zodiac-image/', views.get_zodiac_image, name='zodiac-image'),
    # path('convert-date/', views.convert_date, name='convert_date'),
    path('', views.tikkun, name='tikkun'),
    path('privacy/', views.privacy_page, name='privacy-page'),

    # path('period/<int:id>/', views.detail_page, name='detail_page'),

    
    # path('main_page', views.main_page, name='main_page'),
    path('main_page', views.main_page, name='main_page'),  # Default view without a selected period
    path('<int:id>/', views.main_page, name='main_page_with_detail'),  # View with a selected period


    # path('period/<int:id>/', views.detail_page, name='detail_page'), 



    # path('<int:id>/', views.main_page, name='main_page'),


    # path('yearly_cycle_view/', views.yearly_cycle_view, name='yearly_cycle2'),
    # path('hebrew_date_view/', views.hebrew_date_view, name='hebrew_date'),
    # path('display_period/', views.display_period, name='dispaly_period'),
    path('destiny-number/', destiny_number_view, name='destiny_number'),

    # path('list',current_year , name='list'),
]
