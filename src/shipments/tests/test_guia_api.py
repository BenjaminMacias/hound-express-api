from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from shipments.models import Guia

class GuiaAPITest(APITestCase):
    def test_create_guia_with_recipient(self):
        url = reverse('guia-list')  # URL del ViewSet (por basename)
        data = {
            "tracking_number": "ABC123456",
            "origin": "Guadalajara",
            "destination": "CDMX",
            "recipient": "Benjamín Macías",
            "created_at": "2025-07-10T10:00:00Z",
            "status": "Pendiente"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Guia.objects.count(), 1)

        guia = Guia.objects.first()
        self.assertEqual(guia.trackingNumber, "ABC123456")
        self.assertEqual(guia.recipient, "Benjamín Macías")
        self.assertEqual(guia.origin, "Guadalajara")
        self.assertEqual(guia.destination, "CDMX")
        self.assertEqual(guia.currentStatus, "Pendiente")
