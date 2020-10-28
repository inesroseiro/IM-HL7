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
            print("Message ORY_R01 validated")
    
    elif message[5] == 'ADT^A01' :
        # segmentos obrigatorios MSH EVN PID PV1
        if "MSH" and "EVN" and "PID" and "PV1" in message:
            print("Message ADT_A01 validated")



def print_message_adt(adt):
    print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
    print("******************************* Servico Hospitalar " + adt[2] + " ********************************")
    print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*..*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
    print("Data da mensagem: " + adt[4][0:4]+"/"+adt[4][4:6]+"/"+adt[4][6:8] + "\n")
    print("Hora da mensagem: " + adt[4][8:10]+":"+adt[4][10:12]+"\n")
    print("Tipo da mensagem: " + adt[5] + "\n")
    print("Id de controlo: " + adt[6] +  "\n")
    print("Data do registo: " + adt[11][0:4]+ "/"+adt[11][4:6]+ "/" + adt[11][6:8] + "\n")
    print("Hora do registo: "+ adt[11][8:10] +"h"+ adt[11][10:12] +":"+ adt[11][12:14] + "s" +"\n")
    print("Id do paciente: " + adt[13] + "\n")
    print("Numero interno: " + adt[14] + "\n")
    print("Nome do paciente: " + adt[15] +"\n")
    print("Data e hora do nascimento: " + adt[16][0:4]+"/"+adt[16][4:6]+"/"+adt[16][6:8] + "\n")
    print("Sexo: " + adt[17] + "\n")
    print("Race: "+ adt[18] + "\n ")#não tenho a certeza deste
    print("Morada: " + adt[19] + "\n")
    print("Pais: " + adt[20] + "\n")
    print("Número de telemovel: " + adt[21] + "\n")
    print("Primary language: " + adt[22] + "\n")
    print("Estado civil: " + adt[23] + "\n")
    print("Telefone de casa: " + adt[24][0:9] + "\n")
    print("E-mail: " + adt[24][10:29] + "\n")
    print("\n" + "Contacto de emegencia:\n")
    print("Nome: " + adt[27] + "\n")
    print("Relação com o paciente: " + adt[28] + "\n")
    print("Morada: " + adt[29] + "\n")
    print("Número de telemovel: " + adt[30] + "\n")
    print("Contact rule: " + adt[31] + "\n")
    print("Estado civil: " + adt[32] + "\n")
    print("Sexo: " + adt[33] + "\n")
    print("Dia de aniversário: " + adt[34][0:4]+ "/"+adt[34][4:6]+ "/" + adt[34][6:8] + "\n")
    print("Linguagem: " + adt[35] + "\n")
    print("\n\n\n" + "Classe do paciente: " + adt[38] + "\n\n\n")
    print("Método de codificação de diagnóstico: " + adt[41] + "\n")
    print("Código de diagnóstico: " + adt[42] + "\n")
    print("Descrição do diagnóstico: " + adt[43] + "\n")
    print("Tipo de diagnóstico: " + adt[44] + "\n")
    print("Médico de diagnóstico: " + adt[45] + "\n")
    print("Clasificação do diagnóstico: " + adt[46] + "\n")
    print("Código de ação de diagnóstico: " + adt[47] + "\n")
    print("Diagnóstico parental: " + adt[48] + "\n")
    print("Código de valor Drg Ccl: " + adt[49] + "\n")


def print_message_oru(oru):

    #plot ECG
    ecg_data = oru[28].split("^")

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

    print_message_adt(adt)
    print(adt)
    print("\n")
    print(oru)

   

    print_message_oru(oru)