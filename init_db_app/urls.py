from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from init_db_app.models import put_data

urlpatterns = [
    url(r'^$', ListView.as_view(
                        queryset=put_data.objects.all().order_by("date")[:25],
                        template_name="init_db_app/columns_view.html")),
    url(r'(?P<pk>\d+)$', DetailView.as_view(
                         model = put_data,
                         template_name="init_db_app/put_data.html"))
        ]
