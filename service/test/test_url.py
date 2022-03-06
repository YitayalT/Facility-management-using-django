from importlib.resources import path
from django.urls import reverse, resolve


class TestUrl:
    def test_detail_url(self):
        path = reverse('service_detail', kwargs={'id':1})
        assert resolve(path).view_name == 'service_detail'


