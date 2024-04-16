from django.test import TestCase
from .models import AnalysisTask, DataSource, DataIntegration
from .models import DataPreprocessing, AnalyticalResult
"""
from .models import DiagnosticAnalytics, PredictiveModel, DescriptiveAnalytics
from .models import PrescriptiveAnalytics, DashboardConfiguration
"""


class DataAnalyticModelTestCase(TestCase):
    def setUp(self):
        """ Create sample analysis task for testing """
        self.analysis_task = AnalysisTask.objects.create(
                task_name='Sample Task',
                task_description='Description of sample task',
                status='Pending',
                )
        """ Create sample data source for testing """
        self.data_source = DataSource.objects.create(
                name='Sample Source',
                description='Description of sample source',
                )

    def test_data_integration_creation(self):
        """ Test creating data integration record """
        data_integration = DataIntegration.objects.create(
                source=self.data_source,
                integration_date='2024-04-12',
                integration_details='Details of data integration',
                )
        self.assertIsNotNone(data_integration)

    def test_data_preprocessing_creation(self):
        """ Test creating data preprocessing record """
        data_preprocessing = DataPreprocessing.objects.create(
                preprocessing_date='2024-04-12',
                preprocessing_details='Details of data preprocessing',
                )
        self.assertIsNotNone(data_preprocessing)

    def test_analytical_result_creation(self):
        """ Test creating analytical result record """
        analytical_result = AnalyticalResult.objects.create(
                task=self.analysis_task,
                result_data={'key': 'value'},
                result_visualization='analysis_results/image.jpg',
                )
        self.assertIsNotNone(analytical_result)
