entDia, entData = input().split( )
entH, entM, entS = input().split(' : ')
saiDia, saiData = input().split( )
saiH, saiM, saiS = input().split(' : ')

# casting
entDia = str(entDia)
entData = int(entData)
saiDia = str(saiDia)
saiData = int(saiData)
entH = int(entH)
entM = int(entM)
entS = int(entS)
saiH = int(saiH)
saiM = int(saiM)
saiS = int(saiS)

if saiData >= entData and saiData + entData < 30: # se não ultrapassa 30 dias
    dia = saiData - entData
    if entH >= 0 and entH <= 24 and saiH >= 0 and saiH <= 24:
        if saiH >= entH: # Hora saida sendo maior dia e hora normais
            dia = dia # dia normal
            hora = saiH - entH
            print(f'{dia} dia(s)')
#            print('1ª linha Hora')
            if entM >= 0 and entM <= 60 and saiM >= 0 and saiM <= 60:
                if saiM >= entM: # minuto saida sendo maior
                    minuto = saiM - entM
#                    print('1ª linha Minuto')
                    print(f'{hora} hora(s)')
                    if entS >= 0 and entS <= 60 and saiS >= 0 and saiS <= 60:
                        if saiS >= entS:
                            segundo = saiS - entS
                            print(f'{minuto} minuto(s)')
                            print(f'{segundo} segundo(s)')
                        elif saiS < entS:
                            minuto = minuto - 60
                            segundo = 60 - entS + saiS
                            print(f'{minuto} minuto(s)')
                            print(f'{segundo} segundo(s)')
                    # else:
                    #     print('Digite um número até 60 segundos')
                elif saiM < entM: # minuto saida sendo menor
                    hora = hora - 24 # loop hora
                    minuto = 60 - entM + saiM # loop minuto
#                    print('2ª linha Minuto') # 
                    print(f'{hora} hora(s)')
                    if entM >= 0 and entM <= 60 and saiM >= 0 and saiM <= 60:
                        if saiS >= entS:
                            segundo = saiS - entS
                            print(f'{minuto} minuto(s)')
                            print(f'{segundo} segundo(s)')
                        elif saiS < entS:
                            minuto = minuto - 60
                            segundo = 60 - entS + saiS
                            print(f'{minuto} minuto(s)')
                            print(f'{segundo} segundo(s)')
            #         else:
            #             print('Digite um número até 60 segundos')
            # else:
            #     print('Digite um numero até 60 minutos')
        elif saiH < entH: # Hora saida sendo menor tem loop do dia
            dia = dia - 1 # loop do dia
            hora = 24 - entH + saiH # e loop hora 24 - entrada tipo 08 - 24 = 16 + 6 = 22
            print(f'{dia} dia(s)')
#            print(f'{hora} hora(s)')
#            print('2ª linha Hora')
            if entM >= 0 and entM <= 60 and saiM >= 0 and saiM <= 60:
                if saiM >= entM: # minuto saida sendo maior
                    minuto = saiM - entM
#                    print('1ª linha Minuto')
                    print(f'{hora} hora(s)')
#                    print(f'{minuto} minuto(s)')
                    if entS >= 0 and entS <= 60 and saiS >= 0 and saiS <= 60:
                        if saiS >= entS:
                            segundo = saiS - entS
                            print(f'{minuto} minuto(s)')
                            print(f'{segundo} segundo(s)')
                        elif saiS < entS:
                            minuto = minuto - 60
                            segundo = 60 - entS + saiS
                            print(f'{minuto} minuto(s)')
                            print(f'{segundo} segundo(s)')
                    # else:
                    #     print('Digite um número até 60 segundos')
                elif saiM < entM: # minuto saida sendo menor
                    hora = hora - 1 # loop hora
                    minuto = 60 - entM + saiM # loop minuto
#                    print('2ª linha Minuto') # 
                    print(f'{hora} hora(s)')
                    print(f'{minuto} minuto(s)')
                    if entS >= 0 and entS <= 60 and saiS >= 0 and saiS <= 60:
                        if saiS >= entS:
                            segundo = saiS - entS
                            print(f'{minuto} minuto(s)')
                            print(f'{segundo} segundo(s)')
                        elif saiS < entS:
                            minuto = minuto - 60
                            segundo = 60 - entS + saiS
                            print(f'{minuto} minuto(s)')
                            print(f'{segundo} segundo(s)')
#                     else:
#                         print('Digite um número até 60 segundos')
#             else:
#                 print('Digite um número até 60 minutos')
#     else:
#         print('Valor Hora ultrapassa 24h')
# else:
#     print('ultrapassa o mês')