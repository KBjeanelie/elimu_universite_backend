from django.conf.urls.static import static
from django.urls import path

from elimu_universite import settings
from manager_dashboard.views.administration_view import TypeDocumentDeleteView, TypeDocumentView, TypeSanctionDeleteView, TypeSanctionView, SettingAppView, get_last_document_type, get_last_sanction_type
from manager_dashboard.views.communication_view import AddEventView, AddInformationView, EditEventView, EventView, GroupDiscussionView, InformationView
from manager_dashboard.views.comptes_view import AddStudentAccount, AddTeacherAccount, ListAllStudentAccount, ListAllTeacherAccount, StudentAccountDeleteView, TeacherAccountDeleteView
from manager_dashboard.views.contenu_pedagogique_view import AddeBook, FilesView, FolderViews, eBookDeleteView, eBookView
from manager_dashboard.views.gestion_universite_view import AddProgramView, AddSanctionView, AddSubjectView, EditProgramView, EditSanctionView, EditSubjectView, GroupSubjectView, ProgramView, SanctionAppreciationView, StudentDetailView, SubjectView, TeacherDetailView, TrombinoscopeView
from manager_dashboard.views.home_view import ManagerIndexView


app_name = 'manager_dashboard'
urlpatterns = [
    path(route='', view=ManagerIndexView.as_view(), name='index'),
    path(route='gestion_universite/groupe-de-matières/', view=GroupSubjectView.as_view(), name='group_subjects'),
    path(route='gestion_universite/groupe-de-matières/<int:pk>/delete/', view=GroupSubjectView.as_view(), name='delete_group_subjects'),
    
    path(route='gestion_universite/matières/', view=SubjectView.as_view(), name='subjects'),
    path(route='gestion_universite/matières/ajouter/', view=AddSubjectView.as_view(), name='add_subject'),
    path(route='gestion_universite/matières/<int:pk>/editer/', view=EditSubjectView.as_view(), name='edit_subject'),
    path(route='gestion_universite/matières/<int:pk>/delete/', view=SubjectView.as_view(), name='delete_subject'),
    
    path(route='gestion_universite/programmes/', view=ProgramView.as_view(), name='programs'),
    path(route='gestion_universite/programmes/ajouter/', view=AddProgramView.as_view(), name='add_program'),
    path(route='gestion_universite/programmes/<int:pk>/editer/', view=EditProgramView.as_view(), name='edit_program'),
    path(route='gestion_universite/programmes/<int:pk>/delete/', view=ProgramView.as_view(), name='delete_program'),
    
    path(route='gestion_universite/sanctions-&-appreciations/', view=SanctionAppreciationView.as_view(), name='sanction_appreciations'),
    path(route='gestion_universite/sanctions-&-appreciations/ajouter/', view=AddSanctionView.as_view(), name='add_sanction'),
    path(route='gestion_universite/sanctions-&-appreciations/<int:pk>/editer/', view=EditSanctionView.as_view(), name='edit_sanction'),
    path(route='gestion_universite/sanctions-&-appreciations/<int:pk>/delete/', view=SanctionAppreciationView.as_view(), name='delete_sanction'),
    
    path(route='gestion_universite/trombinoscopes/', view=TrombinoscopeView.as_view(), name='trombinoscopes'),
    path(route='gestion_universite/students/<int:pk>/detail/', view=StudentDetailView.as_view(), name='student_detail'),
    path(route='gestion_universite/teachers/<int:pk>/detail/', view=TeacherDetailView.as_view(), name='teacher_detail'),
    #===END
    
    #=================== THIS ROUTE IS FOR Communication MODULE ========================
    path(route='communication/group-discussions/', view=GroupDiscussionView.as_view(), name='discussion_group'),
    path(route='communication/group-discussions/<int:pk>/delete/', view=GroupDiscussionView.as_view(), name='delete_discussion_group'),
    path(route='communication/informations/', view=InformationView.as_view(), name='informations'),
    path(route='communication/informations/<int:pk>/delete/', view=InformationView.as_view(), name='delete_information'),
    path(route='communication/informations/ajouter/', view=AddInformationView.as_view(), name='add_information'),
    path(route='communication/events/', view=EventView.as_view(), name='events'),
    path(route='communication/events/<int:pk>/edit/', view=EditEventView.as_view(), name='edit_event'),
    path(route='communication/events/<int:pk>/delete/', view=EventView.as_view(), name='delete_events'),
    path(route='communication/events/ajouter/', view=AddEventView.as_view(), name='add_event'),
    #===ENDS
    
    #=========================== THIS ROUTE IS FOR CONTENUE PEDAGOGIQUE MODULE ======================#
    path(route='contenue_pedagogique/ebooks/', view=eBookView.as_view(), name="ebooks"),
    path(route='contenue_pedagogique/ebooks/ajouter/', view=AddeBook.as_view(), name='add_ebook'),
    path(route='contenue_pedagogique/ebooks/<int:pk>/delete/', view=eBookDeleteView.as_view(), name="delete_ebook"),
    path(route='contenue_pedagogique/dossiers/', view=FolderViews.as_view(), name='folders'),
    path(route='contenue_pedagogique/dossiers/<int:folder_id>', view=FilesView.as_view(), name='content_folder'),
    path(route='contenue_pedagogique/fichier/ajouter/', view=FilesView.as_view(), name='add_file'),
    #===END
    
    #=================== THIS ROUTE IS FOR Compte MODULE ===============================#
    path(route='comptes/compte_enseignants/', view=ListAllTeacherAccount.as_view(), name='teachers_account'),
    path(route='comptes/compte_enseignants/ajouter/', view=AddTeacherAccount.as_view(), name='add_teacher_account'),
    path(route='comptes/compte_enseignants/<int:pk>/delete/', view=TeacherAccountDeleteView.as_view(), name='delete_teacher_account'),
    path(route='comptes/compte_etudiants/', view=ListAllStudentAccount.as_view(), name='students_account'),
    path(route='comptes/compte_etudiants/ajouter/', view=AddStudentAccount.as_view(), name='add_student_account'),
    path(route='comptes/compte_etudiants/<int:pk>/delete/', view=StudentAccountDeleteView.as_view(), name='delete_student_account'),
    #===END
    #=================== THIS ROUTE IS FOR ADMINISTRATION MODULE ========================
    # path(route='administration/type_evaluation/', view=TypeEvaluationView.as_view(), name='type_evaluation'),
    path(route='administration/type_documents/', view=TypeDocumentView.as_view(), name='type_documents'),
    path(route='administration/type_documents/<int:pk>/delete/', view=TypeDocumentDeleteView.as_view(), name='delete_type_document'),
    path(route='administration/type_documents/last/', view=get_last_document_type),
    path(route='administration/type_sanctions/', view=TypeSanctionView.as_view(), name='type_sanctions'),
    path(route='administration/type_sanctions/<int:pk>/delete/', view=TypeSanctionDeleteView.as_view(), name='delete_type_sanction'),
    path(route='administration/type_sanctions/last/', view=get_last_sanction_type),
    path(route='administration/reglage-general/', view=SettingAppView.as_view(), name='reglage_general'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)