from django.shortcuts import render,render_to_response,get_object_or_404


def showReport(req):
    return render_to_response("report.html")
