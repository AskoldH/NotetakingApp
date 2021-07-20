import select

from django.shortcuts import render, redirect
from .models import Document


def editor(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        priority = request.POST.get('priority')
        saved_priority=Document()
        saved_priority.priority = request.POST.get('priority')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.priority = priority
            document.save()
            return redirect('/?docid=%i' % docid)

        else:
            document = Document.objects.create(priority=priority, title=title, content=content)
            return redirect('/?docid=%i' % document.id)
    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document': document,
    }

    return render(request, 'editor.html', context)

def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()
    return redirect('/?docid=0')