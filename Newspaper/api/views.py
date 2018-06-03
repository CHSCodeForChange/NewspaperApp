from django.shortcuts import render, redirect
from Newspaper.models import *
from Newspaper.forms import *

from .serializers import *
from rest_framework import generics
from Newspaper.models import *

class GetPaper(generics.RetrieveAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = NewspaperSerializerWithSections

    def get_queryset(self):
        return Paper.objects.all()



class ListPapers(generics.ListAPIView):
    pass
    serializer_class = NewspaperSerializer

    def get_queryset(self):
        return Paper.objects.all()


class ListSections(generics.ListAPIView):
    serializer_class = SectionSerializer

    def get_queryset(self):
        queryset = Section.objects.all()
        parentPaper_id = self.request.query_params.get('parentPaper_id', None)
        print(parentPaper_id)
        parentPaper = Paper.objects.get(id=parentPaper_id)

        if parentPaper is not None:
            queryset = queryset.filter(parentPaper=parentPaper)
        return queryset
