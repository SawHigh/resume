from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.test.client import Client
from resume.models import Contact, Profile, UserContact, Project
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
        i = Contact.objects.create(name="abc", icon=self.get_image_file())
        i.save()        
        j = UserContact.objects.create(user=self.user, contact=i, link='http://google.com')
        j.save()        
        k = Project.objects.create(user=self.user,
                                   title = "aa",
                                   condition = "bb",
                                   description ="cc",
                                   published_date = "1111-11-11",
                                   link = "http://google.com",
                                   source_code = "http://google.com",)
        k.save()
        l = Profile.objects.create(user=self.user)
        l.save()
        self.contact = i
        self.user_contact = j
        self.project = k       
        self.profile = l
        
    def test_user_list(self):

        response = self.client.get(reverse("user_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "profile_name")
        
    def test_project_update(self):
        self.client.login(username='sawhigh', password='password')
        i = self.project
        data=json.dumps({ "title" : "bb",
                        "condition" : "cc",
                        "description" :"dd",
                        "published_date" : "1112-12-12",
                        "link" : "http://google2.com",
                        "source_code" : "http://google2.com"})
        response = self.client.post(reverse("project_update", args=[i.id]), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")
        
    def test_contact_create(self):
        data = {'name':'dealhigh', 'icon': self.get_image_file()}
        self.client.login(username='sawhigh', password='password')
        response = self.client.post(reverse_lazy("contact_create"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")
        
    def test_contact_list(self):
        self.client.login(username='sawhigh', password='password')
        response = self.client.get(reverse("contact_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")

    def testcreate(self):
        self.client.login(username='sawhigh', password='password')
        data=json.dumps({'contact_id':self.contact.id, 'link':'http://google.com'})
        response = self.client.post(reverse("usercontact_create"), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")
        
    def testbrowse(self):
        self.client.login(username='sawhigh', password='password')
        user = self.user
        response = self.client.get(reverse("usercontact_browse", args=[user.id]))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, "link")
        
    def testlist(self):
        self.client.login(username='sawhigh', password='password')       
        response = self.client.get(reverse("profile_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")

    def testupdate(self):
        self.client.login(username='sawhigh', password='password')
        contact = self.user_contact
        data=json.dumps({ 'link':'http://google.com'})
        response = self.client.post(reverse("usercontact_update", args=[contact.id]), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")
        
    def testdelete(self):
        self.client.login(username='sawhigh', password='password')
        contact = self.user_contact

        response = self.client.post(reverse("usercontact_delete", args=[contact.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")
        
    def testexcept(self):    
        self.client.login(username='sawhigh', password='password')
        contact = self.user_contact
        data=json.dumps({ 'link':'http://google.com',"aaa":"bbb"})
        response = self.client.post(reverse("usercontact_update", args=[contact.id]), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        print response
        self.assertContains(response, "fail")
                
    def testupload(self):   
        data = {'avatar': self.get_image_file()}     
        self.client.login(username='sawhigh', password='password')
        i = self.profile
        response = self.client.post(reverse_lazy("avatar_update", args=[i.id]), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")