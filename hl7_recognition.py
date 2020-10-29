import matplotlib.pyplot as plt

def set_data(file_name):
    messages = open(file_name,"r")

    line = messages.read().replace("\n\n", "\nNEW_MESSAGE\n")
    line.replace("\n","")

    #lista de 2 elementos, um com cada mensagem
    message_list = line.split("\nNEW_MESSAGE\n")
    new_list =[] 
    final_list = [] 

    for i in range(len(message_list)):
        new_list.append(message_list[i].split("|")) 

    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            if(new_list[i][j] != ""):
                if ("\n" in new_list[i][j][0]):
                    new_list[i][j] = new_list[i][j][1:]
                
                final_list.append(new_list[i][j])

    #print(final_list)
    return final_list


def validate_message(message):

    if message[7] == 'ORU^R01' :
        # segmentos obrigatorios MSH OBR
        if "MSH" and "OBX" in message:
            i1 = message.index("MSH")
            i2 = message.index("OBX")
            
            if (i1< i2):
                print("Message ORU_R01 validated")
            
    
    elif message[7] == 'ADT^A01' :
        # segmentos obrigatorios MSH EVN PID PV1
        if "MSH" and "EVN" and "PID" and "PV1" in message:
            i1 = message.index("MSH")
            i2 = message.index("EVN")
            i3 = message.index("PID")
            i4 = message.index("PV1")
            if i1<i2 and i2<i3 and i3<i4:
                print("Message ADT_A01 validated")



def print_message_adt(adt):
    print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
    print("******************************* Servico Hospitalar CHUC ********************************")
    print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
    print("Data da mensagem: " + adt[6][0:4]+"/"+adt[4][4:6]+"/"+adt[6][6:8])
    print("Hora da mensagem: " + adt[6][8:10]+":"+adt[6][10:12])
    print("Tipo da mensagem: " + adt[7].replace("^", "_") + "\n\n\t\tDados do paciente")
    print("Id de controlo: " + adt[8])
    print("Data do registo: " + adt[13][0:4]+ "/"+adt[13][4:6]+ "/" + adt[13][6:8])
    print("Hora do registo: "+ adt[13][8:10] +"h"+ adt[13][10:12] +":"+ adt[13][12:14] + "s")
    print("Id interno do paciente: " + adt[15] )
    print("Numero interno: " + adt[16])
    print("Nome do paciente: " + adt[17].replace("^"," "))
    print("Data e hora de nascimento: " + adt[18][0:4]+"/"+adt[18][4:6]+"/"+adt[18][6:8])
    print("Sexo: " + adt[19])
    print("Race: "+ adt[20]) # não tenho a certeza deste
    print("Morada: " + adt[21].replace("^"," "))
    print("Pais: " + adt[22] )
    print("Número de telemovel: " + adt[23])
    print("Primary language: " + adt[24])
    print("Estado civil: " + adt[25])
    print("Telefone de casa: " + adt[26][0:9])
    print("E-mail: " + adt[26][10:29] + "\n")
    print("\n\t\t\t" + "Contacto de emergencia:\n")
    print("Nome: " + adt[29].replace("^"," "))
    print("Relação com o paciente: " + adt[30])
    print("Morada: " + adt[29].replace("^"," "))
    print("Número de telemovel: " + adt[32])
    print("Tipo de Contacto: " + adt[33])
    print("Estado civil: " + adt[34])
    print("Sexo: " + adt[35])
    print("Data de nascimento: " + adt[36][0:4]+ "/"+adt[36][4:6]+ "/" + adt[36][6:8])
    print("Linguagem primária: " + adt[37])
    print("\n\n\n" + "Unidade do paciente: " + adt[40])
    print("Método de codificação de diagnóstico: " + adt[41])
    print("Código de diagnóstico: " + adt[42])
    print("Descrição do diagnóstico: " + adt[43])
    print("Tipo de diagnóstico: " + adt[46])
    print("Médico de diagnóstico: " + adt[47].replace("^"," "))
    print("Clasificação do diagnóstico: " + adt[48])
    print("Código de ação de diagnóstico: " + adt[49])
    print("Sintomas: " + adt[50])
    print(adt[51] + "\n")


def print_message_oru(oru):

    print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
    print("******************************* Servico Hospitalar CHUC ********************************")
    print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
    print("Sending Application: " + oru[2] )
    print("Sending Facility: " + oru[3] )
    print("Receiving Application: " + oru[4] )    
    print("Receiving Facility: " + oru[5] )




    print("\nData da mensagem: " + oru[6][0:4]+"/"+oru[6][4:6]+"/"+oru[6][6:8] )
    print("Hora da mensagem: "+ oru[6][8:10] +"h"+ oru[6][10:12] +":"+ oru[6][12:14] + "s" +"\n")
    print("Tipo de mensagem: " + oru[7].replace("^", "_") )
    print("ID do controlo da mensagem: " + oru[8] )
    print("ID de processamento: " + oru[9] )
    print("Versão do ID: " + oru[10] )

    #falta um
    print("\n\n\t\tPaciente")

    print("\nID : " + oru[12] )
    print("Identificador interno do paciente: " + oru[13])
    print("Nome do paciente: " + oru[14].replace("^"," ") )
    print("\n\n\t\tOBR")
    print("Id: " + oru[16] )
    print("Filler order number: " + oru[17] )
    print("Identificador do serviço: " + oru[18] )
    print("Prioridade: " + oru[19] )
    print("Data da observação: " + oru[20][0:4]+"/"+oru[20][4:6]+"/"+oru[20][6:8] + "\t" + oru[20][8:10] +"h"+ oru[20][10:12] +":"+ oru[20][12:14] + "s")
    print("Informação clinica relevante: " + oru[21])
    print("Estado dos resultados: " + oru[22])

    print("\n\n\t\tOBX"+"\n")
    print("Id: " + oru[24])
    print("Tipo de valor: " + oru[25])
    print("Identificador da observação: " + oru[26])
    print("Estado do resultado de observação: " + oru[28] + "\n")


    #plot ECG
    ecg_data = oru[27].split("^")

    for i in range(len(ecg_data)):
        ecg_data[i] = float(ecg_data[i])
    plt.plot(ecg_data)
    plt.title("Exame: ECG\n Paciente: Gromêncio Sardinha")
    plt.show()


   







if __name__ == "__main__":
    
    adt = set_data("messages.txt")
    oru = set_data("response.txt")

    validate_message(oru)
    validate_message(adt)

    #print(adt)
    #print(oru)
   
    print_message_adt(adt)
    print_message_oru(oru)