from django.shortcuts import render
from .models import Equipement
from .models import Animal
from .forms import MoveForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
def animaux(request):
    Animaux = Animal.objects.filter()
    return render(request, 'blog/Animaux.html', {'Animaux' : Animaux})

def equipements(request):
    Equipements = Equipement.objects.filter()
    return render(request, 'blog/Equipements.html', {'Equipements' : Equipements})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    lieu = animal.lieu
    form=MoveForm()
    return render(request, 'blog/animal_detail.html', {'animal': animal, 'lieu': lieu, 'form': form})

def Tic (request):
    Tic = Animal.objects.get(id_animal="Tic")
    lieu = Tic.lieu
    form=MoveForm()
    return render(request, 'blog/Tic.html', {'animal': Tic, 'lieu': lieu, 'form': form})

def Pocahontas (request):
    Pocahontas = Animal.objects.get(id_animal="Pocahontas")
    lieu = Pocahontas.lieu
    form=MoveForm()
    return render(request, 'blog/Pocahontas.html', {'animal': Pocahontas, 'lieu': lieu, 'form': form})

def Totora (request):
    Totora = Animal.objects.get(id_animal="Totora")
    lieu = Totora.lieu
    form=MoveForm()
    return render(request, 'blog/Totora.html', {'animal': Totora, 'lieu': lieu, 'form': form})

def Patrick (request):
    Patrick = Animal.objects.get(id_animal="Patrick")
    lieu = Patrick.lieu
    form=MoveForm()
    return render(request, 'blog/Patrick.html', {'animal': Patrick, 'lieu': lieu, 'form': form})

def Tac (request):
    Tac = Animal.objects.get(id_animal="Tac")
    lieu = Tac.lieu
    form=MoveForm()
    if form.is_valid():
        ancien_lieu = get_object_or_404(Equipement, id_equip=Tac.lieu.id_equip)
        ancien_lieu.disponibilite = True
        ancien_lieu.save()
        form.save()
        nouveau_lieu = get_object_or_404(Equipement, id_equip=Tac.lieu.id_equip)
        nouveau_lieu.disponibilite = False
        nouveau_lieu.save()
        return redirect('Tac', Tac=Tac)
    else:
        form = MoveForm()
        return render(request,'blog/Tac.html',{'animal': Tac, 'lieu': lieu, 'form': form})
