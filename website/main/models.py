from django.db import models



class Military(models.Model):

    id = models.AutoField(primary_key=True)
    number = models.CharField('Номер', max_length=45)
    dislocation= models.CharField('Дислокация', max_length=45)
    type_troops=models.CharField('Вид войск', max_length=45)
    companies=models.CharField('Роты', max_length=45)


    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return f'/military/{self.id}'

    class Meta:
        verbose_name = 'Военная часть'
        verbose_name_plural= 'Военные части'

class Type_troop(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Номер', max_length=45)
    military = models.ForeignKey(Military, on_delete=models.CASCADE, null=True)
    
    def get_absolute_url(self):
        return f'/type_troops/{self.id}'

    class Meta:
        verbose_name = 'Виды войск'
        verbose_name_plural= 'Виды войск'


class Companies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=45)
    number_employees = models.CharField('Номер', max_length=45)
    type_troops = models.ForeignKey(Type_troop, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/companies/{self.id}'

    class Meta:
        verbose_name = 'Рота'
        verbose_name_plural= 'Роты'


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    fist_name = models.CharField('Имя', max_length=45)
    companies = models.CharField('Рота', max_length=45)
    post = models.CharField('Название', max_length=45)
    year_birth = models.DateField(auto_now=False)
    year_enlistment = models.DateField(auto_now=False)
    length_service = models.CharField('Название', max_length=45)
    honors = models.CharField('Название', max_length=45)
    military_activies= models.CharField('Название', max_length=45)
    compain=models.ForeignKey(Companies,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.fist_name

    def get_absolute_url(self):
        return f'/employees/{self.id}'

    class Meta:
        verbose_name = 'Личный состав'
        verbose_name_plural = 'Личный состав'


class Dislocatio(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField('Название', max_length=45)
    city = models.CharField('Название', max_length=45)
    address = models.CharField('Название', max_length=45)
    squar = models.CharField('Название', max_length=45)
    military=models.OneToOneField(Military,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.country

    def get_absolute_url(self):
        return f'/dislocation/{self.id}'

    class Meta:
        verbose_name = 'Дислокация'
        verbose_name_plural = 'Дислокация'

