from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('military', views.military, name='military'),
    path('type_troops', views.type_troops,name='type_troops'),
    path('companies', views.companies,name='companies'),
    path('employees', views.employees,name='employees'),
    path('dislocation', views.dislocation,name='dislocation'),
    path('create', views.create,name='create'),
    path('create2', views.create2,name='create2'),
    path('create3', views.create3,name='create3'),
    path('create4', views.create4,name='create4'),
    path('create5', views.create5,name='create5'),
    path('military/<int:pk>', views.NewsDetailView.as_view(), name='details_view'),
    path('type_troops/<int:pk>', views.NewsDetailView2.as_view(), name='details_view2'),
    path('companies/<int:pk>', views.NewsDetailView3.as_view(), name='details_view3'),
    path('mane/<int:pk>', views.NewsDetailView4.as_view(), name='details_view4'),
    path('dislocation/<int:pk>', views.NewsDetailView5.as_view(), name='details_view5'),
    path('military/<int:pk>/update', views.NewsUpdateView.as_view(), name='update'),
    path('type_troops/<int:pk>/update', views.NewsUpdateView2.as_view(), name='update2'),
    path('companies/<int:pk>/update', views.NewsUpdateView3.as_view(), name='update3'),
    path('employees/<int:pk>/update', views.NewsUpdateView4.as_view(), name='update4'),
    path('dislocation/<int:pk>/update', views.NewsUpdateView5.as_view(), name='update5'),
    path('military/<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete'),
    path('type_troops/<int:pk>/delete', views.NewsDeleteView2.as_view(), name='delete2'),
    path('companies/<int:pk>/delete', views.NewsDeleteView3.as_view(), name='delete3'),
    path('employees/<int:pk>/delete', views.NewsDeleteView4.as_view(), name='delete4'),
    path('dislocation/<int:pk>/delete', views.NewsDeleteView5.as_view(), name='delete5'),

]