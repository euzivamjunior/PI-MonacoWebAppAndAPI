from django.db import models
from django.dispatch import receiver
from automations.send_email import schedule_confirmation, finished_service


class Formulario(models.Model):
    ano_veiculo = models.CharField(max_length=200)
    marca_veiculo = models.CharField(max_length=200)
    modelo_veiculo = models.CharField(max_length=200)
    servicos = models.TextField(blank=True)
    comentarios = models.TextField(blank=True)
    data_do_agendamento = models.DateTimeField()
    tipo_contato = models.CharField(max_length=100)
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    confirmado = models.BooleanField(default=False)
    servico_realizado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self):
        return self.nome


@receiver(models.signals.pre_save, sender=Formulario)
def send_notification(sender, instance, **kwargs):  # despite pycharm warn, sender and **kwargs are required
    if instance.id is None:  # new object will be created
        pass
    else:
        old_instance = Formulario.objects.get(id=instance.id)
        if old_instance.confirmado is False and instance.confirmado is True:
            data = {'nome': instance.nome, 'email': instance.email}
            schedule_confirmation(data)
        elif old_instance.servico_realizado is False and instance.servico_realizado is True:
            data = {'nome': instance.nome, 'email': instance.email}
            finished_service(data)
            print('Finished service notifier')
