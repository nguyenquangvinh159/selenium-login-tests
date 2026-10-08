"""Create and delete only disposable accounts owned by this test run."""
from dataclasses import dataclass, field
from uuid import uuid4

import requests


@dataclass(frozen=True)
class TestAccount:
    name: str
    email: str
    password: str = field(repr=False)


class AccountFactory:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.created = []

    def _call(self, method, endpoint, data, expected):
        response = self.session.request(
            method, self.base_url + endpoint, data=data, timeout=(10, 45)
        )
        response.raise_for_status()
        # This practice API can return HTTP 200 with a different JSON responseCode.
        payload = response.json()
        if int(payload.get('responseCode', 0)) != expected:
            raise RuntimeError(
                f'{endpoint}: expected responseCode {expected}, '
                f'got {payload.get("responseCode")}: {payload.get("message")}'
            )

    def create(self):
        token = uuid4().hex
        account = TestAccount(
            name='Selenium ' + token[:8],
            email='selenium_' + token + '@example.com',
            password='Aa9!Test_' + token,
        )
        data = dict(
            name=account.name, email=account.email, password=account.password,
            title='Mr', birth_date='1', birth_month='1', birth_year='2000',
            firstname='Selenium', lastname='Practice', company='Test data',
            address1='1 Demo Road', address2='', country='Canada',
            zipcode='A1A1A1', state='Demo', city='Demo', mobile_number='0000000000',
        )
        self._call('POST', '/api/createAccount', data, 201)
        self.created.append(account)
        return account

    def cleanup(self):
        errors = []
        try:
            for account in self.created:
                try:
                    self._call('DELETE', '/api/deleteAccount', {
                        'email': account.email, 'password': account.password,
                    }, 200)
                except (requests.RequestException, RuntimeError, ValueError) as exc:
                    errors.append(f'{account.email}: {type(exc).__name__}: {exc}')
        finally:
            self.session.close()
        if errors:
            raise RuntimeError('Test account cleanup failed: ' + '; '.join(errors))
