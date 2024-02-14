from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from backend.models.gestion_ecole import AcademicYear, StudentCareer
from backend.models.user_account import Student


class AccountantIndexView(View):
    template_name = "accountant_dashboard/index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

#================================
class PreRegistrationView(View):
    template = "accountant_dashboard/communication/pre-inscription.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        try:
            active_year = AcademicYear.objects.get(status=True, school=request.user.school)
        except AcademicYear.DoesNotExist:
            return redirect('manager_dashboard:no_year')
        
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            academic_year = AcademicYear.objects.get(status=True, school=request.user.school)
            students = StudentCareer.objects.filter(academic_year=academic_year, is_registered=False).order_by('-created_at')
            context = {'student_careers':students, 'year':academic_year}
            return render(request, template_name=self.template, context=context)
        except AcademicYear.DoesNotExist:
            # Exécuter du code alternatif si l'objet AcademicYear n'existe pas
           return render(request, template_name=self.template)
        

class PreRegistrationDetailView(View):
    template = "accountant_dashboard/communication/pre-inscription_detail.html"
    
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('backend:login')
        
        try:
            active_year = AcademicYear.objects.get(status=True, school=request.user.school)
        except AcademicYear.DoesNotExist:
            return redirect('manager_dashboard:no_year')
        
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk, *args, **kwargs):
        academic_year = AcademicYear.objects.get(status=True, school=request.user.school)
        student_career = get_object_or_404(StudentCareer, pk=pk, academic_year=academic_year)
        context = {'student_career':student_career}
        return render(request, template_name=self.template, context=context)
    
    def check(self, pk, *args, **kwargs):
        student_career = get_object_or_404(StudentCareer, pk=pk)
        student_career.is_registered = True
        student_career.save()
        
        if student_career.student:
            student_career.student.is_valid = True
            student_career.student.save()
        return redirect('accountant_dashboard:pre_registrations')
    
    def delete(self, pk, *args, **kwargs):
        academic_year = get_object_or_404(AcademicYear, status=True)
        student_career = get_object_or_404(StudentCareer, pk=pk, academic_year=academic_year)
        student = get_object_or_404(Student, id=student_career.student.id)
        student_career.delete()
        student.delete()
        return redirect('accountant_dashboard:pre_registrations')
#===END