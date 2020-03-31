from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from page.forms import FeedbackForm
from page.models import Comment


class IndexView(TemplateView):
    template_name = 'page/index.html'


class FeedbackView(FormView):
    template_name = 'page/feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('page:feedback')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        text = form.cleaned_data['comment']
        comment = Comment(name=name, comment=text)
        comment.save()
        return super(FeedbackView, self).form_valid(form)

    def form_invalid(self, form):
        print('=============================')
        return super(FeedbackView, self).form_invalid(form)


class ContactView(TemplateView):
    template_name = 'page/contact.html'
