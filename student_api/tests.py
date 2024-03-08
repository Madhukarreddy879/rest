from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Student
from .serializers import StudentSerializer




class StudentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student_data = {
            'name': 'John Doe',
            'roll_number': 12345
            # Add other fields as needed
        }
        self.student = Student.objects.create(**self.student_data)

    def test_create_student(self):
        url = reverse('student-list-create')
        response = self.client.post(url, self.student_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)  # Assuming there's already one student created in setUp

    def test_get_all_students(self):
        url = reverse('student-list-create')
        response = self.client.get(url)
        students = Student.objects.all()
        serializer_data = StudentSerializer(students, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_get_student_detail(self):
        url = reverse('student-detail', kwargs={'pk': self.student.pk})
        response = self.client.get(url)
        student = Student.objects.get(pk=self.student.pk)
        serializer_data = StudentSerializer(student).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_update_student(self):
        url = reverse('student-detail', kwargs={'pk': self.student.pk})
        updated_data = {
            'name': 'Updated Name',
            'roll_number': 54321
            # Add other fields as needed
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, updated_data['name'])
        self.assertEqual(self.student.roll_number, updated_data['roll_number'])

    def test_delete_student(self):
        url = reverse('student-detail', kwargs={'pk': self.student.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)
