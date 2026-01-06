
from django.contrib import admin
from django.utils.html import format_html
from jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'company_name',
        'employer_link',
        'location',
        'job_type',
        'is_active_badge',
        'total_applications',
        'posted_date',
    )

    list_filter = (
        'job_type',
        'is_active',
        'posted_date',
        'location',
    )

    search_fields = (
        'title',
        'company_name',
        'location',
        'description',
        'employer__username',
        'employer__email',
    )

    ordering = ('-posted_date',)

    readonly_fields = (
        'posted_date',
        'updated_date',
        'get_total_applications',
    )

    fieldsets = (
        ('Job Information', {
            'fields': ('title', 'company_name', 'employer', 'location', 'job_type')
        }),
        ('Job Details', {
            'fields': ('salary', 'description', 'requirements')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('posted_date', 'updated_date', 'get_total_applications'),
            'classes': ('collapse',),
        }),
    )

    def employer_link(self, obj):
        if obj.employer:
            url = f'/admin/accounts/user/{obj.employer.id}/change/'
            return format_html('<a href="{}">{}</a>', url, obj.employer.username)
        return '-'
    employer_link.short_description = 'Employer'

    def is_active_badge(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="background:#28a745;color:white;padding:3px 10px;border-radius:3px;">{}</span>',
                'Active'
            )
        return format_html(
            '<span style="background:#dc3545;color:white;padding:3px 10px;border-radius:3px;">{}</span>',
            'Inactive'
        )
    is_active_badge.short_description = 'Status'

    def total_applications(self, obj):
        return obj.applications.count()
    total_applications.short_description = 'Applications'

    def get_total_applications(self, obj):
        return obj.applications.count()
    get_total_applications.short_description = 'Total Applications'

    actions = ('activate_jobs', 'deactivate_jobs')

    def activate_jobs(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} job(s) activated.')
    activate_jobs.short_description = 'Activate selected jobs'

    def deactivate_jobs(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} job(s) deactivated.')
    deactivate_jobs.short_description = 'Deactivate selected jobs'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'employer':
            from accounts.models import User
            kwargs['queryset'] = User.objects.filter(role='employer')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
