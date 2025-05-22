import math
import matplotlib.pyplot as plt

class MassaEspecifica:
    def calcular(self):
        op = int(input("""--Calculando Massa Específica--
Selecione a opção desejada:
1- Calcular densidade
2- Calcular massa
3- Calcular volume
"""))
        if op == 1:
            self.m = float(input("Digite a massa (kg): "))
            self.v = float(input("Digite o volume (m³): "))
            self.d = self.m / self.v
            print(f"Densidade = {self.d:.2f} kg/m³")

        elif op == 2:
            self.d = float(input("Digite a densidade (kg/m³): "))
            self.v = float(input("Digite o volume (m³): "))
            self.m = self.d * self.v
            print(f"Massa = {self.m:.2f} kg")

        elif op == 3:
            self.d = float(input("Digite a densidade (kg/m³): "))
            self.m = float(input("Digite a massa (kg): "))
            self.v = self.m / self.d
            print(f"Volume = {self.v:.4f} m³")
            
    def grafico(self):
        #Densidade x Volume
        plt.scatter([self.v], [self.d], color='red')
        plt.xlabel('Volume (m³)')
        plt.ylabel('Densidade (kg/m³)')
        plt.title('Densidade calculada')
        plt.grid(True)
        plt.show()

class Pressao:
    def calcular(self):
        op = int(input("""--Calculando Pressao--
Selecione a opção desejada:
1- Calcular pressão
2- Calcular força
3- Calcular área
"""))
        if op == 1:
            self.f = float(input("Digite a força (N)"))
            self.a = float(input("Digite a área (m²)"))
            self.p = self.f/self.a
            print(f"Pressão = {self.p:.2f}(Pa)")

        elif op == 2:
            self.p = float(input("Digite a pressão (Pa): "))
            self.a = float(input("Digite a área (m²)"))
            self.f = self.p * self.a
            print(f"Força = {self.f:.2f}(N)")

        elif op == 3:
            self.p = float(input("Digite a pressão (Pa): "))
            self.f = float(input("Digite a força (N)"))
            self.a = self.f/self.p
            print(f"Área = {self.a:.2f}(m²)")

    def grafico(self):
        #Pressão vs Área
        plt.scatter([self.a], [self.p], color='orange')
        plt.xlabel('Área (m²)')
        plt.ylabel('Pressão (Pa)')
        plt.title('Pressão')
        plt.grid(True)
        plt.show()
    
class PressaoHidrostatica:
    def calcular(self):
        print("-- Calculando Pressão Hidrostática --")

        op = int(input("""Selecione a opção desejada:
1 - Calcular pressão (P)
2 - Calcular densidade do fluido (p)
3 - Calcular profundidade (h)
4 - Calcular gravidade (g)
"""))

        if op == 1:
            self.d = float(input("Digite a densidade do fluido (kg/m³): "))
            self.g = float(input("Digite a gravidade (m/s²): "))
            self.h = float(input("Digite a profundidade (m): "))
            self.p = self.d * self.g * self.h
            print(f"Pressão = {self.p:.2f} Pa")

        elif op == 2:
            self.p = float(input("Digite a pressão (Pa): "))
            self.g = float(input("Digite a gravidade (m/s²): "))
            self.h = float(input("Digite a profundidade (m): "))
            self.d = self.p / (self.g * self.h)
            print(f"Densidade = {self.d:.2f} kg/m³")

        elif op == 3:
            self.p = float(input("Digite a pressão (Pa): "))
            self.d = float(input("Digite a densidade do fluido (kg/m³): "))
            self.g = float(input("Digite a gravidade (m/s²): "))
            self.h = self.p / (self.d * self.g)
            print(f"Profundidade = {self.h:.2f} m")

        elif op == 4:
            self.p = float(input("Digite a pressão (Pa): "))
            self.d = float(input("Digite a densidade do fluido (kg/m³): "))
            self.h = float(input("Digite a profundidade (m): "))
            self.g = self.p / (self.d * self.h)
            print(f"Gravidade = {self.g:.2f} m/s²")

        else:
            print("Opção inválida.")
            
    def grafico(self):
        #Pressão x Profundidade
        plt.scatter([self.h], [self.p], color='green')
        plt.xlabel('Profundidade (m)')
        plt.ylabel('Pressão (Pa)')
        plt.title('Pressão Hidrostática')
        plt.grid(True)
        plt.show()

class EsvaziamentoReservatorio:
    def __init__(self):
        #Listas p/ armazenar valores
        self.tempos = []
        self.alturas = []
        
    def calcular(self):
        g = 9.81  # gravidade (m/s²)
        
        h0 = float(input("Altura inicial do fluido no reservatório (m): "))
        A_base = float(input("Área da base do reservatório (m²): "))
        
        diametro = float(input("Diâmetro do orifício de saída (m): "))
        A_orificio = math.pi * (diametro / 2) ** 2
        
        delta_t = float(input("Intervalo de tempo entre os cálculos (s): "))
        
        # Inicialização
        h = h0
        V_total = A_base * h0
        tempo = 0
        
        self.tempos = []
        self.alturas = []

        while h > 0:
            v = math.sqrt(2 * g * h) #Velocidade de saída do fluido
            Q = A_orificio * v #Vazão
            V_saida = Q * delta_t #Volume escoado
            V_total -= V_saida #Volume restante
        
            if V_total < 0:
                V_total = 0
        
            h = V_total / A_base #Altura atual
            tempo += delta_t #Tempo de acordo com o intervalo definido
            
            #Jogando valores na lista para usar no grafico 
            self.tempos.append(tempo)
            self.alturas.append(h)
        
        # Resultado final
        print(f"\nTempo total para esvaziar o reservatório: {tempo:.2f} s")
        
    
    def grafico(self):
        #Altura do Fluido x Tempo
        plt.plot(self.tempos, self.alturas, color='blue') #Dados
        plt.xlabel('Tempo (s)') #Texto X
        plt.ylabel('Altura do fluido (m)') #Texto Y
        plt.title('Esvaziamento do Reservatório (Experimento de Torricelli)') #Titulo do Grafico
        plt.grid(True) #Linhas
        plt.show() #Mostrar

class MenuPrincipal:
    def exibir(self):
        while True:
            print("\n=== Mecanica de Fluidos ===")
            opcao = int(input("""Escolha uma opção:
1 - Calcular Massa Específica
2 - Calcular Pressão
3 - Calcular Pressão Hidrostática
4- Calcular Esvaziamento de Reservatório
5- Sair
"""))

            if opcao == 1:
                massa = MassaEspecifica()
                massa.calcular()
                massa.grafico()
                
            elif opcao == 2:
                pressao = Pressao()
                pressao.calcular()
                pressao.grafico()
                
            elif opcao == 3:
                pressaoh = PressaoHidrostatica()
                pressaoh.calcular()
                pressaoh.grafico()
                
            elif opcao == 4:
                esvaziamento= EsvaziamentoReservatorio()
                esvaziamento.calcular()
                esvaziamento.grafico()

            elif opcao == 5:
                print("Encerrando o programa.")
                break   
            else:
                print("Opção inválida. Tente novamente.")

menu = MenuPrincipal()
menu.exibir()
