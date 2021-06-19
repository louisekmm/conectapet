from django.http import HttpResponseRedirect,HttpResponse #Http404, 
from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from django.urls import reverse,reverse_lazy
from django.views import generic
from .models import Ongs,Cidade, Estado,Pet, User,Pet_health,Pet_disease,Pet_disease_areas, Pet_breed, Ongs,Favorites
from .forms import SignUpForm, UserUpdateForm, PetForm, OngForm
from django.contrib.auth import login, authenticate
#from django.contrib.auth.models import User
from django.conf import settings
from django.template import loader, RequestContext
import datetime
from django.contrib import messages
from django.db.models import Case, When


class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Cidade

def load_cities(request):
    if 'type' not in request.GET:
        loaded_field=""
        state_name = Estado.objects.get(uf=request.GET.get('estado'))
        cities = Cidade.objects.filter(estado_uf=state_name).order_by('nome')
    else:
        loaded_field=request.GET.get('type')
        if loaded_field == 'all':
            cities = Cidade.objects.order_by('nome')
        elif loaded_field == 'ongs':
            #ong_cidade = Ongs.objects.get('city_id_id')
            #cities = Cidade.objects.filter(id=ong_cidade).order_by('nome')
            cities = Cidade.objects.order_by('nome')
        else:
            state_name = Estado.objects.get(uf=request.GET.get('estado'))
            cities = Cidade.objects.filter(estado_uf=state_name).order_by('nome')
        
    return render(request, 'cidade_dropdown.html', {'cities': cities, 'loaded_field': loaded_field})
    
def load_breeds(request):
    if 'type' not in request.GET:
        loaded_field=""

    else:
        loaded_field=request.GET.get('type')
    
    ids_at_top = [349, 322, 350]
    order = Case(*[When(id=id, then=pos) for pos, id in enumerate(ids_at_top)])
    breeds = Pet_breed.objects.order_by(order,'name')
    
        
    return render(request, 'breed_dropdown.html', {'breeds': breeds, 'loaded_field': loaded_field})

        
