from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User, Cidade, Estado, Pet_health, Pet_disease_areas, Pet_breed, Pet, Ongs


class SignUpForm(UserCreationForm):
    username = forms.EmailField(required=True, help_text='Informe um e-mail vlido.', label='Email')
    first_name = forms.CharField(required=True, help_text='Informe seu nome.', label='Nome')
    last_name = forms.CharField(required=True, help_text='Informe seu nome.', label='Sobrenome')
    birth_date = forms.DateField(required=True, help_text='Informe sua data de aniversrio', label='Data de Nascimento')
    state_code = forms.ModelChoiceField(queryset=Estado.objects.all(), to_field_name='uf', empty_label="Escolha seu estado", label='Estado')

    city = forms.ModelChoiceField(queryset=Cidade.objects.all(), to_field_name='id', empty_label="Escolha sua cidade", label='Cidade')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2','birth_date','state_code','city' )

class UserUpdateForm(forms.ModelForm):
    username = forms.EmailField(required=True, help_text='Informe um e-mail vlido.', label='Email')
    first_name = forms.CharField(required=True, help_text='Informe seu nome.', label='Nome')
    last_name = forms.CharField(required=True, help_text='Informe seu nome.', label='Sobrenome')
    birth_date = forms.DateField(input_formats=['%d/%m/%Y'], required=True, help_text='Informe sua data de aniversrio', label='Data de Nascimento')
    state_code = forms.ModelChoiceField(queryset=Estado.objects.all(), to_field_name='uf', empty_label="Escolha seu estado", label='Estado')

    city = forms.ModelChoiceField(queryset=Cidade.objects.all(), to_field_name='id', empty_label="Escolha sua cidade", label='Cidade')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','birth_date','state_code','city' )

class PetForm(forms.ModelForm):
    where_was_found_state = forms.ModelChoiceField(queryset=Estado.objects.all(), to_field_name='uf', empty_label="Escolha seu estado", label='Estado')
    where_was_found_city = forms.ModelChoiceField(queryset=Cidade.objects.all(), to_field_name='id', empty_label="Escolha sua cidade", label='Cidade')
    primary_breed = forms.ModelChoiceField(queryset=Pet_breed.objects.all(), to_field_name='id', empty_label="Digite ou escolha")
    secondary_breed = forms.ModelChoiceField(queryset=Pet_breed.objects.all(), to_field_name='id', empty_label="Digite ou escolha", label='Segunda raa')

    class Meta:
        model = Pet
        fields = ('name','is_mixed_breed', 'primary_breed','secondary_breed','where_was_found_state','where_was_found_city','birth_day', 'birth_month','birth_year','species', 'gender', 'size', 'pet_description','color', 'coat','coat_size','qty_preview_adoptions','where_was_found','where_was_found_name','arrival_date','combo_adoption_id','is_microchiped','activity_level','is_basic_trainned','confortable_with_kids','confortable_with_elder','confortable_with_cats','confortable_with_dogs','confortable_with_men','confortable_with_women','is_neutered','was_rabbies_vaccinated_this_year','was_v_vaccinated_this_year','was_others_vaccinated_this_year','video', 'status','walk_pull','walk_pull_hard','walk_dogs','walk_people','walk_fear','teeth_status', 'first_special_need', 'second_special_need', 'third_special_need', 'is_available_adoption','age_category','age','ongs_id','profile_picture','picture_1','picture_2','picture_3','is_walking_daily','is_acupuncture','is_physiotherapy', 'is_vermifuged','is_lice_free','is_dog_meet_necessary','walk_leash','walk_alone','walk_alone_dislike','id_at_ong')


class OngForm(forms.ModelForm):
    state_id = forms.ModelChoiceField(queryset=Estado.objects.all(), to_field_name='uf', empty_label="Escolha seu estado", label='Estado')
    city_id = forms.ModelChoiceField(queryset=Cidade.objects.all(), to_field_name='id', empty_label="Escolha sua cidade", label='Cidade')
    
    class Meta:
        model = Ongs
        fields = ('name','rate', 'hour_open','hour_close','mission_statement','description','web_site', 'phone_number_ddd','phone_number','email', 'facebook', 'instagram', 'logo_link','picture_1', 'picture_2','city_id','state_id','is_foster_ok','is_volunteer_ok','has_transportation','cnpj', 'founded_date','transportation_price')

