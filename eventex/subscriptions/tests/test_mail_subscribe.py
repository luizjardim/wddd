from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Luiz Felipe', cpf='37710722806',
                    email='luizmj@gmail.com', phone='12-98241-5558')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):

        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'luizmj@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):

        expect = ['luizmj@gmail.com', 'luizmj@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents =[
                    'Luiz Felipe',
                    '37710722806',
                    'luizmj@gmail.com',
                    '12-98241-5558',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

