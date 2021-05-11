from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Div
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, Textarea
from suit_redactor.widgets import RedactorWidget
from employees.constants import *
from employees.models import Resume, Education, WorkExperience, Project, Certification, Skill, TrainingExperience, \
    IdCard, Card, ContactPerson, Salary, WorkProject, RegularMeeting, DailyReport, Student


class LoginForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'login'

        self.helper.field_template = 'bootstrap4/layout/inline_field.html'
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Submit', css_class='btn-block')
        )


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['gender', 'native_place', 'nationality', 'birth_date', 'marital_status',
                  'target_position', 'expect_salary', 'expect_salary_intern',
                  'telephone', 'email', 'qq', 'wechat',
                  'english_level', 'english_score',
                  'height', 'weight',
                  'introduction']
        widgets = {
            'introduction': Textarea(attrs={'rows': 3})
        }

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_resume'
        self.helper.layout = Layout(
            Div(
                Div('gender', css_class='col-xs-2'),
                Div('native_place', css_class='col-xs-2'),
                Div('nationality', css_class='col-xs-2'),
                Div('birth_date', css_class='col-xs-2'),
                Div('height', css_class='col-xs-2'),
                Div('weight', css_class='col-xs-2'),
                css_class='row'
            ),
            Div(
                Div('telephone', css_class='col-xs-3'),
                Div('email', css_class='col-xs-3'),
                Div('qq', css_class='col-xs-3'),
                Div('wechat', css_class='col-xs-3'),
                css_class='row'
            ),
            Div(
                Div('english_level', css_class='col-xs-4'),
                Div('english_score', css_class='col-xs-4'),
                Div('marital_status', css_class='col-xs-4'),
                css_class='row'
            ),
            Div(
                Div('target_position', css_class='col-xs-4'),
                Div('expect_salary', css_class='col-xs-4'),
                Div('expect_salary_intern', css_class='col-xs-4'),

            ),
            Div(
                Div('introduction', css_class='col-xs-12'),
                css_class='row'
            )
        )


class EducationFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(EducationFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('school', css_class='col-md-8'),
                Div('major', css_class='col-md-4'),
                css_class='row'
            ),
            Div(
                Div('education', css_class='col-md-3'),
                Div('education_type', css_class='col-md-3'),
                Div('start_date', css_class='col-md-3'),
                Div('end_date', css_class='col-md-3'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden="true"
            )
        )
        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=EDUCATION_FORMS_PREFIX)


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'major', 'education', 'education_type', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_education'
        self.helper.layout = Layout(
            Div(
                Div('school', css_class='col-xs-5'),
                Div('major', css_class='col-xs-5'),
                Div('education', css_class='col-xs-5'),
                Div('education_type', css_class='col-xs-5'),
                Div('start_date', css_class='col-xs-5'),
                Div('end_date', css_class='col-xs-5'),
                css_class='form-group'
            ),
        )


class WorkExperienceFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(WorkExperienceFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('company_name', css_class='col-md-5'),
                Div('position', css_class='col-md-3'),
                Div('start_date', css_class='col-md-2'),
                Div('end_date', css_class='col-md-2'),
                css_class='row'
            ),
            Div(
                Div('resignation_reason', css_class='col-md-12'),
                css_class='row'
            ),
            Div(
                Div('description', css_class='col-md-12'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden="true"
            )
        )
        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=WORK_EXPERIENCE_FORMS_PREFIX)


