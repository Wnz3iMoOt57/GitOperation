from django.contrib import messages, admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from employees.constants import EDUCATION_FORMS_PREFIX, WORK_EXPERIENCE_FORMS_PREFIX, PROJECT_FORMS_PREFIX, \
    CERTIFICATION_FORMS_PREFIX, SKILL_FORMS_PREFIX, TRAINING_EXPERIENCE_FORMS_PREFIX, CARD_FORMS_PREFIX, \
    CONTACT_FORMS_PREFIX, SALARY_FORMS_PREFIX, PROJROM_FORMS_PREFIX
from employees.forms import ResumeForm, EducationForm, EducationFormSetHelper, WorkExperienceForm, \
    WorkExperienceFormSetHelper, ProjectForm, ProjectFormSetHelper, CertificationForm, CertificationFormSetHelper, \
    SkillForm, SkillFormSetHelper, TrainingExperienceForm, TrainingExperienceFormSetHelper, IdCardForm, CardForm, \
    ContactForm, CardFormSetHelper, ContactFormSetHelper, SalaryFormSetHelper, SalaryForm, StudentForm,DailyReportForm
from employees.models import Education, WorkExperience, Project, Certification, Skill, TrainingExperience, Card, \
    ContactPerson, Salary, WorkProject, Student


def form_in_formset_is_valid(form):
    return not (form.empty_permitted and not form.has_changed()) and form.is_valid()


@login_required
def profile(request):
    EducationFormSet = inlineformset_factory(User, Education, form=EducationForm, extra=1)
    WorkExperienceFormSet = inlineformset_factory(User, WorkExperience, form=WorkExperienceForm, extra=1)
    ProjectFormSet = inlineformset_factory(User, Project, form=ProjectForm, extra=1)
    CertificationFormSet = inlineformset_factory(User, Certification, form=CertificationForm, extra=1)
    SkillFormSet = inlineformset_factory(User, Skill, form=SkillForm, extra=2)
    TrainingExperienceFormSet = inlineformset_factory(User, TrainingExperience, form=TrainingExperienceForm, extra=1)

    if request.method == 'POST':
        resume_instance = None
        if hasattr(request.user, 'resume'):
            resume_instance = request.user.resume
        form = ResumeForm(request.POST or None, instance=resume_instance)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            form.save()

        education_forms = EducationFormSet(request.POST or None, instance=request.user, prefix=EDUCATION_FORMS_PREFIX)
        if education_forms.is_valid():
            education_forms.save()

        work_experience_forms = WorkExperienceFormSet(request.POST or None, instance=request.user,
                                                      prefix=WORK_EXPERIENCE_FORMS_PREFIX)
        if work_experience_forms.is_valid():
            work_experience_forms.save()

        project_forms = ProjectFormSet(request.POST or None, instance=request.user, prefix=PROJECT_FORMS_PREFIX)
        if project_forms.is_valid():
            project_forms.save()

        certification_forms = CertificationFormSet(request.POST or None, instance=request.user,
                                                   prefix=CERTIFICATION_FORMS_PREFIX)
        if certification_forms.is_valid():
            certification_forms.save()

        skill_forms = SkillFormSet(request.POST or None, instance=request.user, prefix=SKILL_FORMS_PREFIX)
        if skill_forms.is_valid():
            skill_forms.save()

        training_experience_forms = TrainingExperienceFormSet(request.POST or None, instance=request.user,
                                                              prefix=TRAINING_EXPERIENCE_FORMS_PREFIX)
        if training_experience_forms.is_valid():
            training_experience_forms.save()

        if 'submit-profile' in request.POST:
            resume = request.user.resume
            resume.is_submitted = True
            resume.save()
            messages.success(request, '提交成功')
        else:
            messages.success(request, '保存成功')

    if hasattr(request.user, 'employee'):
        return redirect('employee_profile')

    if hasattr(request.user, 'resume'):
        form = ResumeForm(instance=request.user.resume)

        if request.user.resume.is_submitted:
            user = request.user
            return render(request, 'employees/profile-view.html', {'user': user})
    else:
        form = ResumeForm()

    education_forms = EducationFormSet(instance=request.user, prefix=EDUCATION_FORMS_PREFIX)
    education_forms_helper = EducationFormSetHelper()

    work_experience_forms = WorkExperienceFormSet(instance=request.user, prefix=WORK_EXPERIENCE_FORMS_PREFIX)
    work_experience_forms_helper = WorkExperienceFormSetHelper()

    project_forms = ProjectFormSet(instance=request.user, prefix=PROJECT_FORMS_PREFIX)
    project_forms_helper = ProjectFormSetHelper()

    certification_forms = CertificationFormSet(instance=request.user, prefix=CERTIFICATION_FORMS_PREFIX)
    certification_forms_helper = CertificationFormSetHelper()

    skill_forms = SkillFormSet(instance=request.user, prefix=SKILL_FORMS_PREFIX)
    skill_forms_helper = SkillFormSetHelper()

    training_experience_forms = TrainingExperienceFormSet(instance=request.user,
                                                          prefix=TRAINING_EXPERIENCE_FORMS_PREFIX)
    training_experience_forms_helper = TrainingExperienceFormSetHelper()

    return render(request, 'employees/profile.html',
                  {'form': form, 'education_forms': education_forms, 'education_forms_helper': education_forms_helper,
                   'work_experience_forms': work_experience_forms,
                   'work_experience_forms_helper': work_experience_forms_helper,
                   'project_forms': project_forms, 'project_forms_helper': project_forms_helper,
                   'certification_forms': certification_forms, 'certification_forms_helper': certification_forms_helper,
                   'skill_forms': skill_forms, 'skill_forms_helper': skill_forms_helper,
                   'training_experience_form': training_experience_forms,
                   'training_experience_forms_helper': training_experience_forms_helper,
                   })


