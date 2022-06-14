import unittest

import pytest
from assertions import assert_

from pages.navbar import Navbar
from pages.students_page import StudentsPage


@pytest.mark.usefixtures("setup")
class SmokeTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def before_test(self, setup):
        self.project_page = StudentsPage(setup)
        self.navbar = Navbar(setup)

    def test_smoke_is_login_signup_available(self):
        assert_(True, self.navbar.is_login_sign_up_button_available())
