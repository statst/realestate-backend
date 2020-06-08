from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView 
from rest_framework import permissions
from .models import Listestates
from .serializers import ListestatesSerializer, listestatesDetailSerializer
from datetime import datetime, timezone, timedelta
# Create your views here.

class ListestatesView(ListAPIView):
    queryset = Listestates.objects.order_by('-list_date').filter(is_published=True)
    permissions_classes=(permissions.AllowAny, )
    serializer_class = ListestatesSerializer
    lookup_field = 'slug'

class ListestateView(RetrieveAPIView):
    queryset = Listestates.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = listestatesDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListestatesSerializer

    def post(self, request, format = None):
        queryset = Listestates.objects.order_by('-list_date').filter(is_published=True)
        data= self.request.data
        print(queryset)
        sale_type = data('sale_type')
        queryset = queryset.filter(sale_type__iexact=sale_type)
        price_ = data['price']
        price=[''.join(re.findall('[0-9]+',i)) for i in price_]
        if price != -1:
            queryset = queryset.filter(price >= price)

        bedrooms_ = data['bedrooms']
        bedrooms=[''.join(re.findall('[0-9]+',i)) for i in bedrooms_]

        queryset = queryset.filter(bedrooms >= bedrooms)

        home_type = data ['home_type']
        queryset = queryset.filter(home_type__iexact = home_type)

        bathrooms_ = data['bathrooms']
        bathrooms=[''.join(re.findall('[0-9]+',i)) for i in bathrooms_]

        queryset = queryset.filter(bathrooms >= bathrooms)

        sqft_ = data['sqft']
        sqft=[''.join(re.findall('[0-9]+',i)) for i in sqft_]

        if sqft != 0:
            queryset = queryset.filter(sqft >= sqft)

        days_passed_ = data['days_listed']
        days_passed=[''.join(re.findall('[0-9]+',i)) for i in days_passed_]

        for query in queryset:
            num_days = (datetime.now(timezone.utc)- query.list_date).days

            if days_passed !=0:
                if num_days > days_passed:
                    slug = query.slugqueryset = queryset.exclude(slug__iexact=slug)

        has_photos_ = data['has_photos']
        has_photos=[''.join(re.findall('[0-9]+',i)) for i in has_photos_]

        def pic(i):
            if 'i.photo_'+i:
                count += 1
        
        for query in queryset:
            count = 0
            pic(query)          
            if count < with_photos:
                slug = query.slug
                queryset = queryset.exclude(slug__iexact=slug)

        open_house = data['open_house']
        queryset = queryset.filter(open_house__iexact=open_house)

        keywords = data['keywords']
        queryset = queryset.filter(description_icontains=keywords)

        serializer = ListestatesSerializer(queryset, many = True)

        return Response(serializer.data)