@login_required
def employee_profile(request):
    if hasattr(request.user, 'employee'):
        CardFormSet = inlineformset_factory(User, Card, form=CardForm, extra=1)
        ContactFormSet = inlineformset_factory(User, ContactPerson, form=ContactForm, extra=1)
        if request.method == 'POST':
            id_card_instance = None
            if hasattr(request.user, 'idcard'):
                id_card_instance = request.user.idcard
            id_card_form = IdCardForm(request.POST or None, instance=id_card_instance)
            if id_card_form.is_valid():
                id_card = id_card_form.save(commit=False)
                id_card.user = request.user
                id_card_form.save()

            card_forms = CardFormSet(request.POST or None, instance=request.user, prefix=CARD_FORMS_PREFIX)
            if card_forms.is_valid():
                card_forms.save()

            contact_forms = ContactFormSet(request.POST or None, instance=request.user, prefix=CONTACT_FORMS_PREFIX)
            if contact_forms.is_valid():
                contact_forms.save()

            if 'submit-profile' in request.POST:
                employee = request.user.employee
                employee.is_submitted = True
                employee.save()
                messages.success(request, '提交成功')
            else:
                messages.success(request, '保存成功')

        if request.user.employee.is_submitted:
            user = request.user
            return render(request, 'employees/profile-view.html', {'user': user})

        id_card_form = IdCardForm()
        if hasattr(request.user, 'idcard'):
            id_card_form = IdCardForm(instance=request.user.idcard)
        card_forms = CardFormSet(instance=request.user, prefix=CARD_FORMS_PREFIX)
        card_forms_helper = CardFormSetHelper()
        contact_forms = ContactFormSet(instance=request.user, prefix=CONTACT_FORMS_PREFIX)
        contact_forms_helper = ContactFormSetHelper()
        return render(request, 'employees/profile-employee.html',
                      {
                          'id_card_form': id_card_form,
                          'card_forms': card_forms, 'card_forms_helper': card_forms_helper,
                          'contact_forms': contact_forms, 'contact_forms_helper': contact_forms_helper,
                      })
    else:
        return redirect('profile')


@staff_member_required
def interview_resume(request, pk):
    user = User.objects.get(pk=pk)

    template = 'employees/profile-view.html'
    return render(request, template, {'user': user})


def home(request):
    if hasattr(request.user, 'employee'):
        return redirect('employee_profile')
    else:
        return redirect('profile')


@login_required()
def newStaff(request):
    resume_form = ResumeForm()
    education_form = EducationForm()
    workexperience_form = WorkExperienceForm()
    certification_form = CertificationForm()
    skill_form= SkillForm()
    training_form = TrainingExperienceForm()
    student_form = StudentForm()
    return render(request, 'employees/general.html', {'resume_form': resume_form,
                                                      'education_form': education_form,
                                                      'workexperience_form': workexperience_form,
                                                      'certification_form': certification_form,
                                                      'skill_form': skill_form,
                                                      'training_form': training_form,
                                                      'student_form': student_form})


@login_required()
def test(request):
    report_forms = DailyReportForm()
    resume_form = ResumeForm()
    education_form = EducationForm()
    workexperience_form = WorkExperienceForm()
    certification_form = CertificationForm()
    skill_form = SkillForm()
    training_form = TrainingExperienceForm()
    student_form = StudentForm()
    return render(request,'employees/test.html',{'report_forms':report_forms,
                                                 'resume_form': resume_form,
                                                 'education_form': education_form,
                                                 'workexperience_form': workexperience_form,
                                                 'certification_form': certification_form,
                                                 'skill_form': skill_form,
                                                 'training_form': training_form,
                                                 'student_form': student_form
                                                 })