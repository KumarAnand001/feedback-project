from django.shortcuts import render
from . import forms

# Create your views here.
def thankuView(request):

    return render(request, 'testApp/thanku.html')

def feedbackView(request):

    if request.method == 'GET':

        form = forms.FeedbackForm()
        
    
    
    if request.method == 'POST':

        form = forms.FeedbackForm(request.POST)

        if form.is_valid():

            print('form validation success')
            print('Student Name : ', form.cleaned_data['name'])
            # return thankuView(request)

    return render(request, 'testApp/feedback.html', {'form':form})
    
