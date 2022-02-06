from json import loads
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories, Ads


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CetegoryView(View):
    def get(self, request):
        categories = Categories.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name})
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        cat_new = loads(request.body)
        category = Categories()
        category.name = cat_new["name"]
        category.save()
        return JsonResponse({
            "id": category.id,
            "name": category.name}, status=201)

class CategoryDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
                "id": category.id,
                "name": category.name}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads_set = Ads.objects.all()
        response = []
        for ads in ads_set:
            response.append({
                "id": ads.id,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
                "is_published": ads.is_published})
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        ads_new = loads(request.body)
        ads = Ads()
        ads.name = ads_new["name"]
        ads.author = ads_new["author"]
        ads.price = ads_new["price"]
        ads.description = ads_new["description"]
        ads.address = ads_new["address"]
        ads.is_published = ads_new["is_published"]
        ads.save()
        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "address": ads.address,
            "description": ads.description,
            "is_published": ads.is_published}, status=201)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
                "id": ads.id,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
                "is_published": ads.is_published}, status=200)