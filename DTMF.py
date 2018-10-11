#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
# Professor Rodrigo Carareto
# Projeto DTMF 
# Alessandra Blucher e Eric Otofuji
# Insper Instituto de Ensino e Pesquisa
# Engenharia de Computação
# São Paulo, 2018
####################################################

####################################################
# OBJETIVOS:

# Transmitir símbolos das teclas do telefone
# Receber símbolos das teclas do telefone
# Usuário deve teclar valor a ser transmitido ao rodar a transmissão
# Transmissão deve ser realizada em alguns segundos (parâmetro do código)
# Aplicação deve investigar o sinal pelos símbolos a cada 1 segundo
# Plotar gráfico do sinal recebido e dos harmônicos (Fourier)
# Print da tecla pressionada

####################################################
# AVALIAÇÃO:

# Sinal gerado com sucesso e reproduzido no alto-falante ao pressionar tecla.
# Gráfico de sinal emitido.
# Recepção e Fourier do sinal recebido com identificação dos picos.
# Gráfico do sinal recebido e gráfico dos harmônicos
# Identificação correta da tecla pressionada pelo usuário.

####################################################

#from SignalClass import * #class Signal
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import wave
import time
import pickle
import peakutils
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window


####################################################
#SignalClass

def generateSin(self, freq, amplitude, time, fs):
    n = time*fs
    x = np.linspace(0.0, time, n)
    s = amplitude*np.sin(freq*x*2*np.pi)
    return (x, s)

def calcFFT(self, signal, fs):
    N  = len(signal)
    W = window.hamming(N)
    T  = 1/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    yf = fft(signal*W)
    return(xf, np.abs(yf[0:N//2]))

def plotFFT(self, signal, fs):
    x,y = self.calcFFT(signal, fs)
    plt.figure()
    plt.plot(x, np.abs(y))
    plt.title('Fourier')
####################################################




def signalFrequency(tecla):

	####################################################
	# Define as frequências das teclas
	####################################################
	# Padrão DTMF Bell Labs (Hz)

	#1: 1209 & 697
	#2: 1336 & 697
	#3: 1477 & 697
	#4: 1209 & 770
	#5: 1336 & 770
	#6: 1477 & 770
	#7: 1209 & 852
	#8: 1336 & 852
	#9: 1477 & 852
	#*: 1209 & 941
	#0: 1336 & 941
	##: 1477 & 941

	####################################################
	

	return {

		"1": (generateSin(self,1209,21,1,44100) + generateSin(self,697,21,1,44100)),
		"2": (generateSin(self,1336,21,1,44100) + generateSin(self,697,21,1,44100)),
		"3": (generateSin(self,1477,21,1,44100) + generateSin(self,697,21,1,44100)),
		"4": (generateSin(self,1209,21,1,44100) + generateSin(self,770,21,1,44100)),
		"5": (generateSin(self,1336,21,1,44100) + generateSin(self,770,21,1,44100)),
		"6": (generateSin(self,1477,21,1,44100) + generateSin(self,770,21,1,44100)),
		"7": (generateSin(self,1209,21,1,44100) + generateSin(self,852,21,1,44100)),
		"8": (generateSin(self,1336,21,1,44100) + generateSin(self,852,21,1,44100)),
		"9": (generateSin(self,1477,21,1,44100) + generateSin(self,852,21,1,44100)),
		"0": (generateSin(self,1336,21,1,44100) + generateSin(self,941,21,1,44100)),
		"*": (generateSin(self,1209,21,1,44100) + generateSin(self,941,21,1,44100)),
		"#": (generateSin(self,1477,21,1,44100) + generateSin(self,941,21,1,44100))

	}.get(tecla, None)

signalFrequency(5)


















