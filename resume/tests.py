from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.test.client import Client
from resume.models import Contact, Profile
import json
from StringIO import StringIO
from PIL import Image
from django.core.files.base import File

class APITestCase(TestCase):
    
    @staticmethod
    def get_image_file(name=u'test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = StringIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)
    
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
        i = Profile.objects.create(user=user, avatar=self.get_image_file())
        i.save()
        
        response = self.client.get(reverse("profile_list"))
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
        
    def testupload(self):   
        data = {'avatar': self.get_image_file()}
        
        self.client.login(username='sawhigh', password='password')
        user = User.objects.get(username='sawhigh')
        i = Profile.objects.create(user=user)
        i.save()
        
        response = self.client.post(reverse_lazy("avatar_update", args=[i.id]), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")