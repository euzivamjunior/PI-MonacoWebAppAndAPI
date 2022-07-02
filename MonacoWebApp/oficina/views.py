from django.shortcuts import render, redirect
from datetime import datetime
import requests
# from .models import Formulario
from automations.send_email import contact_form


def index(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        mensagem = request.POST['mensagem']

        data = {'nome': nome, 'telefone': telefone,
                'email': email, 'mensagem': mensagem}

        for i in request.POST:
            print(request.POST[str(i)])

        print('ENVIAR EMAIL')
        contact_form(data)

    return render(request, 'index.html')


def servico_alinhamento(request):
    return render(request, 'servico-alinhamento.html')


def servico_balanceamento(request):
    return render(request, 'servico-balanceamento.html')


def servico_cambagem(request):
    return render(request, 'servico-cambagem.html')


def servico_escapamento(request):
    return render(request, 'servico-escapamento.html')


def servico_motor(request):
    return render(request, 'servico-motor.html')


def servico_pneu(request):
    return render(request, 'servico-pneu.html')


def servico_suspencao(request):
    return render(request, 'servico-suspencao.html')


def servico_troca_oleo(request):
    return render(request, 'servico-troca-oleo.html')


def lista_modelos(request):
    return render(request, 'listaModelos.html')


def formulario(request):
    if request.method == 'POST':
        ano_veiculo = request.POST['ano']
        marca_veiculo = request.POST['marca']
        modelo_veiculo = request.POST['modelo']
        servicos = obtem_servicos(request)
        comentarios = request.POST['comentarios']
        date = datetime.strptime(request.POST['data'], '%Y-%m-%dT%H:%M')  # 2021-10-22T09:57
        tipo_contato = request.POST['tipoContato']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        email = request.POST['email']
        """
        print(request.POST['comentarios'])
        print(request.POST.get('pneus', False))
        """

        data = {
            "ano_veiculo": ano_veiculo,
            "marca_veiculo": marca_veiculo,
            "modelo_veiculo": modelo_veiculo,
            "servicos": servicos,
            "comentarios": comentarios,
            "data_do_agendamento": date,
            "tipo_contato": tipo_contato,
            "nome": nome,
            "sobrenome": sobrenome,
            "cpf": cpf,
            "telefone": telefone,
            "email": email
        }

        requests.post("https://monaco-web-api.herokuapp.com/formulario/", data=data)

        for item in request.POST:
            print(item)
        return redirect('index')
    else:
        return render(request, 'formulario.html')


def obtem_servicos(request):
    servicos_decode = {
        'alinhamento': 'Alinhamento',
        'balanceamento': 'Balanceamento',
        'cambagemCaster': 'Cambagem/Caster',
        'motor': 'Motor',
        'embreagem': 'Embreagem',
        'suspensao': 'Suspensao',
        'freio': 'Freio',
        'escapamento': 'Escapamento',
        'pneus': 'Pneus',
        'trocaOleo': 'Troca de óleo'
    }

    servicos_solicitados = []
    for service in servicos_decode.keys():
        if request.POST.get(service, False) is not False:
            servicos_solicitados.append(servicos_decode[service])

    servicos = '\n'.join(servicos_solicitados)
    # print(servicos)
    return servicos
