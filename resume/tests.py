from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import Client
from resume.models import Contact
import json

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('sawhigh', 'sawhigh@example.com', 'password')

    def testcreate(self):
        self.client.login(username='sawhigh', password='password')
        data=json.dumps({'name':'sawhigh', 'link':'http://google.com'})
        response = self.client.post(reverse("contact_create"), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")
        
    def testbrowse(self):
        self.client.login(username='sawhigh', password='password')
        user = User.objects.get(username='sawhigh')
        contact = Contact.objects.create(user=user, name="1", link='http://google.com')
        contact.save()
        response = self.client.get(reverse("contact_browse", args=[user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        
    def testlist(self):
        self.client.login(username='sawhigh', password='password')
        user = User.objects.get(username='sawhigh')
        contact = Contact.objects.create(user=user, name="1", link='http://google.com')
        contact.save()
        response = self.client.get(reverse("contact_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")

    def testupdate(self):
        self.client.login(username='sawhigh', password='password')
        user = User.objects.get(username='sawhigh')
        contact = Contact.objects.create(user=user, name="1", link='http://google.com')
        contact.save()
        data=json.dumps({'name':'sawhigh', 'link':'http://google.com'})
        response = self.client.post(reverse("contact_update", args=[contact.id]), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")
        
    def testdelete(self):
        self.client.login(username='sawhigh', password='password')
        user = User.objects.get(username='sawhigh')
        contact = Contact.objects.create(user=user, name="1", link='http://google.com')
        contact.save()
        response = self.client.post(reverse("contact_delete", args=[contact.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")