
class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str) -> None:
        self.datos = open(nombre_archivo , "r")
    def procesar_datos(self):
        for dato in self.datos:
            partidos = dato.split()
            if partidos[0].lower() == "temperatura:":
                promedio_temp = 0
                promedio_temp += float(partidos[1])
            elif partidos[0].lower() == "humedad:":
                promedio_hu = 0
                promedio_hu += float(partidos[1])
            elif partidos[0].lower() == "presion:":
                promedio_pre = 0
                promedio_pre += float(partidos[1])
            elif partidos[0].lower() == "viento:":
                promedio_vi = 0
                for letra in partidos[1]:
                    if "N" in partidos[1]:
                        partidos[1].replace("N","")
                    elif "S" in partidos[1]:
                        partidos[1].replace("S","")
                    elif "W" in partidos[1]:
                        partidos[1].replace("W","")
                    elif "E" in partidos[1]:
                        partidos[1].replace("E","")
                    else:
                        viento = float(partidos[1])
                promedio_vi += viento
        n += 1
        temperatura = promedio_temp/n
        humedad = promedio_hu/n
        presion = promedio_pre/n
        viento = promedio_vi/n
        if viento >= 0 and viento< 45:
            print("El promedio de la temperatura es:", temperatura,"de la humedad es:", "de la presion es:","del viento es", viento, "en direccion N")
        elif viento >= 45 and viento< 90:
            print("El promedio de la temperatura es:", temperatura,"de la humedad es:", "de la presion es:","del viento es", viento, "en direccion NE")
        elif viento >= 90 and viento< 135:
            print("El promedio de la temperatura es:", temperatura,"de la humedad es:", "de la presion es:","del viento es", viento, "en direccion E")
        elif viento >= 135 and viento< 180:
            print("El promedio de la temperatura es:", temperatura,"de la humedad es:", "de la presion es:","del viento es", viento, "en direccion SE")
        elif viento >= 180 and viento< 225:
            print("El promedio de la temperatura es:", temperatura,"de la humedad es:", "de la presion es:","del viento es", viento, "en direccion S")
        elif viento >= 225 and viento< 270:
            print("El promedio de la temperatura es:", temperatura,"de la humedad es:", "de la presion es:","del viento es", viento, "en direccion SW")
        elif viento >= 270 and viento< 315:
            print("El promedio de la temperatura es:", temperatura,"de la humedad es:", "de la presion es:","del viento es", viento, "en direccion W")
        elif viento >= 315 and viento< 360:
            print("El promedio de la temperatura es:", temperatura,"de la humedad es:", "de la presion es:","del viento es", viento, "en direccion NW")
        else:
            print("El promedio de la temperatura es:", temperatura,"de la humedad es:", "de la presion es:","del viento es", viento, "en direccion N")
