from django.shortcuts import render, redirect
from .models import Post, Blog, Mensagem
from .forms import MensagemForm

def index(request):
    context = {
        "posts" : Post.objects.all(),
        "blog" : Blog.objects.first(),
    }
    return render(request, "index.html", context)

def contact(request):                                                                                                                                                                                                                                                                     
    context = {
            "blog" : Blog.objects.first(),
        }

    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, "contact.html", context)
    
    else:
        context["form"] = MensagemForm()
        return render(request, "contact.html", context)

def post(request, post_id):
    context = {
        "post" : Post.objects.get(pk=post_id),
        "blog" : Blog.objects.first(),
    }
    return render(request, "post.html", context)

def about(request):
    context = {
        "blog" : Blog.objects.first(),
    }
    return render(request, "about.html", context)

def mensagens(request):
    context = {
        "mensagens" : Mensagem.objects.all(),
        "blog" : Blog.objects.first(),
    }
    return render(request, "mensagens.html", context)

def editar_mensagem(request, mensagem_id):
    context = {
        "blog" : Blog.objects.first(),
        "mensagem" : Mensagem.objects.get(pk = mensagem_id),
    }

    if request.method == "POST":
        context['erro'] = {}
        if not request.POST['nome']:
            context['erro']['nome'] = True
        if not request.POST['email']:
            context['erro']['email'] = True
        if not request.POST['telefone']:
            context['erro']['telefone'] = True
        if not request.POST['mensagem']:
            context['erro']['mensagem'] = True
        if context['erro']:
            return render(request, "editcontact.html", context)
        
        mensagem = context ["mensagem"]
        mensagem.nome = request.POST['nome']
        mensagem.email = request.POST['email']
        mensagem.telefone = request.POST['telefone']
        mensagem.mensagem = request.POST['mensagem']

        mensagem.save()

    return render(request, "editcontact.html", context)

def deletar_mensagem(request, mensagem_id):
    context = {
        "blog" : Blog.objects.first(),
        "mensagem" : Mensagem.objects.get(pk = mensagem_id),
    }

    if request.method == "POST":
        context["mensagem"].delete()
        return redirect("mensagens")
    
    else:
        return render(request, "deletecontact.html", context)

def cadastro(request):
    context = {
        "blog" : Blog.objects.first(),
    }
    return render(request, "cadastro.html", context)