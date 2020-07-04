from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from markdown2 import Markdown
from django.urls import reverse
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "page_title":"Encyclopedia",
        "heading":"All Pages",
        "entries": util.list_entries()
    })

def entry(request,title):
    if util.get_entry(title) is None:
        return render(request, "encyclopedia/error.html",{
            "message":"The requested page was not found."
        })

    markdowner = Markdown()
    content = markdowner.convert(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        'title':title,
        'content':content
    })


def search(request):
    if request.method == "POST":
        q = request.POST["q"]
        results = util.get_entry(q)
        if results is None:
            results = util.search_entry(q)
            return render(request, "encyclopedia/index.html", {
            "page_title":"Search",
            "heading":"Search Results",
            "entries": results
            })

        return HttpResponseRedirect(reverse("encyclopedia:entry",args=(q,)))
        
def newitem(request):
    if request.method == "GET":
        return render(request,"encyclopedia/newitem.html")
    
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        save = util.new_entry(title, content)
        if save == "error":
            return render(request, "encyclopedia/error.html", {
                "message":"A page with the same title already exists. Please try another title."
            } )
        
        return HttpResponseRedirect(reverse("encyclopedia:entry",args=(title,)))

def randompage(request):
    results = util.search_entry("")
    title = random.choice(results)
    return HttpResponseRedirect(reverse("encyclopedia:entry",args=(title,)))

def edit(request, title):
    if request.method == 'GET':
        return render(request, "encyclopedia/edit.html",{
            'title':title,
            'content':util.get_entry(title)
        })
    
    elif request.method == 'POST':
        content = request.POST["content"]
        save = util.save_entry(title, content)
        if save != "success":
            return render(request, "encyclopedia/error.html", {
                'message': 'The entry could not be modified.'
            })
        return HttpResponseRedirect(reverse("encyclopedia:entry",args=(title,)))
        



