import io

from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from teacher.models import TeacherInformation

User = get_user_model()


class TeacherInfoApiTestCase(APITestCase):
    def setUp(self):
        image = io.BytesIO()
        Image.new('RGB', (150, 150)).save(image, 'JPEG')
        image.seek(0)
        self.file = SimpleUploadedFile('teacherimage.jpg', image.getvalue())
        self.user = User.objects.create(email='2@gmail.com')

    def test_valid_post(self):
        url = reverse('teacher')
        data = {
            'telephone_number': '0334532',
            'image': self.file,
            'user': self.user.id,
            'name_of_lesson': 'Java'
        }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(1, TeacherInformation.objects.all().count())
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

