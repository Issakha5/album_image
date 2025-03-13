from django.test import TestCase
from django.urls import reverse
from .models import Image
from .forms import ImageForm
from django.core.files.uploadedfile import SimpleUploadedFile


class ImageViewsTest(TestCase):

    def setUp(self):
        self.image = Image.objects.create(
            title="Test Image",
            image=SimpleUploadedFile("test.jpg", b"file_content",
                                     content_type="image/jpeg")
        )

    def test_image_list_view(self):
        response = self.client.get(reverse('image_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'imageapp/read.html')

    def test_image_detail_view(self):
        response = self.client.get(
            reverse('image_detail', args=[self.image.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'imageapp/detail.html')

    def test_image_create_view_get(self):
        response = self.client.get(reverse('image_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'imageapp/create.html')

    def test_image_create_view_post(self):
        file = SimpleUploadedFile("test1.jpg", b"new_content",
                                  content_type="image/jpeg")
        response = self.client.post(reverse('image_create'), {
            'title': 'New Image',
            'image': file
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Image.objects.count(), 2)  # L'image test + 1 nouvelle

    def test_image_update_view_get(self):
        response = self.client.get(
            reverse('image_update', args=[self.image.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'imageapp/create.html')

    def test_image_update_view_post(self):
        file = SimpleUploadedFile("test2.jpg", b"updated_content",
                                  content_type="image/jpeg")
        response = self.client.post(
            reverse('image_update', args=[self.image.pk]), {
                'title': 'Updated Image',
                'image': file
            }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.image.refresh_from_db()
        self.assertEqual(self.image.title, "Updated Image")

    def test_image_delete_view_get(self):
        response = self.client.get(
            reverse('image_delete', args=[self.image.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'imageapp/delete.html')

    def test_image_delete_view_post(self):
        response = self.client.post(
            reverse('image_delete', args=[self.image.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Image.objects.count(),0)
