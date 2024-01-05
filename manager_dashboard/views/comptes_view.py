
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from user_account.forms import UserStudentForm, UserTeacherForm

from user_account.models import User

#========================== PARTIE CONCERNANT LA GESTION DE COMPTE ENSEIGNANT
class AddTeacherAccount(View):
    template = "manager_dashboard/comptes/ajout_compte_enseignant.html"
    form = UserTeacherForm()
    context_object = {'form': form}
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context=self.context_object)

class ListAllTeacherAccount(View):
    template = "manager_dashboard/comptes/compte_enseignant.html"
    teachers_account = User.objects.filter(is_teacher=True)
    context_object = {'teachers_account': teachers_account}
    
    def get(self, request, *args, **kwargs):
        
        return render(request, template_name=self.template, context=self.context_object)
    
    def post(self, request, *args, **kwargs):
        form = UserTeacherForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_teacher_user(
                form.cleaned_data['username'],
                form.cleaned_data['teacher'],
                form.cleaned_data['password'],
            )
        return redirect('manager_dashboard:teachers_account')

class TeacherAccountDeleteView(View):
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(User, pk=pk)
        instance.delete()
        return JsonResponse({'message': 'Élément supprimé avec succès'})


#========================== PARTIE CONCERNANT LA GESTION DE COMPTE ETUDIANT
class AddStudentAccount(View):
    template = "manager_dashboard/comptes/ajout_compte_etudiant.html"
    form = UserStudentForm()
    context_object = {'form': form}
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context=self.context_object)

class ListAllStudentAccount(View):
    template = "manager_dashboard/comptes/compte_etudiant.html"
    students_account = User.objects.filter(is_student=True)
    context_object = {'students_account': students_account}
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template, context=self.context_object)
    
    def post(self, request, *args, **kwargs):
        form = UserStudentForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_student_user(
                form.cleaned_data['username'],
                form.cleaned_data['student'],
                form.cleaned_data['password'],
            )
        return redirect('manager_dashboard:students_account')

class StudentAccountDeleteView(View):
    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(User, pk=pk)
        instance.delete()
        return JsonResponse({'message': 'Élément supprimé avec succès'})