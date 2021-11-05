
#   ASSISTENTE VIRTUAL ALICE + PODE USAR VOZ MASCULINA AQUI É FEMININA

# ----------------------------------------------------------------------------------------------
# PYTTSX3 - É BÁSICAMENTE PARA A VOZ DA ASSISTENTE VIRTUAL
# SPEECH_RECOGNITION = É PARA O MICROFONE NO SEU CASO PARA FALA COM A ASSISTENTE
# WEBBROWSER = É PARA ABRIR NAVEGADOR E SITES
# OS = É BASICAMENTE PARA ABRIR O PLAYER DE MÚSICA E ARQUIVOS EM GERAL DENTRO DO SEU COMPUTADOR
# -----------------------------------------------------------------------------------------------
# TEM A FUNÇÃO BONÚS QUE É A BIBLIOTECA PARA FUNÇÃO O  DATETIME QUE SERVE PARA DIZER ANTES DA APRESENTAÇAO HORAS E DATA
# MAS AQUI VOU AMOSTRA SOMENTE O BÁSICO DAS FUNÇÕES EXISTENTE QUE JÁ FAZ BASTANTE COISA,
# NELE VOCÊ PODE USAR COM A PLACA ARDUINA E ADICIONAR FUNÇÕES DE LIGA A LAMPADA E ETC...
# UMA OBSERVAÇÃO USAR A VERSÃO DO PYTHON 3.6 POIS SÓ ELA FUNCIONA COM PYAUDIO ENTRE OUTRAS BIBLIOTECAS APESAR QUE O QUE USO AQUI TODAS AS FUNÇÕES VAI FUNCIONAR.
#-------------------------------------------------------------------------------------------------------------------------------------------------

import pyttsx3
import speech_recognition as sr  # OBS - baixe as bibliotecas mencionadas
import webbrowser as web
import os

nome = "senhor"
texto = "Olá " + str(nome) + "Meu nome é Alice, em que posso ajudar?" # AQUI VOCÊ PODE BOTAR A FUNÇÃO DATETIME, AONDE ELA DIZ AS HORAS E O DIA ATUAL

en = pyttsx3.init()
en.say(texto)
en.setProperty('voice', b'brasil') # voz, velocdade e volume da voz da assistente
en.setProperty('rate', 140)
en.setProperty('volume', 1)
en.runAndWait()

recon = sr.Recognizer()
with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt')   # parte do microfone
    recon.adjust_for_ambient_noise(source)

if resposta==("Google"):
    en.say('Ok, Abrindo o Google')
    en.setProperty('voice', b'brasil')   # É SÓ DIZER A PALAVRA  - GOOGLE E ELA ABRE A PAGINA GOOGLE
    en.setProperty('rate', 140)
    en.setProperty('volume', 1)
    en.runAndWait()
    web.open("https://www.google.com.br")

elif resposta==("YouTube"):
    en.say('Ok, Abrindo o YouTube')
    en.setProperty('voice',b'brasil')  # É SÓ DIZER A PALAVRA - YOUTUBE E ELA ABRE O YOUTUBE
    en.setProperty('rate', 140)
    en.setProperty('volume', 1)
    en.runAndWait()
    