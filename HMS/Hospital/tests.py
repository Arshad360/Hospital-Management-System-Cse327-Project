from django.templatetags.i18n import language
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


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

