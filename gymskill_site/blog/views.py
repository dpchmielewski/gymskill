from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author':'gymadmin',
		'title': 'Blogpost 1',
		'content': 'First post content',
		'date_posted': 'August 21, 2023'
	},
{
		'author':'gymadmin',
		'title': 'Blogpost 2',
		'content': 'First post content',
		'date_posted': 'August 22, 2023'
	}
]

def home(request):
	context = {
		'posts': posts,
		'title': 'Blog'
	}
	return render(request, 'blog/home.html', context)

def about(request):
	context = {
		'title': 'About'
	}
	return render(request, 'blog/about.html', context)
