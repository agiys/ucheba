from django.test import TestCase, Client
from django.urls import reverse
from main.models import *


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.military_url = reverse('military')
        self.type_troops_url = reverse('type_troops')
        self.companies_url = reverse('companies')
        self.employees_url = reverse('employees')
        self.dislocation_url = reverse('dislocation')
        self.create_military_url = reverse('create')
        self.create_type_troops_url = reverse('create2')
        self.create_companies_url = reverse('create3')
        self.create_employees_url = reverse('create4')
        self.create_dislocation_url = reverse('create5')
        
    
    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
    
    def test_military_GET(self):
        response = self.client.get(self.military_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/template1.html')
        
    def test_type_troops_GET(self):
        response = self.client.get(self.type_troops_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/template2.html')
    
    def test_companies_GET(self):
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/template3.html')
        
    def test_employees_GET(self):
        response = self.client.get(self.employees_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/template4.html')
        
    def test_dislocation_GET(self):
        response = self.client.get(self.dislocation_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/template5.html')
        
    def test_create_military_POST(self):
        response = self.client.post(self.create_military_url, data={
            'number':'1',
            'dislocation':'asd',
            'type_troops':'asd',
            'companies':'sdas',})
        self.assertEqual(response.status_code, 302)
    
    def test_create_type_troops_POST(self):
        response = self.client.post(self.create_type_troops_url, data={
            'title':'1',})
        self.assertEqual(response.status_code, 302)
    
    def test_create_companies_POST(self):
        response = self.client.post(self.create_companies_url, data={
            'title':'1',
            'number_employees': '3',})
        self.assertEqual(response.status_code, 302)
    
    def test_create_employees_POST(self):
        response = self.client.post(self.create_employees_url, data={
            'fist_name':'asd',
            'companies':'asd',
            'post':'asd',
            'year_birth':'13.02.1888',
            'year_enlistment':'13.02.1888',
            'length_service': '123',
            'honors':'123',
            'military_activies':'13.02.1888',})
        self.assertEqual(response.status_code, 302)
        
    def test_create_dislocation_POST(self):
        response = self.client.post(self.create_dislocation_url, data={
            'country':'asd',
            'city':'asd',
            'address':'asd',
            'squar':'asd',})
        self.assertEqual(response.status_code, 302)
        
    def test_military_detail_GET(self):
        military = Military.objects.create(number='1', dislocation='123',type_troops='123',companies='123')

        response = self.client.get(
            reverse('details_view', kwargs={'pk': military.id}), 
            {'number': '1', 'dislocation': '123', 'type_troops': '123', 'companies':'123'})

        self.assertEqual(response.status_code, 200)
        
    def test_type_troops_detail_GET(self):
        type_troop = Type_troop.objects.create(title='123')

        response = self.client.get(
            reverse('details_view2', kwargs={'pk': type_troop.id}), 
            {'title': '123' })

        self.assertEqual(response.status_code, 200)
    
    def test_companies_detail_GET(self):
        companies = Companies.objects.create(title='1', number_employees='123')

        response = self.client.get(
            reverse('details_view3', kwargs={'pk': companies.id}), 
            {'title': '1', 'number_employees': '123'})

        self.assertEqual(response.status_code, 200)
    
    def test_mane_detail_GET(self):
        mane = Employees.objects.create(fist_name='1', companies='123', post='123', year_birth='1999-03-03', year_enlistment='1999-03-03', length_service='123', honors='123', military_activies='1999-03-03')

        response = self.client.get(
            reverse('details_view4', kwargs={'pk': mane.id}), 
            {'fist_name':'1',
            'companies':'123',
            'post':'123',
            'year_birth':'1999.03.03',
            'year_enlistment':'1999.03.03',
            'length_service': '123',
            'honors':'123',
            'military_activies':'1999.03.03',})

        self.assertEqual(response.status_code, 200)
    
    def test_dislocation_detail_GET(self):
        dislocation = Dislocatio.objects.create(country='asd', city='asd',address='asd',squar='asd')

        response = self.client.get(
            reverse('details_view5', kwargs={'pk': dislocation.id}), 
            {'country':'asd',
            'city':'asd',
            'address':'asd',
            'squar':'asd',})

        self.assertEqual(response.status_code, 200)
    
    def test_update_military(self):
        military = Military.objects.create(number='1', dislocation='123',type_troops='123',companies='123')

        response = self.client.post(
            reverse('update', kwargs={'pk': military.id}), 
            {'number': '123', 'dislocation': '123', 'type_troops': '123', 'companies':'123'})

        self.assertEqual(response.status_code, 302)

        military.refresh_from_db()
        self.assertEqual(military.number, '123')
        
    def test_update_type_troop(self):
        type_troop = Type_troop.objects.create(title='123')

        response = self.client.post(
            reverse('update2', kwargs={'pk': type_troop.id}), 
            {'title': '1234' })

        self.assertEqual(response.status_code, 302)

        type_troop.refresh_from_db()
        self.assertEqual(type_troop.title, '1234')
        
    def test_update_companies(self):
        companies = Companies.objects.create(title='1', number_employees='123')

        response = self.client.post(
            reverse('update3', kwargs={'pk': companies.id}), 
            {'title': '123', 'number_employees': '123'})

        self.assertEqual(response.status_code, 302)

        companies.refresh_from_db()
        self.assertEqual(companies.title, '123')
    
    def test_update_employees(self):
        mane = Employees.objects.create(fist_name='1', companies='123', post='123', year_birth='1999-03-03', year_enlistment='1999-03-03', length_service='123', honors='123', military_activies='1999-03-03')

        response = self.client.post(
            reverse('update4', kwargs={'pk': mane.id}), 
            {'fist_name':'asd',
            'companies':'123',
            'post':'123',
            'year_birth':'1999-03-03',
            'year_enlistment':'1999-03-03',
            'length_service': '123',
            'honors':'123',
            'military_activies':'1999-03-03',})

        self.assertEqual(response.status_code, 302)

        mane.refresh_from_db()
        self.assertEqual(mane.fist_name, 'asd')
        
    def test_update_dislocation(self):
        dislocation = Dislocatio.objects.create(country='asd', city='asd',address='asd',squar='asd')

        response = self.client.post(
            reverse('update5', kwargs={'pk': dislocation.id}), 
            {'country':'asd2',
            'city':'asd',
            'address':'asd',
            'squar':'asd',})

        self.assertEqual(response.status_code, 302)

        dislocation.refresh_from_db()
        self.assertEqual(dislocation.country, 'asd2')
        
        
    def test_delete_military(self):
        military = Military.objects.create(number='1', dislocation='123',type_troops='123',companies='123')

        response = self.client.post(
            reverse('delete', kwargs={'pk': military.id}), 
            {'number': '1', 'dislocation': '123', 'type_troops': '123', 'companies':'123'})

        self.assertRedirects(response, reverse('military'), status_code=302)
        
    def test_delete_type_troop(self):
        type_troop = Type_troop.objects.create(title='123')

        response = self.client.post(
            reverse('delete2', kwargs={'pk': type_troop.id}), 
            {'title': '123' })

        self.assertRedirects(response, reverse('type_troops'), status_code=302)
    
    def test_delete_companies(self):
        companies = Companies.objects.create(title='1', number_employees='123')

        response = self.client.post(
            reverse('delete3', kwargs={'pk': companies.id}), 
            {'title': '1', 'number_employees': '123'})

        self.assertRedirects(response, reverse('companies'), status_code=302)
        
    def test_delete_employees(self):
        mane = Employees.objects.create(fist_name='1', companies='123', post='123', year_birth='1999-03-03', year_enlistment='1999-03-03', length_service='123', honors='123', military_activies='1999-03-03')

        response = self.client.post(
            reverse('delete4', kwargs={'pk': mane.id}), 
            {'fist_name':'1',
            'companies':'123',
            'post':'123',
            'year_birth':'1999.03.03',
            'year_enlistment':'1999.03.03',
            'length_service': '123',
            'honors':'123',
            'military_activies':'1999.03.03',})

        self.assertRedirects(response, reverse('employees'), status_code=302)
    
    def test_delete_dislocation(self):
        dislocation = Dislocatio.objects.create(country='asd', city='asd',address='asd',squar='asd')

        response = self.client.post(
            reverse('delete5', kwargs={'pk': dislocation.id}), 
            {'country':'asd',
            'city':'asd',
            'address':'asd',
            'squar':'asd',})

        self.assertRedirects(response, reverse('dislocation'), status_code=302)