from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chapter, Entry, Exercise
from .forms import ChapterForm, EntryForm, ExerciseForm
from django.contrib.auth.models import User
from django.http import Http404
import os, random, re
# Create your views here.

def index(request):
    return render(request, 'bili/index.html')

@login_required
def chapters(request):
    chapters = Chapter.objects.filter(owner_z=request.user).order_by('date_added')
    context = {'chapters': chapters}
    return render(request, 'bili/chapters.html', context)

@login_required
def new_chapter(request):
    if request.method != 'POST':
        form = ChapterForm()
    else:
        form = ChapterForm(data=request.POST)
        if form.is_valid():
            new_chapter = form.save(commit=False)
            new_chapter.owner_z = request.user
            new_chapter.save()
            return redirect('bili:chapters')
    context = {'form': form}
    return render(request, 'bili/new_chapter.html', context)

@login_required
def new_entry(request,chapter_id):
    context = if_owner(request, "chapter", chapter_id)
    chapter = context['chapter']
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.chapter = chapter
            new_entry.save()
            return redirect('bili:chapter', chapter_id=chapter_id)
    context['form'] = form
    return render(request, 'bili/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    context = if_owner(request, "entry", entry_id)
    chapter = context['chapter']
    entry = context['entry']
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bili:chapter', chapter_id=chapter.id)
    context['form'] = form
    return render(request, 'bili/edit_entry.html', context)

@login_required
def chapter(request, chapter_id):
    chapter =get_object_or_404(Chapter, id=chapter_id)
    if chapter.owner_z != request.user:
        raise Http404
    entries = chapter.entry_set.order_by('-date_added')
    exercises = Exercise.objects.all()
    context = {'chapter': chapter, 'entries': entries, 'exercises': exercises}
    return render(request, 'bili/chapter.html', context)

@login_required
def edit_chapter(request, chapter_id):
    context = if_owner(request, "chapter", chapter_id)
    chapter = context['chapter']
    if request.method != 'POST':
        form = ChapterForm(instance=chapter)
    else:
        form = ChapterForm(instance=chapter, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bili:chapters')
    context['form'] = form
    return render(request, 'bili/edit_chapter.html', context)

@login_required
def new_exercise(request, chapter_id,entry_id):
    context = if_owner(request, "entry", entry_id)
    chapter = context['chapter']
    entry = context['entry']
    if request.method != 'POST':
        form = ExerciseForm()
    else:
        form = ExerciseForm(data=request.POST)
        if form.is_valid():
            new_exercise = form.save(commit=False)
            new_exercise.entry = entry
            new_exercise.save()
            return redirect('bili:chapter', chapter_id=chapter_id)
    context['form'] = form
    return render(request, 'bili/new_exercise.html', context)

@login_required
def exercise(request, exercise_id):
    context = if_owner(request,"exercise",exercise_id)
    return render(request, 'bili/exercise.html', context)

@login_required
def exercise_html(request, exercise_id):
    context = if_owner(request, "exercise", exercise_id)
    exercise = context['exercise']
    road = os.getcwd()
    road1 = 'bili/templates/bili'
    if road1 not in road:
        road = road + "/" + road1
        os.chdir(road)
    for del_file in os.listdir(road):
        if re.search(r'_\d{4}', del_file):
            os.unlink(del_file)
    x = random.randint(1000, 9999)
    html = "exercise_html_" + str(x) + ".html"
    bilihtml = 'bili/' + html
    htmlfile = open(html, 'w')
    htmlfile.write(exercise.text)
    htmlfile.close()
    return render(request, bilihtml, context)

@login_required
def edit_exercise(request, exercise_id):
    context = if_owner(request, "exercise", exercise_id)
    exercise = context['exercise']
    chapter = context['chapter']
    if request.method != 'POST':
        form = ExerciseForm(instance=exercise)
    else:
        form = ExerciseForm(instance=exercise, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bili:chapter', chapter_id=chapter.id)
    context['form'] = form
    return render(request, 'bili/edit_exercise.html', context)

@login_required
def del_exercise(request, exercise_id):
    context = if_owner(request, "exercise", exercise_id)
    chapter = context['chapter']
    if request.method != 'POST':
        return render(request, 'bili/del_con_exercise.html', context)
    else:
        if request.POST.get('yes_or_no', None) == "yes":
            Exercise.objects.filter(id=exercise_id).delete()
    return redirect('bili:chapter', chapter_id=chapter.id)

@login_required
def del_chapter(request, chapter_id):    
    context = if_owner(request, "chapter", chapter_id)
    chapter = context['chapter']
    if request.method != 'POST':
        return render(request, 'bili/del_con_chapter.html', context)
    else:
        if request.POST.get('yes_or_no', None) == "yes":
            Chapter.objects.filter(id=chapter_id).delete()
    return redirect('bili:chapters')

@login_required
def del_entry(request, entry_id):
    context = if_owner(request, "entry", entry_id)
    chapter = context['chapter']
    
    if request.method != 'POST':
        return render(request, 'bili/del_con_entry.html', context)
    else:
        if request.POST.get('yes_or_no', None) == "yes":
            Entry.objects.filter(id=entry_id).delete()
    return redirect('bili:chapter', chapter_id=chapter.id)

@login_required
def if_owner(request_obj, id_name, id_value):
    if id_name == "chapter":
        chapter = Chapter.objects.get(id=id_value)
        context = {"chapter":chapter}
    if id_name == "entry":
        entry = Entry.objects.get(id=id_value)
        chapter = entry.chapter
        context = {"chapter":chapter, "entry":entry}
    if id_name == "exercise":
        exercise = Exercise.objects.get(id=id_value)
        entry = exercise.entry
        chapter = entry.chapter
        context = {"chapter":chapter, "entry":entry, "exercise":exercise}
    if chapter.owner_z != request_obj.user:
        raise Http404
    return context




@login_required
def goto(request):
    print(request.POST.get('user'),request.POST.get('pwd'))
    print(request.POST)
    print(request.POST.getlist('skill'))
    return render(request, 'bili/index.html')
