# tests.py
from django.test import TestCase
from .models import IssueTypes

class IssueTypesModelTest(TestCase):

    def setUp(self):
        # Create an instance of IssueTypes for testing
        self.issue_type = IssueTypes.objects.create(
            issue_type_id='IT-001',
            issue_type_name='Bug',
            description='An issue that indicates a bug in the system.'
        )

    def test_issue_type_creation(self):
        # Verify that the issue type was created correctly
        print("++++++++++++++++++++++Issue Type Creation ++++++++++++++++++++++++++")
        self.assertEqual(self.issue_type.issue_type_id, 'IT-001')
        self.assertEqual(self.issue_type.issue_type_name, 'Bug')
        self.assertEqual(self.issue_type.description, 'An issue that indicates a bug in the system.')

    def test_string_representation(self):
        # Verify the string representation of the issue type
        print('++++++++++++++test_string_representation+++++++++++++++++++++++')
        self.assertEqual(str(self.issue_type), 'Bug')
