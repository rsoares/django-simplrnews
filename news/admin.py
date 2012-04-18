# -*- coding: utf-8 -*-
# Ricardo Soares (ricardo@dengun.com) - Dengun 2012


from datetime import datetime, date
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Check if it has modeltranslation
HAS_MODELTRANSLATION = False
try:
    from modeltranslation.admin import TranslationAdmin
    HAS_MODELTRANSLATION = True
except:  # Need to handle proper exceptions ^!
    class TranslationAdmin(admin.ModelAdmin):
        pass

from news.models import NewsArticle, NewsPhoto, NewsSubscriber


class NewsFields(forms.ModelForm):
    title_en = forms.CharField(widget=forms.TextInput(attrs={'class':'modeltranslation', 'style':'width: 20em'}))
    title_pt = forms.CharField(widget=forms.TextInput(attrs={'class':'modeltranslation', 'style':'width: 20em'}))
    summary_en = forms.CharField(widget=forms.TextInput(attrs={'class':'modeltranslation', 'style':'width: 20em'}))
    summary_pt = forms.CharField(widget=forms.TextInput(attrs={'class':'modeltranslation', 'style':'width: 20em'}))
    content_en = forms.CharField(widget=forms.Textarea(attrs={'class':'modeltranslation', 'cols':'80'}))
    content_pt = forms.CharField(widget=forms.Textarea(attrs={'class':'modeltranslation', 'cols':'80'}))

    class Meta:
        model = NewsArticle


# Inlines
class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    fields = ('image', 'position')
    extra = 0


class NewsAdmin(TranslationAdmin):
    
    class Media:
        if HAS_MODELTRANSLATION:
            js = ("js/force_jquery.js",
                  "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js",
                  "js/tabbed_translation_fields.js",
                  "js/wymeditor/wymeditor/jquery.wymeditor.js",
                  "js/fancyeditor.js",
                 )
            css = {'screen': ("css/tabbed_translation_fields.css", "css/admin.css")}
        else:
            js = ("http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js",
                  "js/wymeditor/wymeditor/jquery.wymeditor.js",
                  "js/fancyeditor.js",
                 )
            css = {'screen': ("css/admin.css",)}

    fieldsets = ((None,
                 {'fields': ('title', 'url_slug', 'summary', 'content', ('published', 'on_homepage'), 'publication_date')}),
                 )
    
    # Set rewrited form if it has modeltranslation
    if HAS_MODELTRANSLATION:
        form = NewsFields
    
    inlines = (NewsPhotoInline,)
    list_display = ('title', 'published', 'publication_date', 'on_homepage')
    list_display_links = ('title',)
    list_filter = ('publication_date', 'published')
    search_fields = ['title', 'publication_date']
    readonly_fields = ('publication_date',)
    actions = ['publish', 'unpublish']
    prepopulated_fields = {"url_slug": ("title",)}
    
    def publish(self, request, queryset):
        to_publish = queryset.update(published=True, publication_date=datetime.now())
        if to_publish == 1:
            message_bit = u"1 article was"
        else: 
            message_bit = u"%s articles were" % to_publish
        self.message_user(request, u"%s successfully published." % message_bit)
    publish.short_description = u"Publish on website"
    
    def unpublish(self, request, queryset):
        to_unpublish = queryset.update(published=False, publication_date=None)
        if to_unpublish == 1:
            message_bit = u"1 article was"
        else: 
            message_bit = u"%s articles were" % to_unpublish
        self.message_user(request, u"%s successfully unpublished." % message_bit)
    unpublish.short_description = u"Unpublish from website"
    
    def save_model(self, request, obj, form, change):
        if obj.published:
            obj.publication_date = datetime.now()
        obj.save()


class NewsSubscriberAdmin(admin.ModelAdmin):
    fields = ('email', 'name')
    list_display = ('email', 'name', 'registration_date')
    list_display_links = ('email', 'name')
    list_filter = ('registration_date',)
    search_fields = ['name', 'email']
        

admin.site.register(NewsArticle, NewsAdmin)
admin.site.register(NewsSubscriber, NewsSubscriberAdmin)
