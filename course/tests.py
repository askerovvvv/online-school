import io

from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from course.models import *
from course.serializers import *

User = get_user_model()


class CourseTestApiTestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(slug='Backend')
        self.user = User.objects.create(email='admintestuser@gmail.com', is_staff=True)
        self.user2 = User.objects.create(email='testuser@gmail.com',)

        self.course1 = Course.objects.create(title='Python', category=self.category)
        self.course2 = Course.objects.create(title='Java', category=self.category)

        self.serializer_data = CourseSerializers(Course.objects.all(), many=True).data

        image = io.BytesIO()
        Image.new('RGB', (150, 150)).save(image, 'JPEG')
        image.seek(0)
        self.file = SimpleUploadedFile('image.jpg', image.getvalue())

    def test_valid_get(self):
        url = reverse('course-list')
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.serializer_data, response.data)
        self.assertEqual(len(self.serializer_data), len(response.data))

    def test_invalid_get(self):
        url = reverse('course-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)