class PetList(generic.ListView):
    model = Pet
    paginate_by = 6

    def get_queryset(self):
        filter_criteria = self.kwargs.get('type') # se fosse .com/?type='2' faria self.request.GET.get('type')

        if  'city' not in self.request.GET:
            ong_value = ""
        else:
            if self.request.GET.get('city') is None or self.request.GET.get('city') == '':
                ong_value = ""
            else:
                city_value = self.request.GET.get('city')
                ong_value = Ongs.objects.filter(city_id=city_value)

        if  'size' not in self.request.GET:
            size_value = ""
        else:
            if self.request.GET.get('size') is None or self.request.GET.get('size') == '' or 'all' in self.request.GET.get('size'):
                size_value = ""
            else:
                size_value = self.request.GET.get('size').split('0')
        
        if 'breed' not in self.request.GET:
            breed_value = ""
        else: 
            if self.request.GET.get('breed') is None or self.request.GET.get('breed') == '' or 'all' in self.request.GET.get('breed'):
                breed_value = ""
            else:   
                breed_value = self.request.GET.get('breed').split('a')

        if  'age' not in self.request.GET:
            age_value = ""
        else:
            if self.request.GET.get('age') is None or self.request.GET.get('age') == '' or 'all' in self.request.GET.get('age'):
                age_value = ""
            else:
                age_value = self.request.GET.get('age').split('0')

        if 'fem' not in self.request.GET and 'mac' not in self.request.GET:
            gender_value = ""
        else:
            if (self.request.GET.get('fem')=="false" and self.request.GET.get('mac') == "false") or (self.request.GET.get('fem')=="true" and self.request.GET.get('mac') == "true"):    
                gender_value = ""
            elif self.request.GET.get('fem')=="true" and self.request.GET.get('mac') == "false":
                gender_value="Fêmea"
            else:
                gender_value="Macho"

        if 'dog' not in self.request.GET and 'cat' not in self.request.GET:
            species_value = ""
        else:
            if (self.request.GET.get('dog')=="false" and self.request.GET.get('cat') == "false") or (self.request.GET.get('dog')=="true" and self.request.GET.get('cat') == "true"):    
                species_value = ""
            elif self.request.GET.get('dog')=="true" and self.request.GET.get('cat') == "false":
                species_value="Cachorro"
            else:
                species_value="Gato"

        #so para manage
        if  'pet' not in self.request.GET:
            pet_value = ""
        else:
            if self.request.GET.get('pet') is None or self.request.GET.get('pet') == '':
                pet_value = ""
            else:
                pet_value = self.request.GET.get('pet')

        if  'color' not in self.request.GET:
            color_value = ""
        else:
            if self.request.GET.get('color') is None or self.request.GET.get('color') == '' or 'all' in self.request.GET.get('color'):
                color_value = ""
            else:
                color_value = self.request.GET.get('color').split('0')

        if  'coat' not in self.request.GET:
            coat_value = ""
        else:
            if self.request.GET.get('coat') is None or self.request.GET.get('coat') == '' or 'all' in self.request.GET.get('coat'):
                coat_value = ""
            else:
                coat_value = self.request.GET.get('coat').split('0')

        #ordenacao
        if 'sort' not in self.request.GET:
            if filter_criteria == 'manage':
                asc_desc = 'asc'
                sort_value = 'name'
            else:
                asc_desc = 'desc'
                sort_value = 'created_at'  
        else:
            asc_desc = self.request.GET.get('sort').split('-')[1]
            sort_value = self.request.GET.get('sort').split('-')[0]

        if filter_criteria == 'manage':
            user_ong = User.objects.get(id=self.request.user.id).ongs_id_id

            if asc_desc == 'asc': 
                results = Pet.objects.filter(ongs_id_id=user_ong).order_by(sort_value)
            else:
                results = Pet.objects.filter(ongs_id_id=user_ong).order_by('-'+sort_value)

            
        #not manage
        else:
            
            if asc_desc == 'asc': 
                results = Pet.objects.filter(is_available_adoption=1, is_neutered=1).order_by(sort_value)
            else:
                results = Pet.objects.filter(is_available_adoption=1, is_neutered=1).order_by('-'+sort_value)

        #filtros
        if size_value != "" and size_value != "all":
            results = results.filter(size__in=[s for s in size_value])
        
        if age_value != "" and age_value != "all":
            results = results.filter(age_category__in=[a for a in age_value])

        if color_value != "" and color_value != "all":
            results = results.filter(color__in=[a for a in color_value])

        if coat_value != "" and coat_value != "all":
            results = results.filter(coat_size__in=[a for a in coat_value])

        if breed_value != "" and breed_value != "all":
            results = results.filter(primary_breed_id__in=[b for b in breed_value])

        if gender_value != "":
            results = results.filter(gender = gender_value)

        if species_value != "":
            results = results.filter(species = species_value)

        if ong_value != "":
            results = results.filter(ongs_id_id__in=[o for o in ong_value])

        if pet_value != "":
            if pet_value.isdigit():
                results = results.filter(id_at_ong = pet_value)
            else:
                results = results.filter(name__contains = pet_value) 

        return results

    def get_template_names(self):
        filter_criteria = self.kwargs.get('type')

        if filter_criteria == 'manage':
            template_name = 'pet_list_manage.html'
        elif filter_criteria == 'show_order_m':
            template_name = 'pet_list_manage_search.html'
        elif filter_criteria == 'show_order':
            template_name = 'pet_list_search.html'
        else:
            template_name = 'pet_list.html'

        return template_name

class PetView(generic.DetailView):
    model = Pet

class PetCreate(generic.CreateView):
    model = Pet
    form_class = PetForm

    def get_success_url(self):
        return reverse_lazy('pet_list', kwargs={'type': 'manage'})


class PetUpdate(generic.UpdateView):
    model = Pet
    form_class = PetForm

    def get_success_url(self):
        return reverse_lazy('pet_list', kwargs={'type': 'manage'})
    
    def get_template_names(self):
        return 'pet_update.html'

    
class PetDelete(generic.DeleteView):
    model = Pet
    success_url = reverse_lazy('pet_list', kwargs={'type': 'manage'})