class WorkExperienceForm(ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ['user']
        widgets = {
            'description': Textarea(attrs={'rows': 3})
        }

    def __init__(self, *args, **kwargs):
        super(WorkExperienceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_workexperience'
        self.helper.layout = Layout(
            Div(
                Div('company_name', css_class='col-xs-5'),
                Div('position', css_class='col-xs-5'),
                Div('description', css_class='col-xs-5'),
                Div('resignation_reason', css_class='col-xs-5'),
                Div('start_date', css_class='col-xs-5'),
                Div('end_date', css_class='col-xs-5'),
                css_class='form-group'
            ),
        )


class ProjectFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ProjectFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('name', css_class='col-md-8'),
                Div('start_date', css_class='col-md-2'),
                Div('end_date', css_class='col-md-2'),
                css_class='row'
            ),
            Div(
                Div('technology', css_class='col-md-12'),
                css_class='row'
            ),
            Div(
                Div('description', css_class='col-md-12'),
                css_class='row'
            ),
            Div(
                Div('responsibility', css_class='col-md-12'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden='true'
            )
        )
        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=PROJECT_FORMS_PREFIX)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['user']
        widgets = {
            'technology': Textarea(attrs={'rows': 3}),
            'description': Textarea(attrs={'rows': 3}),
            'responsibility': Textarea(attrs={'rows': 3}),
        }


class CertificationFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CertificationFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('name', css_class='col-md-6'),
                Div('remark', css_class='col-md-6'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden='true'
            )
        )
        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=CERTIFICATION_FORMS_PREFIX)


class CertificationForm(ModelForm):
    class Meta:
        model = Certification
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(CertificationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_certification'
        self.helper.layout = Layout(
            Div(
                Div('name', css_class='col-xs-5'),
                Div('remark', css_class='col-xs-5'),
                css_class='form-group'
            ),
        )


class SkillFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SkillFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('level', css_class='col-md-2'),
                Div('content', css_class='col-md-10'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden='true'
            )
        )
        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=SKILL_FORMS_PREFIX)


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_skill'
        self.helper.layout = Layout(
            Div(
                Div('level', css_class='col-xs-5'),
                Div('content', css_class='col-xs-5'),
                css_class='form-group'
            ),
        )


class TrainingExperienceFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TrainingExperienceFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('name', css_class='col-md-4'),
                Div('organization_name', css_class='col-md-4'),
                Div('start_date', css_class='col-md-2'),
                Div('end_date', css_class='col-md-2'),
                css_class='row'
            ),
            Div(
                Div('content', css_class='col-md-12'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden="true"
            )
        )
        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=TRAINING_EXPERIENCE_FORMS_PREFIX)


class TrainingExperienceForm(ModelForm):
    class Meta:
        model = TrainingExperience
        exclude = ['user']
        widgets = {
            'content': Textarea(attrs={'rows': '3'})
        }

    def __init__(self, *args, **kwargs):
        super(TrainingExperienceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_training'
        self.helper.layout = Layout(
            Div(
                Div('name', css_class='col-xs-5'),
                Div('organization_name', css_class='col-xs-5'),
                Div('start_date', css_class='col-xs-5'),
                Div('end_date', css_class='col-xs-5'),
                Div('content', css_class='col-xs-5'),
                css_class='form-group'
            ),
        )


class IdCardForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IdCardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('id_card_number', css_class='col-md-6'),
                Div('id_card_address', css_class='col-md-6'),
                css_class='row'
            ),
            Div(
                Div('residence_address', css_class='col-md-6'),
                Div('id_card_photo', css_class='col-md-6'),
                css_class='row'
            ),
        )

    class Meta:
        model = IdCard
        exclude = ['user']


class CardFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CardFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('number', css_class='col-md-6'),
                Div('bank_name', css_class='col-md-6'),
                css_class='row'
            ),
            Div(
                Div('branch_name', css_class='col-md-6'),
                Div('phone', css_class='col-md-6'),
                css_class='row'
            ),
            Div(Div('is_default', css_class='col-md-12'), css_class='row'),
            Div(Div('remark', css_class='col-md-12'), css_class='row'),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden="true"
            )
        )

        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=CARD_FORMS_PREFIX)


class CardForm(ModelForm):
    class Meta:
        model = Card
        exclude = ['user']
        widgets = {
            'remark': Textarea(attrs={'rows': '3'})
        }


class ContactFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ContactFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('name', css_class='col-md-3'),
                Div('relationship', css_class='col-md-3'),
                Div('organization', css_class='col-md-3'),
                Div('telephone', css_class='col-md-3'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden="true"
            )
        )

        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=CONTACT_FORMS_PREFIX)


class ContactForm(ModelForm):
    class Meta:
        model = ContactPerson
        exclude = ['user']


class WorkProjectFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(WorkProjectFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('name', css_class='col-md-8'),
                Div('start_time', css_class='col-md-2'),
                Div('end_time', css_class='col-md-2'),
                css_class='row'
            ),
            Div(
                Div('key_skill', css_class='col-md-12'),
                css_class='row'
            ),
            Div(
                Div('description', css_class='col-md-12'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden='true'
            )
        )
        self.all().wrap_together(Div, css_class=PROJROM_FORMS_PREFIX)


class WorkProjectForm(ModelForm):
    class Meta:
        model = WorkProject
        fields = ('name', 'description', 'key_skill', 'start_time', 'end_time')
        # widgets = {
        #     'key_skill': Textarea(attrs={'rows': 3}),
        #     'description': Textarea(attrs={'rows': 3}),
        # }


class SalaryFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SalaryFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('salary_level', css_class='col-md-4'),
                Div('salary_proportion', css_class='col-md-4'),
                Div('actual_salary', css_class='col-md-2'),
                css_class='row'
            ),
            Div(
                Div('gross_salary', css_class='col-md-2', function='jisuan'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden="true"
            )
        )
        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=SALARY_FORMS_PREFIX)


class SalaryForm(ModelForm):
    class Meta:
        model = Salary
        exclude = ['user']
        widgets = {
            'gross_salary': Textarea(attrs={'readonly': 'readonly', 'onblur': ''}),
        }


class DailyReportFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(DailyReportFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('header', css_class='col-md-4'),
                Div('create_time', css_class='col-md-4'),
                css_class='row'
            ),
            Div(
                Div('report_content', css_class='col-md-2'),
                Div('assess', css_class='col-md-4'),
                css_class='row'
            ),
            Div(
                Div('score', css_class='col-md-2'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden="true"
            )
        )
        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=DAILYREPORT_FORMS_PREFIX)


class DailyReportForm(ModelForm):
    class Meta:
        model = DailyReport
        fields = ('user', 'header', 'create_time', 'report_content', 'assess', 'score')
        widgets = {
            'report_content': RedactorWidget(editor_options={'lang': 'en','minHeight':300}),
            'assess': RedactorWidget(editor_options={'lang': 'en','minHeight':200})
        }


class RegularMeetingFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(RegularMeetingFormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False

        self.layout = Layout(
            Div(
                Div('title', css_class='col-md-4'),
                Div('specker', css_class='col-md-4'),
                Div('participant', css_class='col-md-2'),
                Div('meeting_time', css_class='col-md-4'),
                Div('enclosure', css_class='col-md-2'),
                css_class='row'
            ),
            Div(
                Div('main_content', css_class='col-md-2'),
                css_class='row'
            ),
            Button('button', '删除', css_class='btn btn-outline-danger btn-block btn-delete'),
            Div(
                Div('DELETE'),
                css_class='row',
                hidden="true"
            )
        )
        self.layout.extend(['user', 'id'])
        self.all().wrap_together(Div, css_class=REGULARMETTING_FORMS_PREFIX)


class RegularMeetingForm(ModelForm):
    class Meta:
        model = RegularMeeting
        exclude = ['user']
        widgets = {
            'main_content': RedactorWidget(editor_options={'lang': 'en'})
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('sname', 'age', 'sex', 'sdept')

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_student'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div('sname', css_class='col-xs-5'),
                Div('sdept', css_class='col-xs-5'),
                Div('age', css_class='col-xs-5'),
                Div('sex', css_class='col-xs-5'),
                css_class='form-group'
            ),
            Div(
                Div('age', css_class='col-xs-5'),
                Div('sex', css_class='col-xs-5'),
                css_class='form-group'
            ),
        )

