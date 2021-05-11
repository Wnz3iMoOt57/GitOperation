from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from employees.forms import DailyReportForm, RegularMeetingForm
from employees.models import Resume, Education, WorkExperience, Project, Certification, Skill, Interview, Activity, \
    Employee, IdCard, Card, ContactPerson, Comment, TrainingExperience, InterviewResume, WorkProject, Salary,\
    DailyReport, RegularMeeting, Student


def get_full_name(self):
    return '%s%s' % (self.last_name, self.first_name)


User.__str__ = get_full_name


class ActivityAdminForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['user', 'content']


class ActivityAdmin(ModelAdmin):
    list_display = ['user', 'activity_date', 'content', 'update_time']
    list_display_links = list_display
    list_filter = ['user']
    ordering = ['-activity_date']

    fields = ['user', 'activity_date', 'content']
    form = ActivityAdminForm
    autocomplete_fields = ['user']

    def save_model(self, request, obj, form, change):
        obj.updater = request.user
        if not change:
            obj.creator = request.user
        super().save_model(request, obj, form, change)


class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', )


class MyUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined']
    # list_display_links = list_display
    ordering = ['-date_joined']

    add_form = MyUserCreationForm
    prepopulated_fields = {'username': ('first_name', 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', ),
        }),
    )


class InterviewResumeAdmin(ModelAdmin):
    list_display = ['user', 'telephone', 'email', 'view_resume']
    list_display_links = None
    list_filter = ['user']

    def view_resume(self, obj):
        return format_html('<a href="{}" target="_blank">查看简历</a>', reverse('interview_resume', args=(obj.user.pk,)))

    view_resume.allow_tags = True
    view_resume.short_description = '查看简历'


class InterviewDoneFilter(SimpleListFilter):
    title = '是否已经面试'
    parameter_name = 'done'

    def lookups(self, request, model_admin):
        return ('true', '已面试'), ('false', '未面试')

    def queryset(self, request, queryset):
        if self.value() == 'true':
            return queryset.filter(time__lt=timezone.now())
        if self.value() == 'false':
            return queryset.filter(time__gt=timezone.now())


class InterviewAdmin(ModelAdmin):
    list_display = ['user', 'time', 'interviewer', 'result', 'view_resume']
    list_display_links = ['user', 'time', 'interviewer', 'result']
    ordering = ['-time']
    list_filter = ['user', InterviewDoneFilter]

    autocomplete_fields = ['user']
    change_form_template = 'admin/change_form_more_time.html'

    def view_resume(self, obj):
        return format_html('<a type="button" class="btn btn-primary" href="{}" target="_blank">查看简历</a>', reverse('interview_resume', args=(obj.user.pk,)))

    view_resume.allow_tags = True
    view_resume.short_description = '查看简历'


class EmployeeAdmin(ModelAdmin):
    list_display = ['user', 'number', 'type', 'status', 'enter_date', 'qualify_date', 'leave_date', 'view_info']
    list_display_links = list_display

    autocomplete_fields = ['user']
    ordering = ['-enter_date']
    list_filter = ['type', 'status']

    def view_info(self, obj):
        return format_html('<a type="button" class="btn btn-primary" href="{}" target="_blank">查看资料</a>', reverse('interview_resume', args=(obj.user.pk,)))

    view_info.allow_tags = True
    view_info.short_description = '查看资料'


class WorkProjectAdmin(ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')
    list_display_links = list_display


class SalaryAdmin(ModelAdmin):
    list_display = ('user', 'salary_level', 'salary_proportion','gross_salary','actual_salary')
    list_display_links = list_display


class DailyReportAdmin(ModelAdmin):
    form = DailyReportForm
    exclude = None
    list_display = ('user', 'header', 'create_time')
    list_display_links = list_display
    autocomplete_fields = ['user']
    # fieldsets = (
    #     ['Basic', {
    #         'fields': ('user', 'header', 'create_time',),
    #     }],
    #     ['Cotent', {
    #         'classes': ('full-width',),  # CSS
    #         'fields': ('report_content', 'assess',),
    #     }],
    #     [None, {
    #         'fields': ('score',),
    #     }],
    # )


class RegularMeetingAdmin(ModelAdmin):
    form = RegularMeetingForm
    exclude = None
    list_display = ('specker', 'title', 'meeting_time')
    list_display_links = list_display
    autocomplete_fields = ['specker']
    # fieldsets = (
    #     [None, {
    #         'fields': ('title', 'specker', 'participant', 'meeting_time',),
    #     }],
    #     [None, {
    #         'classes': ('full-width',),  # CSS
    #         'fields': ('main_content',),
    #     }],
    #     [None, {
    #         'fields': ('enclosure',),
    #     }],
    # )


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Resume)
admin.site.register(InterviewResume, InterviewResumeAdmin)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Skill)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(IdCard)
admin.site.register(Card)
admin.site.register(ContactPerson)
admin.site.register(Comment)
admin.site.register(TrainingExperience)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(WorkProject, WorkProjectAdmin)
admin.site.register(DailyReport, DailyReportAdmin)
admin.site.register(RegularMeeting, RegularMeetingAdmin)