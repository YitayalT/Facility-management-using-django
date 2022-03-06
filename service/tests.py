from django.test import TestCase

class TestUrl(TestCase):
    def test_url_exists(self):
        response = self.client.get('/service-item')
        self.assertEqual(response.status_code, 200)

    def test_string_method(self):
        student = Student.objects.get(id=1)
        expected_string = f"Name: {student.first_name} {student.last_name}"
        self.assertEqual(str(student), expected_string)
