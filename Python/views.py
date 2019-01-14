from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def PythonHome(request):
    return render(request,'index.html')

def built_in_function(request):
	return render(request, 'built_in_function.html', {})

def built_in_function2(request):
	return render(request, 'built_in_function2.html', {})

def list_operation(request):
	return render(request, 'list_operation.html', {})

def string_operation(request):
	return render(request, 'string_operation.html', {})

def dictionary_operation(request):
	return render(request, 'dictionary_operation.html', {})

def list_comprehension(request):
	return render(request,'list_comprehension.html')

def itertools(request):
	return render(request,'itertools.html')
