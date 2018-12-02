from django.shortcuts import render

# Create your views here.
def test(requests):

    return  render(requests, 'tests/test.html')