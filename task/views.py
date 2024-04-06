from django.shortcuts import render
from django.views import View
from typing import IO
from TFIDF import tfidf
from DB.db_funcs import get_context, clean_bd

# Create your views here.

def storage_file(file: IO) -> None:
    with open('files/file.txt', 'w', encoding='UTF-8') as f:
        for line in file.readlines():
            decoded_line = line.decode('utf-8').strip()
            print(decoded_line, file=f)

class FileInput(View):
    def get(self, request):
        clean_bd()
        return render(request, 'task/task.html')

    def post(self, request):
        storage_file(request.FILES['file'])
        tfidf('files/file.txt')
        context = get_context()
        return render(request, 'task/table.html',
                      context={'words': context})