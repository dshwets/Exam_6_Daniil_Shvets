from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from webapp.models import Feedback
from webapp.forms import FeedbackForm


def index_view(request):
    if request.method == 'GET':
        feedbacks = Feedback.objects.filter(status='active').order_by('-created_at')
        context = {
            'feedbacks': feedbacks
        }
        return render(request, 'index.html', context)


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index_view')


def create_feedback(request):
    if request.method == 'GET':
        return render(request, 'create_feedback.html', context={
            'form': FeedbackForm()
        })
    elif request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            feedback = Feedback.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )
            return redirect('index')
        else:
            return render(request, 'create_feedback.html', context={
                'form': form
            })


def update_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'GET':
        form = FeedbackForm(initial={
            'name': feedback.name,
            'email': feedback.email,
            'text': feedback.text,
        })
        return render(request, 'feedback_update.html', context={'form': form,
                                                                'feedback': feedback})
    elif request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            feedback.name = form.cleaned_data['name']
            feedback.email = form.cleaned_data['email']
            feedback.text = form.cleaned_data['text']
            feedback.save()
            return redirect('index', )
        else:
            return render(request, 'feedback_update.html', context={'form': form,
                                                                    'feedback': feedback})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
