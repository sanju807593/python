from django.shortcuts import render
from .forms import StudentForm


# Create your views here.
def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'student_form.html', {'form': form})