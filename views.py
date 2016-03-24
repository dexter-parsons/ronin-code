from django.shortcuts import render, render_to_response, RequestContext
from django.core.urlresolvers import reverse
import forms
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.contrib import auth
from django.core.context_processors import csrf
from goals.models import Goals, Goals_log, Goalsco

"""class SiteViewer(CreateView):
	model = Goals
	template_name = 'base.html'

"""
class ListGoalsView(ListView):

    model = Goals
    template_name = 'goals.html'
    form_class = forms.GoalsForm 

class CreateGoalsView(CreateView):

    model = Goals
    template_name = 'edit_goals.html'
    form_class = forms.GoalsForm
    #form_class = forms.GoalsForm
    
    def get_success_url(self):
        return reverse('goals-create')

    def get_context_data(self, **kwargs):
    	kwargs['object_list'] = Goals.objects.order_by('id')
        return super(CreateGoalsView, self).get_context_data(**kwargs)
        
def UserDetails():
    model = Goals_log
    template_name = 'goals.html'
    meta['users'] = request.POST.get('users','')





"""
class UpdateGoalsView(UpdateView):

    model = Goals
    template_name = 'goals.html'

    def get_success_url(self):
        return reverse('goals-list')    

    def get_context_data(self, **kwargs):

        context = super(UpdateGoalsView, self).get_context_data(**kwargs)
        context['action'] = reverse('goals-new',
                                    kwargs={'pk': self.get_object().id})

        return context        
"""
"""
class DeleteGoalsView(DeleteView):

    model = Goals
    template_name = 'goals.html'

    def get_success_url(self):
        return reverse('goals-list') 

#class ListUsersView(ListView):

 #   model = Goals_log
  #  template_name = 'goals.html'
"""

