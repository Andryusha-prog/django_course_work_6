from lib2to3.fixes.fix_input import context
from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.forms import BaseModelForm, inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from email_sender.cron import send_func
from email_sender.forms import ClientFormCreate, ClientFormUpdate, MailingFormCreate, MailingFormUpdate, \
    MessageFormCreate, MessageFormUpdate, AttemptForm, ManagerMailingDetailForm
from email_sender.models import Client, Mailing, Message, Attempt
from email_sender.services import send_send


# Create your views here.

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientFormCreate
    success_url = reverse_lazy('sender:client_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        client = form.save()
        user = self.request.user
        client.user = user
        client.save()
        return super().form_valid(form)
    

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientFormUpdate
    
    def get_success_url(self):
        return reverse_lazy('sender:client_detail', kwargs={'pk': self.object.pk})

class ClientListView(ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('sender:client_list')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageFormCreate
    success_url = reverse_lazy('sender:message_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        message = form.save()
        user = self.request.user
        message.user = user
        message.save()
        return super().form_valid(form)

class MessageListView(ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageFormUpdate
    
    def get_success_url(self):
        return reverse_lazy('sender:message_detail', kwargs={'pk': self.object.pk})


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('sender:message_list')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingFormCreate
    success_url = reverse_lazy('sender:mailing_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        mailing = form.save()
        user = self.request.user
        mailing.user = user
        mailing.save()
        send_func('go_mail', mailing_pk=mailing.pk, message_pk=mailing.message.pk)
        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MailingFormset = inlineformset_factory(Mailing, Attempt, AttemptForm, extra=0)
        if self.request.method == 'POST':
            context_data['formset'] = MailingFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MailingFormset(instance=self.object)
        return context_data


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingFormUpdate

    
    def get_success_url(self):
        return reverse_lazy('sender:mailing_detail', kwargs={'pk': self.object.pk})


    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return MailingFormUpdate
        if user.has_perm('email_sender.cant_edit_mailing'):
            return ManagerMailingDetailForm



class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('sender:mailing_list')

class AttemptListView(ListView):
    model = Attempt