from django.db import models


class AnalysisTask(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class DataSource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class DataIntegration(models.Model):
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    integration_date = models.DateField()
    integration_details = models.TextField()


class DataPreprocessing(models.Model):
    preprocessing_date = models.DateField()
    preprocessing_details = models.TextField()


class AnalyticalResult(models.Model):
    task = models.ForeignKey(AnalysisTask, on_delete=models.CASCADE)
    result_data = models.JSONField()
    result_visualization = models.ImageField(upload_to='analysis_results/')


class DescriptiveAnalytics(models.Model):
    analytics_date = models.DateField()
    summary_statistics = models.TextField()
    visualization = models.ImageField(upload_to='descriptive_analytics/')


class DiagnosticAnalytics(models.Model):
    analytics_date = models.DateField()
    insights = models.TextField()
    correlation_analysis = models.TextField()


class PredictiveModel(models.Model):
    model_name = models.CharField(max_length=100)
    model_type = models.CharField(max_length=50)
    training_data = models.ForeignKey(DataSource,
                                      related_name='training_data',
                                      on_delete=models.CASCADE)
    prediction_results = models.ImageField(upload_to='predictive_models/')


class PrescriptiveAnalytics(models.Model):
    analytics_date = models.DateField()
    recommendations = models.TextField()


class DashboardConfiguration(models.Model):
    dashboard_name = models.CharField(max_length=100)
    dashboard_description = models.TextField()
    configuration_data = models.JSONField()
