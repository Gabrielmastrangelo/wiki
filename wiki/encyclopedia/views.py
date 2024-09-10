from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page(request, title):
    import markdown2

    page_content = util.get_entry(title)
    html_content = markdown2.markdown(page_content)


    return render(request, "encyclopedia/page.html", {
        "page": html_content,
        "page_title": title
    })

def search(request):
    form = request.GET

    if util.get_entry(form['q']) != None:
        return HttpResponseRedirect(reverse("title", kwargs={"title": form['q']}))
    else:
        list_entries = util.list_entries()
        list_substrings = [entry for entry in list_entries if form['q'] in entry]
        #print(list_entries)
        return render(request, "encyclopedia/search.html", {
            'list': list_substrings
        })

def new_page(request):
    if request.method == 'POST':
        form = request.POST

        if util.get_entry(form['title']):
            # There exist already a page with the same tittle
            return render(request, "encyclopedia/new_page.html", {
                'error': True
            })
        else:
            # If such page does not exist, then we create it
            util.save_entry(form['title'], form['content'])
            return HttpResponseRedirect(reverse("title", kwargs={"title": form['title']}))
    
    return render(request, "encyclopedia/new_page.html", {
                    'error': False
                })

def edit(request, title):
    page_content = util.get_entry(title)

    if request.method == 'POST':
        util.save_entry(title, page_content)
        return HttpResponseRedirect(reverse("title", kwargs={"title": title}))


    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": page_content
    })



def random(request):
    import random

    sample = random.sample(util.list_entries(), 1)

    return HttpResponseRedirect(reverse("title", kwargs={"title": sample[0]}))


