from django.test import SimpleTestCase
from main.forms import *


class TestPositionForms(SimpleTestCase):

    def test_expense_form_valid_data(self):
        form = PositionForm(data={
            'name': 'директор',
            'salary': 1000,
        })

        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form = PositionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

class TestContactForms(SimpleTestCase):

    def test_expense_form_valid_data(self):
        form = ContactForm(data={
            'subject': 'subject',
            'content': 'content'
        })

        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

