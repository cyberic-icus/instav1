from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("""<h1> API URLS: </h1> 
	 <li> /api/v1/<int:pk>/ </li>
	 <li> /api/v1/<int:pk>/update </li>
	 <li> /api/v1/<int:pk>/posts/ </li>
	 <li> /api/v1/posts/ </li> 
	 <li> /api/v1/posts/create </li>
	 <li> /api/v1/posts/<int:pk> </li>
	 <li> /api/v1/posts/<int:pk>/update </li>
	 <li> /api/v1/admin/delete-users/ </li>
	 <li> /api/v1/auth/login </li>
	 <li> /api/v1/auth/registration </li>
	 
	 
	 """)
