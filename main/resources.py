from import_export import resources
from main.models import Student

class StudentResource(resources.ModelResource):

    class Meta:
        model = Student