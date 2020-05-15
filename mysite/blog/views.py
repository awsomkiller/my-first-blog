from django.shortcuts import render

# Create your views here.
def post_list(request):
	return rentder(request,'blog/post_list.html',{})
