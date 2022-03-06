from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from employee.forms import EmployeeForm

from django.views.generic import DetailView
from employee.models import Employee


class EmployeeImage(TemplateView):
    form = EmployeeForm
    template_name = 'emp_image.html'

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()

            return HttpResponseRedirect(reverse_lazy('emp_image_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class EmpImageDisplay(DetailView):
    model = Employee
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'


def plant(request):
    import tensorflow
    result1 = Employee.objects.latest('id')
    import numpy as np
    #from tensorflow import keras
    import h5py
    models = tensorflow.keras.models.load_model('C:/Users/vikas/Desktop/PLANT LEAF/Deploy/employee/plant1.h5')
    from tensorflow.keras.preprocessing import image
    test_image = image.load_img('C:/Users/vikas/Desktop/PLANT LEAF/Deploy/media/' + str(result1),target_size=(225, 225))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = models.predict(test_image)
    prediction = result[0]
    prediction = list(prediction)
    classes=['Apple Disease','Apple healthy','Cherry Disease','Cherry healthy','Grape Disease','Grape healthy','Peach Bacterial','Peach healthy','Strawberry Disease','Strawberry healthy']
    output = zip(classes, prediction)
    output = dict(output)
    if output['Apple Disease'] == 1.0:
        a = "Apple Disease Leaf"
    elif output['Apple healthy'] == 1.0:
        a = "Apple healthy Leaf"
    elif output['Cherry Disease'] == 1.0:
        a = "Cherry Disease Leaf"
    elif output['Cherry healthy'] == 1.0:
        a = "Cherry healthy Leaf"
    elif output['Grape Disease'] == 1.0:
        a = "Grape Disease Leaf"
    elif output['Grape healthy'] == 1.0:
        a = "Grape healthy Leaf"
    elif output['Peach Bacterial'] == 1.0:
        a = "Peach Bacterial Leaf"
    elif output['Peach healthy'] == 1.0:
        a = "Peach healthy Leaf"
    elif output['Strawberry Disease'] == 1.0:
        a = "Strawberry Disease Leaf"
    elif output['Strawberry healthy'] == 1.0:
        a = "Strawberry healthy Leaf"

    return render(request, "result.html", {"out": a})
