from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import*
from django.contrib import messages


class IndexView(View):
    def get(self, request,*args ,**kwargs):
        return render(request, 'index.html')
    def post(self , request):
        pass

class LivrosView(View):
    def get(self, request,*args ,**kwargs):
        livros = Livro.objects.all()
        return render(request, 'livro.html',{'livros': livros})
    def post(self , request):
        pass

class EmprestimoView(View):
    def get(self, request, *args, **kwargs):
        reservas = Emprestimo.objects.all()
        return render(request, 'reserva.html',{'reservas': reservas})
    
class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades':
cidades})

class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores':
autores})

class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html',
{'editoras': editoras})

class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Usuario.objects.all()
        return render(request, 'usuario.html',
{'leitores': leitores})


class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos':
generos})


class DeleteLivroView(View):
    def get(self, request, id, *args, **kwargs):
        livro = Livro.objects.get(id=id)
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!') # Mensagem de sucesso
        return redirect('livros')

class EditarLivroView(View):
    template_name = 'editar_livro.html'
    def get(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)
        form = LivroForm(instance=livro)
        return render(request, self.template_name, {'livro': livro, 'form': form})
    
    def post(self, request, id, *args, **kwargs):
            livro = get_object_or_404(Livro, id=id)
            form = LivroForm(request.POST, instance=livro)
            if form.is_valid():
                form.save()
                messages.success(request, 'As edições foram salvas comsucesso.')
                return redirect('editar', id=id) # Redirecionar de volta para a página de edição
            else:
                messages.error(request, 'Corrija os erros no formulárioantes de enviar novamente.')
                return render(request, self.template_name, {'livro': livro,'form': form})
            
