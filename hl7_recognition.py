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
    print("Data da mensagem: " + adt[4][0:4]+"/"+adt[4][4:6]+"/"+adt[4][6:8])
    print("Hora da mensagem: " + adt[4][8:10]+":"+adt[4][10:12]+"\n")

    print("Numero interno: " + adt[14])



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