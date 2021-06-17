from django.shortcuts import render,get_object_or_404
from django.views import generic
from .forms import UploadForm
from .utils import detectImg
from .models import Upload
# Create your views here.



class UploadImage(generic.CreateView):
	form_class = UploadForm
	template_name = 'upload/index.html'

	def post(self,request):
		form = self.form_class(request.POST or None,request.FILES or None)
		form.save()

		return super().form_valid(form)


class ShowImage(generic.DetailView):
	model = Upload
	template_name = 'upload/detected_image.html'

	def get(self,request,*args,**kwargs):
		objs = probs = []
		
		imgObj = Upload.objects.get(pk = kwargs['pk'])
		if not imgObj.det_objects or not imgObj.det_probabilty:
			detections = detectImg(imgObj.image.name)

			results_object = results_per=""
			for item in detections:
				results_object += item["name"]+"#"
				results_per += str(item["percentage_probability"])+"#"
				

			imgObj.det_objects = results_object
			imgObj.det_probabilty = results_per
			imgObj.save()


		objs = imgObj.det_objects.rstrip('#').split('#')
		probs = imgObj.det_probabilty.rstrip('#').split('#')
		
		res = zip(objs,probs)
        
		post = get_object_or_404(Upload,pk=kwargs['pk'])
		context = {'post':post,'res':res}
		return render(request,self.template_name,context)


