from django.shortcuts import render, redirect
from .models import Training
from .ai_train import generate_workout_plan


def configurator(request):
    if request.method == 'POST':
        config = Training()
        config.user = request.user
        config.train_place = request.POST.get('train-place')
        config.train_type = request.POST.get('train-type')
        config.train_program = request.POST.get('train-program')
        config.day_week = request.POST.getlist('day-week')
        config.muscle_groups = request.POST.getlist('muscle-groups')
        config.difficulty = request.POST.get('difficulty')

        config.train_plan = generate_workout_plan(train_place=config.train_place,
                                                train_type=config.train_type,
                                                train_program=config.train_program,
                                                day_week=config.day_week,
                                                muscle_groups=config.muscle_groups,
                                                difficulty=config.difficulty)

        config.save()

        return redirect('users:profile')

    return render(request, 'configurator/configurator.html')

def it_works(request):
    return render(request, 'configurator/itworks.html')
