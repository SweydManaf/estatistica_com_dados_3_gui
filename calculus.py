from math import log10, ceil


class Calculus:
    def __init__(self, vector):
        self.vector = vector
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
            if self.numeroDeClasses % 2 == 0:
                self.medianaI = round(self.numeroDeClasses / 2 - 1)
            else:
                self.medianaI = ceil(self.numeroDeClasses / 2 - 1)
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
