#Vamos criar os comandos para para o boot de transparencia
import pyautogui
import time

# Tempo para o usuário posicionar o mouse 

pyautogui.press("Win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("Enter")
time.sleep(2)

#Função para abrir a tela 
pyautogui.click(x=888, y=36)
time.sleep(2)

#Função para escrever o link
pyautogui.write("https://transparencia.pmspa.rj.gov.br/")
time.sleep(1)
pyautogui.press("Enter")
time.sleep(2)

#Clicar no icone de Ação covid-19
pyautogui.click(x=605, y=525)
time.sleep(2)

#Clicar no icones dentro covid-19
pyautogui.click(x=287, y=390)
time.sleep(1)
pyautogui.click(x=618, y=27)
time.sleep(2)

#Clicar no segundo icone dentro covid-19
pyautogui.click(x=648, y=370)
time.sleep(1)

#Vai abrir o pdf 
pyautogui.click(x=821, y=432)
time.sleep(3)

#Vai fechar o pdf
pyautogui.click(x=619, y=22)
time.sleep(1)

#Vai clicar na seta para voltar
pyautogui.click(x=191, y=268)
time.sleep(1)

#Vai abrir o terceiro icone dentro covid-19
pyautogui.click(x=944, y=388)
time.sleep(1)

pyautogui.click(x=198, y=283)
time.sleep(1)

#Clicar no inicio
pyautogui.click(x=167, y=150)
time.sleep(1)

#Clicar no icone de Licitações
pyautogui.click(x=932, y=891)
time.sleep(2)

#Abrir o primeiro icone de licitações
pyautogui.click(x=300, y=367)
time.sleep(2)
#Fechar a pagina
pyautogui.click(x=615, y=19)
time.sleep(1) 

#Clicar no terceiro icone de licitações
pyautogui.click(x=937, y=380)
time.sleep(2)
#fechar a pagina
pyautogui.click(x=619, y=23)
time.sleep(1)

#Vai clicar no quarto icone de licitações
pyautogui.click(x=1247, y=373)
time.sleep(2)
#Vai clicar no pdf
pyautogui.click(x=835, y=424)
time.sleep(1)
#Fechar o pdf
pyautogui.click(x=619, y=28)
time.sleep(1)

#Voltar ao inicio
pyautogui.click(x=165, y=151)
time.sleep(1)

#Vamos usar o scroll do mouse para baixo
pyautogui.scroll(-500)

#Vamos clicar no icone de educação
pyautogui.click(x=1606, y=884)
time.sleep(2)

#Vamos clicar no primeiro icone de educação
pyautogui.click(x=292, y=366)
time.sleep(2)

#vamos clicar na seta para voltar
pyautogui.click(x=194, y=265)
time.sleep(1)

#Vamos clicar no segundo icone de educação
pyautogui.click(x=628, y=381)
time.sleep(2)

#Vamos clicar no X para fechar
pyautogui.click(x=517, y=503)
time.sleep(1)

#Vamos imprimir relatorio
pyautogui.click(x=1577, y=386)
time.sleep(4)

#Vamos abrir o arquivo baixado
pyautogui.click(x=1786, y=138)
time.sleep(2)

#Vamos fechar a pagina
pyautogui.click(x=618, y=23)
time.sleep(1)

#Vamos voltar ao inicio
pyautogui.click(x=165, y=151)
