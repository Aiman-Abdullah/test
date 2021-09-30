from django.shortcuts import render
import pandas as pd
from django_pandas.io import read_frame
# from firstUI.models import Tempcolor


def testPage(request):

    return render(request,'test_index.html')
