from math import log10, ceil


class Calculus:
    def __init__(self, vector):
        self.vector = vector

        # ######### teste self.vector = [1.99, 2.18, 2.03, 1.78, 1.43, 1.43, 1.92, 2.19, 1.74, 1.56, 2.16, 1.69,
        # 2.22, 1.49, 1.44, 2.22, 1.46, 1.72, 2.01, 1.73, 1.70, 2.01, 1.66, 2.29, 1.76, 2.08, 1.48, 1.4, 1.95, 2.24]
        # self.vector = [84, 74, 59, 67, 65, 68, 71, 80, 41, 95, 33, 81, 41, 78, 66, 52, 91, 50, 56, 48, 47, 65, 53, 94,
        #                39, 73, 55, 65, 35, 69, 68, 57, 76, 45, 89, 61, 35, 85, 55, 98, 73, 85, 73, 64, 42, 77, 88, 60,
        #                74, 54]
        self.vector.sort()

        self.amplitudeTotal = round(max(self.vector) - min(self.vector), 2)
        self.numeroDeClasses = round(ceil(1 + 3.32 * log10(len(self.vector))), 2)
        self.intervaloDeClasses = round(self.amplitudeTotal / self.numeroDeClasses, 2)

        ########### NUMERO DE CLASSES ###################
        self.classes = []
        atuall = min(self.vector)
        for i in range(0, self.numeroDeClasses):
            proximo = atuall + self.intervaloDeClasses
            self.classes.append([round(atuall, 2), round(proximo, 2)])
            atuall = proximo

        ########## CENTRO DE CLASSES ####################
        self.centroDeClasses = []
        for c in self.classes:
            self.centroDeClasses.append(round(round(c[0] + c[1], 2) / 2, 2))

        # ######### FREQUENCIAS RELATIVAS ###################
        self.frequenciaRelativa = []
        self.count = 0
        for limites in self.classes:
            self.count = 0
            for x in self.vector:
                if limites[0] <= x < limites[1]:
                    self.count += 1
            self.frequenciaRelativa.append(self.count)

        ########### FREQUENCIAS ABSOLUTAS ###################
        self.frequenciaAbsoluta = [0]
        for i in range(0, self.numeroDeClasses):
            self.frequenciaAbsoluta.append(self.frequenciaRelativa[i] + self.frequenciaAbsoluta[i])
        self.frequenciaAbsoluta.remove(0)

        ########## FREQUENCIAS RELATIVAS PERCENTUAIS ################
        self.frequenciaRelativaPer = []
        for i in self.frequenciaRelativa:
            self.frequenciaRelativaPer.append(round(i / len(self.vector) * 100, 2))

        ########## FREQUENCIA ABSOLUTA PERCENTUAL #####################
        self.frequenciaAbsolutaPer = []
        for i in self.frequenciaAbsoluta:
            self.frequenciaAbsolutaPer.append(round(i / len(self.vector) * 100, 2))

        ##############  MEDIDAS DE TENDENCIA ############################
        self.media = round(
            sum([self.centroDeClasses[i] * self.frequenciaRelativa[i] for i in range(0, self.numeroDeClasses)]) / len(
                self.vector), 2)

        try:
            self.medianaI = round(self.numeroDeClasses / 2 - 1)
            self.mediana = round(self.classes[self.medianaI][0] + self.intervaloDeClasses * (
                    (len(self.vector) / 2) - self.frequenciaAbsoluta[self.medianaI - 1]) / self.frequenciaRelativa[
                                     self.medianaI], 2)
        except:
            self.mediana = None

        ######
        # self.modaI = self.frequenciaRelativa.index(max(self.frequenciaRelativa))
        # self.moda = self.classes[self.modaI][0] + (self.frequenciaRelativa[self.modaI])

    def get_at(self):
        return self.amplitudeTotal

    def get_k(self):
        return self.numeroDeClasses

    def get_ac(self):
        return self.intervaloDeClasses

    def get_classes(self):
        return self.classes

    def get_ci(self):
        return self.centroDeClasses

    def get_fi(self):
        if sum(self.frequenciaRelativa) == len(self.vector):
            return self.frequenciaRelativa

    def get_fa(self):
        return self.frequenciaAbsoluta

    def get_fi_per(self):
        return self.frequenciaRelativaPer

    def get_fa_per(self):
        return self.frequenciaAbsolutaPer

    def get_media(self):
        return self.media

    def get_mediana(self):
        return self.mediana

    def get_moda(self):
        pass
