from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from first_app.models import School


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'Basic content injected'
        return context


class SchoolListView(ListView):
    model = School
    template_name = 'first_app/school-list.html'
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    model = School
    template_name = 'first_app/school-detail.html'
    context_object_name = 'school_detail'
