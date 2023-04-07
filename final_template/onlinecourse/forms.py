from django.shortcuts import render
from django.http import HttpResponseRedirect
# <HINT> Import any new Models here
from .models import Question, Choice
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.forms import Form
from django.contrib.auth import login, logout, authenticate

class ChoiceForm(Form):
    def __init__(self, questionId, *args,**kwargs):
        super(forms.Form, self).__init__(args, kwargs)
        question = Question.objects.get_object_or_404(Question, pk=questionId)
        self.selected = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                    queryset=Choices.objects.filter(question=question))
