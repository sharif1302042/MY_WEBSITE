from django.urls import path,include
from Python import views

urlpatterns = [
    path('PythonHome',views.PythonHome,name='Python/PythonHome'),
	
    path('dictionary_operation/',views.dictionary_operation,name='Python/dictionary_operation'),
    path('built_in_function/',views.built_in_function,name='Python/built_in_function'),
	path('built_in_function2/',views.built_in_function2,name='Python/built_in_function2'),
	path('list_operation/',views.list_operation,name='Python/list_operation'),
	path('string_operation/',views.string_operation,name='Python/string_operation'),
	path('list_comprehension/',views.list_comprehension,name='Python/list_comprehension'),
	path('itertools/',views.itertools,name='Python/itertools'),

	

]
