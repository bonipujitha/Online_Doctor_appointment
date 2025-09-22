from django.test import TestCase, Client
from .models import Doctor

class DoctorSignupTest(TestCase):

    def test_doctor_signup_info_in_db(self):
        """
        Test that doctor signup information is saved correctly in the database.
        """
        # Create a test client
        client = Client()

        # Prepare test data
        name = "Test Doctor"
        email = "test@example.com"
        password = "testpassword"
        phone = "1234567890"
        address = "Test Address"
        qualification = "MD"

        # Simulate doctor signup form submission
        response = client.post('/dsignupaction/', {
            "name": name,
            "email": email,
            "pwd": password,
            "phone": phone,
            "address": address,
            "qualification": qualification,
        })

        # Check if the doctor object was created and saved
        doctor = Doctor.objects.get(email=email)
        self.assertEqual(doctor.name, name)
        self.assertEqual(doctor.email, email)
        self.assertEqual(doctor.phone, phone)
        self.assertEqual(doctor.address, address)
        self.assertEqual(doctor.qualification, qualification)

        # Check if the doctor signup page redirects to the doctor view page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/dviewprofile/')

    def test_doctor_signup_missing_info(self):
        """
        Test that doctor signup fails if any required information is missing.
        """
        # Create a test client
        client = Client()

        # Submit form without name
        response = client.post('/dsignupaction/', {
            "email": "test@example.com",
            "pwd": "testpassword",
            "phone": "1234567890",
            "address": "Test Address",
            "qualification": "MD",
        })

        # Check if the doctor signup page is displayed again with error message
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please fill in all fields")

        # Similar tests can be done for other missing information

