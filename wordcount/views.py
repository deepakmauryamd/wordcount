from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def count(request):
    data = request.GET['text']
    data_list = data.split()
    data_list_len = len(data_list)

    data_dictionary = {}

    for word in data_list:
        if word in data_dictionary:
            data_dictionary[word] += 1
        else:
            data_dictionary[word] = 1

    sorted_dict = sorted(data_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'text': data,'data_length': data_list_len, 'data_dictionary': sorted_dict})


def about(request):
    return render(request, 'about.html')

