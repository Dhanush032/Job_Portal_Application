from django.contrib import admin
from django.utils.html import format_html
from applications.models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'applicant_link',
        'job_link',
        'company_name',
        'status_badge',
        'applied_date',
        'view_resume'
    ]
    
    list_filter = [
        'status',
        'applied_date',
        'job__job_type',
        'job__company_name'
    ]
    
    search_fields = [
        'applicant__username',
        'applicant__email',
        'applicant__first_name',
        'applicant__last_name',
        'job__title',
        'job__company_name'
    ]
    
    ordering = ['-applied_date']
    
    readonly_fields = ['applied_date', 'applicant_details', 'job_details']
    
    fieldsets = (
        ('Application Info', {
            'fields': ('job', 'applicant', 'status')
        }),
        ('Application Details', {
            'fields': ('resume', 'cover_letter')
        }),
        ('Additional Info', {
            'fields': ('applicant_details', 'job_details', 'applied_date'),
            'classes': ('collapse',)
        }),
    )
    
    def applicant_link(self, obj):
        return format_html(
            '<a href="/admin/accounts/user/{}/change/">{}</a>',
            obj.applicant.id,
            obj.applicant.get_full_name() or obj.applicant.username
        )
    applicant_link.short_description = 'Applicant'
    
    def job_link(self, obj):
        return format_html(
            '<a href="/admin/jobs/job/{}/change/">{}</a>',
            obj.job.id,
            obj.job.title
        )
    job_link.short_description = 'Job Title'
    
    def company_name(self, obj):
        return obj.job.company_name
    company_name.short_description = 'Company'
    
    def status_badge(self, obj):
        colors = {
            'pending': '#FFC107',
            'accepted': '#28a745',
            'rejected': '#dc3545'
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px; text-transform: capitalize;">{}</span>',
            colors.get(obj.status, '#6c757d'),
            obj.status
        )
    status_badge.short_description = 'Status'
    
    def view_resume(self, obj):
        if obj.resume:
            return format_html(
                '<a href="{}" target="_blank" style="color: #007bff;">View Resume</a>',
                obj.resume.url
            )
        return "No Resume"
    view_resume.short_description = 'Resume'
    
    def applicant_details(self, obj):
        return format_html(
            '<strong>Email:</strong> {}<br>'
            '<strong>Phone:</strong> {}<br>'
            '<strong>Skills:</strong> {}<br>'
            '<strong>Experience:</strong> {} years',
            obj.applicant.email,
            obj.applicant.phone or 'N/A',
            obj.applicant.skills or 'N/A',
            obj.applicant.experience_years or 'N/A'
        )
    applicant_details.short_description = 'Applicant Details'
    
    def job_details(self, obj):
        return format_html(
            '<strong>Location:</strong> {}<br>'
            '<strong>Type:</strong> {}<br>'
            '<strong>Salary:</strong> {}<br>'
            '<strong>Employer:</strong> {}',
            obj.job.location,
            obj.job.get_job_type_display(),
            obj.job.salary,
            obj.job.employer.username
        )
    job_details.short_description = 'Job Details'
    
    actions = ['accept_applications', 'reject_applications', 'reset_to_pending']
    
    def accept_applications(self, request, queryset):
        
        updated = queryset.update(status='accepted')
        self.message_user(request, f'{updated} application(s) accepted.')
    accept_applications.short_description = "Accept selected applications"
    
    def reject_applications(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f'{updated} application(s) rejected.')
    reject_applications.short_description = "Reject selected applications"
    
    def reset_to_pending(self, request, queryset):
        updated = queryset.update(status='pending')
        self.message_user(request, f'{updated} application(s) reset to pending.')
    reset_to_pending.short_description = "Reset to pending"
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "applicant":
            kwargs["queryset"] = db_field.related_model.objects.filter(role='job_seeker')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)  
        }