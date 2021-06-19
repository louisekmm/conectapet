import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Estado(models.Model):
    nome = models.CharField(null=True, blank=True, max_length=75)
    uf = models.CharField(null=True, blank=True, max_length=5)

    def __str__(self):
        return self.uf

class Cidade(models.Model):
    nome = models.CharField(null=True, blank=True, max_length=120)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    estado_uf = models.CharField(null=True, blank=True, max_length=5)

    def __str__(self):
        return self.nome

class Ongs(models.Model):

    ADOPTION_VALUE = [ 
        ('Gratuito', 'Gratuito'),
        ('10,00', '10,00'), 
        ('15,00', '15,00'), 
        ('20,00', '20,00'),
        ('25,00', '25,00'), 
        ('30,00', '30,00'), 
        ('35,00', '35,00'), 
        ('40,00', '40,00'),
        ('45,00', '45,00'), 
        ('50,00', '50,00'), 
        ('55,00', '55,00'), 
        ('60,00', '60,00'),
        ('65,00', '65,00'), 
        ('70,00', '70,00'),
        ('75,00', '75,00'), 
        ('80,00', '80,00'), 
        ('85,00', '85,00'), 
        ('90,00', '90,00'),
        ('95,00', '95,00'), 
        ('100,00', '100,00'), 
    ]


    OPEN_HOURS = [ 
        ('06:00', '06:00'),
        ('06:30', '06:30'), 
        ('07:00', '07:00'), 
        ('07:30', '07:30'),
        ('08:00', '08:00'), 
        ('08:30', '08:30'), 
        ('09:00', '09:00'), 
        ('09:30', '09:30'),
        ('10:00', '10:00'), 
        ('10:30', '10:30'), 
        ('11:00', '11:00'), 
        ('11:30', '11:30'),
        ('12:00', '12:00'), 
        ('12:30', '12:30'),
    ]

    CLOSE_HOURS = [ 
        ('16:00', '16:00'),
        ('16:30', '16:30'), 
        ('17:00', '17:00'), 
        ('17:30', '17:30'),
        ('18:00', '18:00'), 
        ('18:30', '18:30'), 
        ('19:00', '19:00'), 
        ('19:30', '19:30'),
        ('20:00', '20:00'), 
        ('20:30', '20:30'), 
        ('21:00', '21:00'), 
        ('21:30', '21:30'),
        ('22:00', '22:00'), 
        ('22:30', '22:30'),
    ]

    DDD = [ 
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('21', '21'),
        ('22', '22'),
        ('24', '24'),
        ('27', '27'),
        ('28', '28'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('37', '37'),
        ('38', '38'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
        ('48', '48'),
        ('49', '49'),
        ('51', '51'),
        ('53', '53'),
        ('54', '54'),
        ('55', '55'),
        ('61', '61'),
        ('62', '62'),
        ('63', '63'),
        ('64', '64'),
        ('65', '65'),
        ('66', '66'),
        ('67', '67'),
        ('68', '68'),
        ('69', '69'),
        ('71', '71'),
        ('73', '73'),
        ('74', '74'),
        ('75', '75'),
        ('77', '77'),
        ('79', '79'),
        ('81', '81'),
        ('82', '82'),
        ('83', '83'),
        ('84', '84'),
        ('85', '85'),
        ('86', '86'),
        ('87', '87'),
        ('88', '88'),
        ('89', '89'),
        ('91', '91'),
        ('92', '92'),
        ('93', '93'),
        ('94', '94'),
        ('95', '95'),
        ('96', '96'),
        ('97', '97'),
        ('98', '98'),
        ('99', '99'),
    ]

    TRANSPORTATION = [ 
        ('Grtis', 'Grtis'),
        ('1,00', '1,00'), 
        ('2,00', '2,00'), 
        ('3,00', '3,00'),
        ('4,00', '4,00'), 
        ('5,00', '5,00'), 
        ('7,00', '7,00'), 
        ('10,00', '10,00'),
        ('12,00', '12,00'), 
        ('15,00', '15,00'), 
        ('18,00', '18,00'), 
        ('20,00', '20,00'),
        ('25,00', '25,00'), 
        ('30,00', '30,00'),
        ('35,00', '35,00'), 
        ('40,00', '40,00'), 
        ('45,00', '45,00'), 
        ('50,00', '50,00'),
        ('55,00', '65,00'), 
        ('60,00', '60,00'), 
    ]
    name = models.CharField(null=True, blank=True, max_length=40)
    rate = models.CharField(null=True, blank=True, default='Gratuito', max_length=8, choices=ADOPTION_VALUE)
    hour_open = models.CharField(blank=True, null=True, default='', max_length=5, choices=OPEN_HOURS)
    hour_close = models.CharField(blank=True, null=True, default='', max_length=5, choices=CLOSE_HOURS) 
    mission_statement = models.CharField(null=True, blank=True, default='', max_length=300)
    description = models.CharField(null=True, blank=True, default='', max_length=500)
    web_site = models.CharField(null=True, blank=True, max_length=150)
    phone_number_ddd = models.CharField(null=True, blank=True, max_length=3, choices=DDD)
    phone_number = models.CharField(null=True, blank=True, max_length=12)
    email = models.CharField(null=True, blank=True, max_length=100)
    facebook = models.CharField(null=True, blank=True, max_length=100)
    instagram = models.CharField(null=True, blank=True, max_length=40)
    logo_link = models.ImageField(null=True, blank=True)
    picture_1 = models.ImageField(null=True, blank=True)
    picture_2 = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    city_id = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True, blank=True)
    state_id = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
    is_foster_ok = models.BooleanField(default=0)
    is_volunteer_ok = models.BooleanField(default=0)
    has_transportation = models.BooleanField(default=0)
    cnpj = models.CharField(null=True, blank=True, max_length=18)
    founded_date = models.CharField(null=True, blank=True, max_length=30, default='')
    is_approved = models.BooleanField(default=0)
    transportation_price = models.CharField(null=True, blank=True, max_length=7, choices=TRANSPORTATION)
    
    def __str__(self):
        return self.name

class User(AbstractUser):

    PERMISSION = [
        ('Editar tudo', 'Editar tudo'),  
        ('Editar equipe e pets', 'Editar equipe e pets'),
        ('Editar pets', 'Editar pets'),
        ('Visualizar equipe e pets', 'Visualizar equipe e pets'),
        ('Visualizar pets', 'Visualizar pets'),
    ]

    ROLE = [
        ('Advogado(a)', 'Advogado(a)'),
        ('Auxiliar de veterinrio', 'Auxiliar de veterinrio'),
        ('Bilogo(a)', 'Bilogo(a)'),  
        ('Colaborador(a)', 'Colaborador(a)'),  
        ('Departamento administrativo', 'Departamento administrativo'),
        ('Departamento de atendimento', 'Departamento de atendimento'),        
        ('Departamento de eventos', 'Departamento de eventos'),
        ('Departamento educativo', 'Departamento educativo'),         
        ('Departamento de marketing', 'Departamento de marketing'),       
        ('Departamento financeiro', 'Departamento financeiro'),
        ('Diretor(a) administrativo', 'Diretor(a) administrativo'),
        ('Diretor(a) de eventos', 'Diretor(a) de eventos'),
        ('Diretor(a) financeiro', 'Diretor(a) financeiro'),
        ('Diretor(a) geral', 'Diretor(a) geral'),
        ('Diretor(a) marketing', 'Diretor(a) marketing'),          
        ('Diretor(a) tcnico', 'Diretor(a) tcnico'),        
        ('Funcionrio(a)', 'Funcionrio(a)'),
        ('Fundador(a)', 'Fundador(a)'),  
        ('Presidente', 'Presidente'),
        ('Protetor(a) associado', 'Protetor(a) associado'),
        ('Secretrio(a)', 'Secretrio(a)'),
        ('Suplente de secretrio', 'Suplente de secretrio'),
        ('Suplente de presidente', 'Suplente de presidente'),
        ('Suplente de vice-presidente', 'Suplente de vice-presidente'), 
        ('Tesoreiro(a)', 'Tesoreiro(a)'),        
        ('Veterinrio(a)', 'Veterinrio(a)'),
        ('Vice-presidente', 'Vice-presidente'),
        ('Voluntrio(a)', 'Voluntrio(a)'),
    ]

    permission_ong = models.CharField(null=True, blank=True, max_length=30, choices=PERMISSION)
    role_ong = models.CharField(null=True, blank=True, max_length=30, choices=ROLE)
    birth_date = models.DateField(null=True, blank=True)
    has_confirmed_email = models.BooleanField(default=0)
    country = models.CharField(null=True, blank=True, max_length=50)
    state_code = models.CharField(null=True, blank=True, max_length=3)
    city = models.CharField(null=True, blank=True, max_length=50)
    neighborhood = models.CharField(null=True, blank=True, max_length=50)
    rg = models.CharField(null=True, blank=True, max_length=12)
    cpf = models.CharField(null=True, blank=True, max_length=15)
    phone_number_ddd = models.CharField(null=True, max_length=3)
    phone_number = models.CharField(null=True, blank=True, max_length=10)
    address_street = models.CharField(null=True, blank=True, max_length=70)
    address_number = models.CharField(null=True, blank=True, max_length=6)
    address_complement = models.CharField(null=True, blank=True, max_length=10)
    postal_code = models.CharField(null=True, blank=True, max_length=10)
    facebook_id = models.CharField(null=True, blank=True, max_length=30)    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) 
    ongs_id = models.ForeignKey(Ongs, on_delete=models.SET_NULL, null=True, blank=True)

