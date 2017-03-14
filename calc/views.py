from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def suma(request, op1, op, op2):
    return HttpResponse("<h1>" + op1 + op + op2 + "=" +
                        str(int(op1) + int(op2)) + "</h1>")


def resta(request, op1, op, op2):
    return HttpResponse("<h1>" + op1 + op + op2 + "=" +
                        str(int(op1) - int(op2)) + "</h1>")


def mult(request, op1, op, op2):
    return HttpResponse("<h1>" + op1 + op + op2 + "=" +
                        str(int(op1) * int(op2)) + "</h1>")


def div(request, op1, op, op2):
    return HttpResponse("<h1>" + op1 + op + op2 + "=" +
                        str(int(op1) / int(op2)) + "</h1>")


def error(request, parametro):
    return HttpResponse("<h1>Not Found</h1>")
