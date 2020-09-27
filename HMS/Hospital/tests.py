from django.templatetags.i18n import language
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse



class login(TestCase):

def login(self):
    self.user = get_user_model().objects.create_user(
        username = 'Group6',
        email = 'group6@gmail.com',
        password = '123456',
    )


def blood_bank(self):
    request = self.client.get(reverse("login"))
    self.assertContains(request, 'admin')
    self.assertEqual(request,'Access')
    self.assertContains(request, 'blood_bank')
    self.assertAlmostEqual(language['percent']['python'])
    self.assertAlmostEqual(request["error"])
    self.assertAlmostEqual(request["login"])


def pharmacy(self):
    request = self.client.get(reverse("pharmacy"))
    self.assertContains(request, 'admin')
    self.assertEqual(request,'Access')
    self.assertContains(request, 'pharmacy')
    self.assertAlmostEqual(language['percent']['python'])
    self.assertAlmostEqual(request["error"])
    self.assertAlmostEqual(request["login"])










# Create your tests here.

class login(TestCase):

    def admin(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='admin@gmail.com',
            password='654321',
        )

    def ambulance(self):
        request = self.client.get(reverse("ambulance"))
        self.assertContains(request, 'admin')
        self.assertEqual(request, 'Access')
        self.assertContains(request, 'ambulance')
        self.assertAlmostEqual(language['percent']['python'])
        self.assertAlmostEqual(request["error"])
        self.assertAlmostEqual(request["login"])

    def emergency(self):
        request = self.client.get(reverse("emergency"))
        self.assertContains(request, 'admin')
        self.assertEqual(request, 'Access')
        self.assertContains(request, 'emergency')
        self.assertAlmostEqual(language['percent']['python'])
        self.assertAlmostEqual(request["error"])
        self.assertAlmostEqual(request["login"])


