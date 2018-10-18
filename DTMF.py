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

# Transmitir símbolos das keys do telefone.
# Receber símbolos das keys do telefone.
# Usuário deve keyr valor a ser transmitido ao rodar a transmissão.
# Transmissão deve ser realizada em alguns segundos (parâmetro do código).
# Aplicação deve investigar o sinal pelos símbolos a cada 1 segundo.
# Plotar gráfico do sinal recebido e dos harmônicos (Fourier).
# Print da key pressionada.

####################################################
# AVALIAÇÃO:

# Sinal gerado com sucesso e reproduzido no alto-falante ao pressionar key.
# Gráfico de sinal emitido.
# Recepção e Fourier do sinal recebido com identificação dos picos.
# Gráfico do sinal recebido e gráfico dos harmônicos.
# Identificação correta da key pressionada pelo usuário.

####################################################

#from SignalClass import * #class Signal
import numpy as np
import sounddevice as sd
sd.default.samplerate = 44100
sd.default.channels = 2
import matplotlib.pyplot as plt
import wave
import time
import pickle
import keyboard
import peakutils
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window


####################################################
#SignalClass
def generateSin(freq, amplitude, time, fs):
    n = time*fs
    x = np.linspace(0.0, time, n)
    s = amplitude*np.sin(freq*x*2*np.pi)
    return (x, s)
def calcFFT(signal, fs):
    N  = len(signal)
    W = window.hamming(N)
    T  = 1/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    yf = fft(signal*W)
    return(xf, np.abs(yf[0:N//2]))
def plotFFT(signal, fs):
    x,y = self.calcFFT(signal, fs)
    plt.figure()
    plt.plot(x, np.abs(y))
    plt.title('Fourier')
####################################################




def signalFrequency(key):

	####################################################
	# Define as frequências das keys
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
	
	

	try:
		return {

			"1": (generateSin(1209,21,1,44100) + generateSin(697,21,1,44100)),
			"2": (generateSin(1336,21,1,44100) + generateSin(697,21,1,44100)),
			"3": (generateSin(1477,21,1,44100) + generateSin(697,21,1,44100)),
			"4": (generateSin(1209,21,1,44100) + generateSin(770,21,1,44100)),
			"5": (generateSin(1336,21,1,44100) + generateSin(770,21,1,44100)),
			"6": (generateSin(1477,21,1,44100) + generateSin(770,21,1,44100)),
			"7": (generateSin(1209,21,1,44100) + generateSin(852,21,1,44100)),
			"8": (generateSin(1336,21,1,44100) + generateSin(852,21,1,44100)),
			"9": (generateSin(1477,21,1,44100) + generateSin(852,21,1,44100)),
			"0": (generateSin(1336,21,1,44100) + generateSin(941,21,1,44100)),
			"*": (generateSin(1209,21,1,44100) + generateSin(941,21,1,44100)),
			"#": (generateSin(1477,21,1,44100) + generateSin(941,21,1,44100)),

		}.get(key, None);
	
	except:
		pass


def play(key):
	try:
		sd.play((signalFrequency(key)[1] + signalFrequency(key)[3]), 44100); sd.wait();
	
	except:
		pass


def testSignalSound():
	try:
		sd.play(signalFrequency(str(1))[1] + signalFrequency(str(1))[3], 44100); sd.wait();
		sd.play(signalFrequency(str(2))[1] + signalFrequency(str(2))[3], 44100); sd.wait();
		sd.play(signalFrequency(str(3))[1] + signalFrequency(str(3))[3], 44100); sd.wait();
		sd.play(signalFrequency(str(4))[1] + signalFrequency(str(4))[3], 44100); sd.wait();
		sd.play(signalFrequency(str(5))[1] + signalFrequency(str(5))[3], 44100); sd.wait();
		sd.play(signalFrequency(str(6))[1] + signalFrequency(str(6))[3], 44100); sd.wait();
		sd.play(signalFrequency(str(7))[1] + signalFrequency(str(7))[3], 44100); sd.wait();
		sd.play(signalFrequency(str(8))[1] + signalFrequency(str(8))[3], 44100); sd.wait();
		sd.play(signalFrequency(str(9))[1] + signalFrequency(str(9))[3], 44100); sd.wait();
		sd.play(signalFrequency(str(0))[1] + signalFrequency(str(0))[3], 44100); sd.wait();
		sd.play(signalFrequency(   "*")[1] + signalFrequency(   "*")[3], 44100); sd.wait();
		sd.play(signalFrequency(   "#")[1] + signalFrequency(   "#")[3], 44100); sd.wait();
	
	except:
		pass

#testSignalSound();



def getKey():
	try:
		key = str(input()); sf = signalFrequency(key);
		return(key)
	
	except:
		pass

#getKey();


def plotGeneratedSignal(key):
	plt.plot(signalFrequency(key)[1][0:1000] + signalFrequency(key)[3][0:1000]); plt.show();

#play(str(3));
#plotGeneratedSignal(str(0));

####################################################
### UNDER CONSTRUCTION ###
####################################################
 def getSignal():

	abacate = sd.rec();
	return abacate


abacate = sd.rec(4410000);
print(abacate);
plt.plot(abacate.T[1]); plt.show();
sd.play(abacate, 44100);
####################################################
### UNDER CONSTRUCTION ###
####################################################

def plotReceivedSignal():
	####################################################
	# OBJETIVOS:

	# Plotar gráfico do sinal recebido e dos harmônicos (Fourier)
	# Print da key pressionada

	####################################################
	# AVALIAÇÃO:

	# Gráfico do sinal recebido e gráfico dos harmônicos

	####################################################
	pass

def discoverReceivedSignal():
	####################################################
	# OBJETIVOS:

	# Print da key pressionada

	####################################################
	# AVALIAÇÃO:

	# Identificação correta da key pressionada pelo usuário.

	####################################################
	pass
	

def mainGenerate():
	try:
		key = getKey();
		play(key);
		plotGeneratedSignal(key);
	
	except:
		pass

mainGenerate()

def mainReceive():
	try:
		listened = getSignal();
		key = discoverReceivedSignal(listened);
		print(key);
		plotReceivedSignal(listened);
	
	except:
		pass

#mainReceive()



