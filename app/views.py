from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.gis.geoip2 import GeoIP2

class IPAddressView(APIView):

    def get(self, request, *args, **kwargs):
        """
        Handle GET request
        """
        return render(request, 'home.html')

    def post(self, request, *args, **kwargs):
        """
        Handle POST request
        """
        try:
            x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
            if x_forwarded_for:
                ip = x_forwarded_for.split(",")[0]
            else:
                ip = request.META.get("REMOTE_ADDR")
            g = GeoIP2()
            try:
                geo_data = g.city(ip)
                return render(request, "home.html", {"response": geo_data})
            except Exception as e:
                return render(request, "home.html", {"response": str(e)})
        except Exception as e:
            return render(request, "home.html", {"response": str(e)})
