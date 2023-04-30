from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from places.models import Place

User = get_user_model()


class TestsView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='MIHA')
        cls.places = Place.objects.create(
            name='Тестовое название',
            latitude=56.825053189709,
            longitude=60.5994881210587,
            comment='Тестовый коммент',
        )
        cls.templates_pages_names = {
            reverse('places:profile'): 'user/profile.html',
            reverse('places:map'): 'user/map.html',
        }

    def setUp(self):
        # Создаем авторизованный клиент
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
    
    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        for reverse_name, template in self.templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
    
    def test_profile_show_correct_context(self):
        response = self.authorized_client.get(reverse('places:profile'))
        first_object = response.context['page_obj'][0]
        name = first_object.name
        author = first_object.author
        comment = first_object.comment
        latitude = first_object.latitude
        longitude = first_object.longitude
        self.assertEqual(name, 'Тестовое название')
        self.assertEqual(author, self.user)
        self.assertEqual(comment, 'Тестовый коммент')
        self.assertEqual(latitude, 56.825053189709)
        self.assertEqual(longitude, 60.5994881210587)