class Pet_breed(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    species = models.CharField(null=True, blank=True, max_length=30)

    def __str__(self):
        return self.name    

class Pet(models.Model):

    COLOR_OF_PETS = [
        ('Amarelo', 'Amarelo'), 
        ('Branco', 'Branco'), 
        ('Cinza', 'Cinza'), 
        ('Creme', 'Creme'),
        ('Laranja', 'Laranja'),
        ('Marrom', 'Marrom'), 
        ('Preto', 'Preto'),  
    ]

    COLOR_PATTERN_OF_PETS = [
        ('Arlequim', 'Arlequim'),
        ('Belton', 'Belton'),  
        ('Bicolor', 'Bicolor'), 
        ('Fulvo','Fulvo'),
        ('Lobeiro', 'Ruo'), 
        ('Merle', 'Merle'),
        ('Pintaigado', 'Pintaigado'), 
        ('Ruo', 'Ruo'), 
        ('Sal e Pimenta', 'Sal e Pimenta'),  
        ('Tigrado', 'Tigrado'),
        ('Unicolor','Unicolor')
    ]

    GENDER_OF_PETS = [
        ('Fmea', 'Fmea'), 
        ('Macho', 'Macho'), 
    ]

    ACTIVITY_LEVEL_PETS = [
        ('Hiperativo', 'Hiperativo'), 
        ('Ativo', 'Ativo'), 
        ('Moderado', 'Moderado'),
        ('Baixo', 'Baixo'),  
    ]

    SPECIAL_NEED = [
        ('3 patas funcionais', '3 patas funcionais'), 
        ('2 patas funcionais', '2 patas funcionais'),
        ('1 pata funcional', '1 pata funcional'), 
        ('0 patas funcionais', '0 patas funcionais'), 
        ('Apenas alguns dentes', 'Apenas alguns dentes'),
        ('Cegueira parcial', 'Cegueira parcial'), 
        ('Cegueira total', 'Cegueira total'),
        ('Necessidade de remdios para sempre', 'Necessidade de remdios para sempre'),
        ('Necessidade de terapias para sempre', 'Necessidade de terapias'),
        ('Necessidade de terapias e remdios para sempre', 'Necessidade de terapias e remdios para sempre'),
        ('Nenhum dente', 'Nenhum dente'), 
        ('Doena Neural','Doena Neural'),
        ('Rabo amputado', 'Rabo amputado'), 
        ('Surdez parcial', 'Surdez parcial'), 
        ('Surdez total', 'Surdez total'),          
    ]

    CONFORTABLE = [ 
        ('No', 'No'), 
        ('Sim', 'Sim'),
        ('No sei', 'No sei'),
    ]

    STATUS_OF_PETS = [
        ('A caminho do novo lar', 'A caminho do novo lar'), 
        ('Adoo pendente', 'Adoo pendente'), 
        ('Adotado', 'Adotado'), 
        ('Doente', 'Doente'),
        ('Esperando visita', 'Esperando visita'), 
        ('Falecido', 'Falecido'),
        ('Retornando para abrigo','Retornando para abrigo'),
        ('Lar provisrio','Lar provisrio'),
        ('Lar provisrio pelo FDS','Lar provisrio pelo FDS'),

    ]

    STATUS_OF_TEETH = [
        ('Perfeitos', 'Perfeitos'), 
        ('Um pouco de trtaro', 'Um pouco de trtaro'), 
        ('Trtaro mediano', 'Trtaro mediano'),
        ('Perdeu alguns dentes', 'Perdeu alguns dentes'),
        ('Dentes permitem apenas comida mole', 'Dentes permitem apenas comida mole'), 
        ('Perdeu quase todos ou todos os dentes', 'Perdeu quase todos ou todos os dentes'), 
    ]

    COAT_OF_PETS = [
        ('Arrepiado ', 'Arrepiado'), 
        ('Liso', 'Liso'),
        ('Ondulado', 'Ondulado'), 
    ]

    COAT_SIZE_OF_PETS = [
        ('Curto', 'Curto'), 
        ('Mdio', 'Mdio'),
        ('Longo', 'Longo'), 
    ]

    SPECIES_OF_PETS = [
        ('Cachorro', 'Cachorro'), 
        ('Gato', 'Gato'), 
        ('Outros', 'Outros'),  
    ]

    SIZE_OF_PETS = [
        ('Mini', 'Mini'), 
        ('Pequeno', 'Pequeno'), 
        ('Mdio', 'Mdio'), 
        ('Grande', 'Grande'),
        ('Gigante', 'Gigante'), 
    ]

    AGE_CATEGORY_OF_PETS = [
        ('Filhote', 'Filhote'), 
        ('Adolescente', 'Adolescente'), 
        ('Adulto', 'Adulto'), 
        ('Maduro', 'Maduro'),
        ('Idoso', 'Idoso'), 
    ]

    AGE_OF_PETS = [
        ('1 ms', '1 ms'), 
        ('2 meses', '2 meses'), 
        ('3 meses', '3 meses'), 
        ('4 meses', '4 meses'),
        ('5 meses', '5 meses'), 
        ('6 meses', '6 meses'), 
        ('7 meses', '7 meses'), 
        ('8 meses', '8 meses'),
        ('9 meses', '9 meses'), 
        ('10 meses', '10 meses'), 
        ('11 meses', '11 meses'),
        ('1 ano', '1 ano'), 
        ('2 anos', '2 anos'),
        ('3 anos', '3 anos'), 
        ('4 anos', '4 anos'),
        ('5 anos', '5 anos'), 
        ('6 anos', '6 anos'),
        ('7 anos', '7 anos'),
        ('8 anos', '8 anos'), 
        ('9 anos', '9 anos'),
        ('10 anos', '10 anos'), 
        ('11 anos', '11 anos'),
        ('12 anos', '12 anos'),
        ('13 anos', '13 anos'), 
        ('14 anos', '14 anos'),
        ('15 anos', '15 anos'), 
        ('16 anos', '16 anos'),
        ('17 anos', '17 anos'),
        ('18 anos', '18 anos'), 
        ('19 anos', '19 anos'),
        ('20 anos', '20 anos'), 
        ('21 anos', '21 anos'),
        ('22 anos', '22 anos'), 
        ('23 anos', '23 anos'),
        ('24 anos', '24 anos'), 
        ('25 anos', '25 anos'),
        ('26 anos', '26 anos'), 
        ('27 anos', '27 anos'),
        ('28 anos', '28 anos'), 
        ('29 anos', '29 anos'),
        ('30 anos', '30 anos'), 
        ('No sei', 'No sei'),
    ]


    DAY_OF_PETS = [ 
        ('No sei', 'No sei'),
        ('1', '1'), 
        ('2', '2'),
        ('3', '3'), 
        ('4', '4'),
        ('5', '5'), 
        ('6', '6'),
        ('7', '7'),
        ('8', '8'), 
        ('9', '9'),
        ('10', '10'), 
        ('11', '11'),
        ('12', '12'),
        ('13', '13'), 
        ('14', '14'),
        ('15', '15'), 
        ('16', '16'),
        ('17', '17'),
        ('18', '18'), 
        ('19', '19'),
        ('20', '20'), 
        ('21', '21'),
        ('22', '22'), 
        ('23', '23'),
        ('24', '24'), 
        ('25', '25'),
        ('26', '26'), 
        ('27', '27'),
        ('28', '28'), 
        ('29', '29'),
        ('30', '30'),
        ('31', '31'), 
    ]

    MONTH_OF_PETS = [
        ('No sei', 'No sei'), 
        ('Janeiro', 'Janeiro'), 
        ('Fevereiro', 'Fevereiro'), 
        ('Maro', 'Maro'),
        ('Abril', 'Abril'), 
        ('Maio', 'Maio'), 
        ('Junho', 'Junho'), 
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'), 
        ('Setembro', 'Setembro'), 
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'), 
        ('Dezembro', 'Dezembro'),
    ]

    AGE_OF_PETS = [
        ('1 ms', '1 ms'), 
        ('2 meses', '2 meses'), 
        ('3 meses', '3 meses'), 
        ('4 meses', '4 meses'),
        ('5 meses', '5 meses'), 
        ('6 meses', '6 meses'), 
        ('7 meses', '7 meses'), 
        ('8 meses', '8 meses'),
        ('9 meses', '9 meses'), 
        ('10 meses', '10 meses'), 
        ('11 meses', '11 meses'),
        ('1 ano', '1 ano'), 
        ('2 anos', '2 anos'),
        ('3 anos', '3 anos'), 
        ('4 anos', '4 anos'),
        ('5 anos', '5 anos'), 
        ('6 anos', '6 anos'),
        ('7 anos', '7 anos'),
        ('8 anos', '8 anos'), 
        ('9 anos', '9 anos'),
        ('10 anos', '10 anos'), 
        ('11 anos', '11 anos'),
        ('12 anos', '12 anos'),
        ('13 anos', '13 anos'), 
        ('14 anos', '14 anos'),
        ('15 anos', '15 anos'), 
        ('16 anos', '16 anos'),
        ('17 anos', '17 anos'),
        ('18 anos', '18 anos'), 
        ('19 anos', '19 anos'),
        ('20 anos', '20 anos'), 
        ('21 anos', '21 anos'),
        ('22 anos', '22 anos'), 
        ('23 anos', '23 anos'),
        ('24 anos', '24 anos'), 
        ('25 anos', '25 anos'),
        ('26 anos', '26 anos'), 
        ('27 anos', '27 anos'),
        ('28 anos', '28 anos'), 
        ('29 anos', '29 anos'),
        ('30 anos', '30 anos'), 
        ('Menos de 1 ano', 'Menos de 1 ano'),
    ]

    RETURN_OF_PETS = [ 
        (0, 0),
        (1, 1), 
        (2, 2),
        (3, 3), 
        (4, 4),
        (5, 5), 
        (6, 6),
        (7, 7),
        (8, 8), 
        (9, 9),
        (10, 10), 
    ]

    TYPES_STREET = [
        ('Alameda', 'Alameda'),
        ('Avenida', 'Avenida'),
        ('Chcara', 'Chcara'),
        ('Colnia', 'Colnia'),
        ('Condomnio', 'Condomnio'),
        ('Conjunto', 'Conjunto'),
        ('Estao', 'Estao'),
        ('Estrada', 'Estrada'),
        ('Favela', 'Favela'),
        ('Fazenda', 'Fazenda'),
        ('Jardim', 'Jardim'),
        ('Ladeira', 'Ladeira'),
        ('Lago', 'Lago'),
        ('Largo', 'Largo'),
        ('Loteamento', 'Loteamento'),
        ('Passarela', 'Passarela'),
        ('Parque', 'Parque'),
        ('Praa', 'Praa'),
        ('Praia','Praia'),
        ('Rodovia', 'Rodovia'),
        ('Rua', 'Rua'),
        ('Setor', 'Setor'),
        ('Travessa', 'Travessa'),
        ('Viaduto', 'Viaduto'),
        ('Vila', 'Vila'),
    ]

    SPECIAL_NEED = [
        ('3 patas funcionais', '3 patas funcionais'), 
        ('2 patas funcionais', '2 patas funcionais'),
        ('1 pata funcional', '1 pata funcional'), 
        ('0 patas funcionais', '0 patas funcionais'), 
        ('No pode mastigar', 'No pode mastigar'),
        ('Cegueira parcial', 'Cegueira parcial'), 
        ('Cegueira total', 'Cegueira total'),
        ('Necessidade de remdios para sempre', 'Necessidade de remdios para sempre'),
        ('Necessidade de terapias para sempre', 'Necessidade de terapias'),
        ('Necessidade de terapias e remdios para sempre', 'Necessidade de terapias e remdios para sempre'),
        ('Doena mental','Doena mental'),
        ('Epilepsia','Epilesia'),
        ('Rabo amputado', 'Rabo amputado'), 
        ('Surdez parcial', 'Surdez parcial'), 
        ('Surdez total', 'Surdez total'),    
        ('No sente cheiro','No sente cheiro')      
    ]

    def get_years():
        now = int(timezone.now().year) + 1
        past = timezone.now().year - 30
        
        a = []
        for i in reversed(range(past,now)):
            a.append((i,i))
        a = tuple(a)   

        return a

    name = models.CharField("Nome", null=True, blank=True, max_length=30)
    pet_description = models.CharField(null=True, blank=True, max_length = 700)
    age = models.CharField(null=True, blank=True, max_length=40, choices=AGE_OF_PETS, default='')
    age_category = models.CharField(null=True, blank=True, max_length=30, choices=AGE_CATEGORY_OF_PETS, default='')
    species = models.CharField(null=True, blank=True, max_length=25,choices=SPECIES_OF_PETS, default='')
    primary_breed = models.ForeignKey(Pet_breed, on_delete=models.CASCADE, null=True, blank=True, related_name='primary_breed')
    secondary_breed = models.ForeignKey(Pet_breed, on_delete=models.CASCADE, null=True, blank=True, related_name='secondary_breed')
    color = models.CharField(null=True, blank=True, max_length=30,choices=COLOR_OF_PETS, default='')
    coat = models.CharField(null=True, blank=True, max_length=20,choices=COAT_OF_PETS, default='')
    gender = models.CharField(null=True, blank=True, max_length=10, choices=GENDER_OF_PETS, default='')
    birth_day = models.CharField(default=0, null=True, blank=True, max_length=30,choices=DAY_OF_PETS,)
    birth_month = models.CharField(default=0, null=True, blank=True, max_length=30,choices=MONTH_OF_PETS,)
    birth_year = models.IntegerField(default=0, null=True, blank=True, choices=get_years())
    is_microchiped = models.BooleanField(default=0)
    activity_level = models.CharField(null=True, blank=True, max_length=40, choices=ACTIVITY_LEVEL_PETS, default='')
    is_basic_trainned = models.BooleanField(default=0)
    confortable_with_kids = models.CharField(null=True, blank=True, max_length=100, choices=CONFORTABLE, default='')
    confortable_with_elder = models.CharField(null=True, blank=True, max_length=100, choices=CONFORTABLE, default='')
    confortable_with_cats = models.CharField(null=True, blank=True, max_length=100, choices=CONFORTABLE, default='')
    confortable_with_dogs = models.CharField(null=True, blank=True, max_length=100, choices=CONFORTABLE, default='')
    confortable_with_men = models.CharField(null=True, blank=True, max_length=100, choices=CONFORTABLE, default='')
    confortable_with_women = models.CharField(null=True, blank=True, max_length=100, choices=CONFORTABLE, default='')
    arrival_date = models.CharField(null=True, blank=True, max_length=30, default='')
    where_was_found_name = models.CharField(null=True, blank=True, max_length=100, default='')
    is_neutered = models.BooleanField(default=0)
    was_rabbies_vaccinated_this_year = models.BooleanField(default=0)
    was_v_vaccinated_this_year = models.BooleanField(default=0)
    was_others_vaccinated_this_year = models.BooleanField(default=0)
    profile_picture = models.ImageField(null=True, blank=True)
    picture_1 = models.ImageField(null=True, blank=True)
    picture_2 = models.ImageField(null=True, blank=True)
    picture_3 = models.ImageField(null=True, blank=True)
    video = models.CharField(null=True, blank=True, max_length=150)
    qty_views = models.IntegerField(default=0)
    qty_favorites = models.IntegerField(default=0)
    qty_msg = models.IntegerField(default=0)
    qty_shares = models.IntegerField(default=0)
    ongs_id = models.ForeignKey(Ongs, on_delete=models.CASCADE, default=1)
    status = models.CharField(null=True, blank=True, max_length=50, choices=STATUS_OF_PETS, default='')
    coat_size = models.CharField(null=True, blank=True, max_length=50, choices=COAT_SIZE_OF_PETS, default='')
    walk_pull = models.BooleanField(default=0)
    walk_pull_hard = models.BooleanField(default=0)
    walk_dogs = models.BooleanField(default=0)
    walk_people = models.BooleanField(default=0)
    walk_fear = models.BooleanField(default=0)
    color_pattern = models.CharField(null=True, blank=True, max_length=30,choices=COLOR_PATTERN_OF_PETS, default='')
    size = models.CharField(null=True, blank=True, max_length=50,choices=SIZE_OF_PETS, default='')
    qty_preview_adoptions = models.IntegerField(default=0, choices=RETURN_OF_PETS)
    qty_adoptions_app = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    teeth_status = models.CharField(null=True, blank=True, max_length=50, choices=STATUS_OF_TEETH, default='')
    combo_adoption_id = models.IntegerField(default=0, null=True, blank=True,)
    is_available_adoption = models.BooleanField(default=1)
    where_was_found = models.CharField(null=True, blank=True, max_length=50, choices=TYPES_STREET, default='')
    where_was_found_city = models.CharField(null=True, blank=True, max_length=100, default='')
    where_was_found_state = models.CharField(null=True, blank=True, max_length=100, default='')
    first_special_need = models.CharField(null=True, blank=True, max_length=100, choices=SPECIAL_NEED, default='')
    second_special_need = models.CharField(null=True, blank=True, max_length=100, choices=SPECIAL_NEED, default='')
    third_special_need = models.CharField(null=True, blank=True, max_length=100, choices=SPECIAL_NEED, default='')
    is_mixed_breed = models.BooleanField(default=1)
    is_walking_daily = models.BooleanField(default=0)
    is_acupuncture = models.BooleanField(default=0)
    is_physiotherapy = models.BooleanField(default=0)
    is_vermifuged = models.BooleanField(default=0)
    is_lice_free = models.BooleanField(default=0)
    is_dog_meet_necessary = models.BooleanField(default=0)
    walk_alone_dislike = models.BooleanField(default=0)
    walk_alone = models.BooleanField(default=0)
    walk_leash = models.BooleanField(default=0)
    id_at_ong = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

@receiver(models.signals.pre_save, sender=Pet)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_pic = Pet.objects.get(pk=instance.pk).profile_picture
        except Pet.DoesNotExist:
            return
        else:
            new_pic = instance.profile_picture
            if old_pic and old_pic.url != new_pic.url:
                old_pic.delete(save=False)

class Favorites(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)

class Pet_disease_areas(models.Model):
    name = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.name

class Pet_disease(models.Model):

    AREA_OF_PETS = [
        ('Cardiologia', 'Cardiologia'), 
        ('Dermatologia', 'Dermatologia'),
        ('Endocrinologia', 'Endocrinologia'),  
        ('Gastroenterologia e Hepatologia','Gastroenterologia e Hepatologia'),
        ('Hematologia e Imunologia', 'Hematologia e Imunologia'), 
        ('Infecciosas', 'Infecciosas'), 
        ('Intoxicaes e Envenemanentos', 'Intoxicaes e Envenemanentos'),      
        ('Musculoesquelticas', 'Musculoesquelticas'),
        ('Nefrologia e Urologia', 'Nefrologia e Urologia'), 
        ('Neonatologia', 'Neonatologia'), 
        ('Neurologia', 'Neurologia'), 
        ('Oftalmologia', 'Oftalmologia'), 
        ('Oncologia', 'Oncologia'), 
        ('Respiratrias', 'Respiratrias'),
        ('Teriogenologia','Teriogenologia'),
        ('Vacinao e Nutrologia', 'Vacinao e Nutrologia'), 
        ('Outras', 'Outras'), 
    ]

    name = models.CharField(null=True, blank=True, max_length=150)
    area = models.CharField(null=True, blank=True, max_length=100,choices=AREA_OF_PETS, default='')
    area_id = models.ForeignKey(Pet_disease_areas,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name

class Pet_health(models.Model):

    SPECIAL_NEED = [
        ('3 patas funcionais', '3 patas funcionais'), 
        ('2 patas funcionais', '2 patas funcionais'),
        ('1 pata funcional', '1 pata funcional'), 
        ('0 patas funcionais', '0 patas funcionais'), 
        ('No pode mastigar', 'No pode mastigar'),
        ('Cegueira parcial', 'Cegueira parcial'), 
        ('Cegueira total', 'Cegueira total'),
        ('Necessidade de remdios para sempre', 'Necessidade de remdios para sempre'),
        ('Necessidade de terapias para sempre', 'Necessidade de terapias'),
        ('Necessidade de terapias e remdios para sempre', 'Necessidade de terapias e remdios para sempre'),
        ('Doena mental','Doena mental'),
        ('Epilepsia','Epilesia'),
        ('Rabo amputado', 'Rabo amputado'), 
        ('Surdez parcial', 'Surdez parcial'), 
        ('Surdez total', 'Surdez total'),    
        ('No sente cheiro','No sente cheiro')      
    ]

    STATUS = [
        ('Curado', 'Curado'), 
        ('Em tratamento', 'Em tratamento'),
        ('Sem verba', 'Sem verba'), 
    ]

    SPECIAL_TREATMENT = [
        ('Fisioterapia', 'Fisioterapia'), 
        ('Acunpuntura', 'Acunpuntura'),
        ('Caminhada diria', 'Caminhada diria'), 
    ]

    TYPES = [
        ('Fatal', 'Fatal'), 
        ('Para o resto da vida', 'Para o resto da vida'), 
        ('Temporria', 'Temporria'),
    ]

    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    diagnose_date = models.DateField(null=True, blank=True)
    #disease = models.ForeignKey(Pet_disease,on_delete=models.CASCADE)
    disease_status = models.CharField(null=True, blank=True, max_length=100, choices=STATUS, default='')
    disease_type = models.CharField(null=True, blank=True, max_length=100, choices=TYPES, default='')
    internal_notes = models.CharField(null=True, blank=True, max_length=300) 
    which_special_need = models.CharField(null=True, blank=True, max_length=100, choices=SPECIAL_NEED, default='')
    which_special_treatment = models.CharField(null=True, blank=True, max_length=100, choices=SPECIAL_TREATMENT, default='')
    #disease_area = models.ForeignKey(Pet_disease_areas,on_delete=models.CASCADE, null=True, blank=True)
    disease_name = models.CharField(null=True, blank=True, max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.disease