def favorite_status(request):
    type_fav = request.GET.get('type')
    qty_favorites = int(Pet.objects.get(id=request.GET.get('pet_id')).qty_favorites)

    if Favorites.objects.filter(pet_id_id=request.GET.get('pet_id'), user_id_id=request.user.id).exists():
        if type_fav == 'load':
            return HttpResponse("<label style='color: #e63e62;margin-right: 2px' title='Faça login para favoritar esse pet'><span class='fas fa-heart'></span></label>")
        else:
            Favorites.objects.filter(pet_id_id=request.GET.get('pet_id'), user_id_id=request.user.id).delete()
            Pet.objects.filter(id=request.GET.get('pet_id')).update(qty_favorites=qty_favorites-1)
            return HttpResponse("<label style='color: #e63e62;margin-right: 2px' title='Faça login para favoritar esse pet'><span class='fas fa-heart' style='font-weight: 400;'></span></label>")
    else:
        if type_fav == 'load':
            return HttpResponse("<label style='color: #e63e62;margin-right: 2px' title='Faça login para favoritar esse pet'><span class='fas fa-heart' style='font-weight: 400;'></span></label>")
        else:
            Favorites.objects.create(pet_id_id=request.GET.get('pet_id'), user_id_id=request.user.id)
            Pet.objects.filter(id=request.GET.get('pet_id')).update(qty_favorites=qty_favorites+1)
            return HttpResponse("<label style='color: #e63e62;margin-right: 2px' title='Faça login para favoritar esse pet'><span class='fas fa-heart'></span></label>")
        
def load_combo_adoption(request):
    pet_id = request.GET.get('pet_id')
    user_ong = User.objects.get(id=request.user.id).ongs_id_id
    type_request = request.GET.get('type')
    
    if 'combo_id' not in request.GET:
        combo_id = 0
    else:
        combo_id = request.GET.get('combo_id')
    
    if type_request == 'create':
        if 'word' not in request.GET:
            pet_ids = Pet.objects.filter(ongs_id_id=user_ong, is_available_adoption=1, combo_adoption_id=0, is_neutered=1).order_by('name')
        else:
            pet_searched = request.GET.get('word')
            if pet_searched.isdigit():
                pet_ids = Pet.objects.filter(ongs_id_id=user_ong, is_available_adoption=1, combo_adoption_id=0,  is_neutered=1, id=pet_searched).order_by('name')
            else:
                pet_ids = Pet.objects.filter(ongs_id_id=user_ong, is_available_adoption=1, combo_adoption_id=0, is_neutered=1, name__contains=pet_searched).order_by('name')
    else:
        pet_id = request.GET.get('pet_id')
        if 'word' not in request.GET:
            pet_ids = Pet.objects.filter(ongs_id_id=user_ong).exclude(id=pet_id).order_by('name')
        else:
            pet_searched = request.GET.get('word')
            if pet_searched.isdigit():
                pet_ids = Pet.objects.filter(ongs_id_id=user_ong, is_available_adoption=1, combo_adoption_id=0, is_neutered=1, id=pet_searched).exclude(id=pet_id).order_by('name')
            else:
                pet_ids = Pet.objects.filter(ongs_id_id=user_ong, is_available_adoption=1, combo_adoption_id=0, is_neutered=1, name__contains=pet_searched).exclude(id=pet_id).order_by('name')
   

    return render(request, 'combo_adoption_dropdown.html', {'pet_ids': pet_ids,'type_request': type_request,'combo_id': combo_id})       
    
def available_adopt_status(request):
    pet_id = request.GET.get('pet_id')
    reason = request.GET.get('available_status')
    pet_obj = Pet.objects.get(id=pet_id)

    if reason == 'Disponível':
        pet_obj.is_available_adoption = 1
        pet_obj.save()
        return HttpResponse('Disponível para adoção')
    else:
        pet_obj.is_available_adoption = 0
        pet_obj.status = reason
        pet_obj.save()
        return HttpResponse(reason)

def add_combo_adoption(request):
    pet_id_combo = request.GET.get('pet_id_combo')
    pet_id_add = request.GET.get('pet_id')

    pet_obj = Pet.objects.get(id=pet_id_combo)

    if pet_id_add == 0 and request.GET.get('type') == 'create':
        pet_obj_add= Pet.objects.latest('id')
        pet_obj.combo_adoption_id = pet_obj_add.id
    elif request.GET.get('type') == 'remove':
        pet_obj.combo_adoption_id = 0
        pet_obj_add = Pet.objects.get(id=pet_id_add)
        pet_obj_add.combo_adoption_id = 0
        pet_obj_add.save()
    else:
        pet_obj.combo_adoption_id = pet_id_add

    pet_obj.save()
    
def check_ids_pet(request):
    id_check = request.GET.get('id_check')
    ong = request.GET.get('id_ong')

    if Pet.objects.filter(id_at_ong=id_check, ongs_id_id=ong).exists():
        return HttpResponse("<label style='color:red;'><span class='fas fa-times'></span> ID "+id_check+" já existe</label>")
    else:
        return HttpResponse("<label style='color:green;'><span class='fas fa-check'></span> ID disponível</label>")
