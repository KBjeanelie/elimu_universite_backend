from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from module_invoice_and_accounting.forms import ItemForm
from module_invoice_and_accounting.models import Item

#=============================== PARTIE CONCERNANT LES ARTICLES ==========================
class EditItemView(View):
    template = "accountant_dashboard/administration/edit_article.html"
    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Item, pk=pk)
        form = ItemForm(instance=item)
        context = {'form':form, 'item':item}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Item, pk=pk)
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('accountant_dashboard:items')  # Redirigez vers la page appropriée après la mise à jour réussie
        # Si le formulaire n'est pas valide, réaffichez le formulaire avec les erreurs
        context = {'form': form, 'item': item}
        return render(request, template_name=self.template, context=context)
    
class AddItemView(View):
    template = "accountant_dashboard/administration/ajout_article.html"
    def get(self, request, *args, **kwargs):
        form = ItemForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)
    
    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accountant_dashboard:items")
        form = ItemForm()
        context = {'form':form}
        return render(request, template_name=self.template, context=context)

class ItemView(View):
    template = "accountant_dashboard/administration/articles.html"

    def get(self, request, *args, **kwargs):
        items = Item.objects.all().order_by('-created_at')
        context = {'items': items}
        return render(request, template_name=self.template, context=context)
    
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Item, pk=pk)
        instance.delete()
        items = Item.objects.all().order_by('-created_at')
        context = {'items': items}
        return render(request, template_name=self.template, context=context)
    
#===END