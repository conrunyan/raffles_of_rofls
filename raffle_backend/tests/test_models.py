from django.test import TestCase
from raffle_backend.models import (
    User,
    Winner,
    Session,
    Host
)

class TestUser(TestCase):
    def test_base_constructor(self):
        pass