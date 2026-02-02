def Read():
    with open("DNA_String.txt", "r") as file:
        DNA=file.read()
    return DNA
DNA_String=Read()

def Cleanup(DNA_String):
    DNA_String=DNA_String.replace(' ', '')
    DNA_String=DNA_String.replace('\n', '')
    DNA_String=DNA_String.replace('\t', '')
    DNA_Length=len(DNA_String)
    print(DNA_String)
    return DNA_String, DNA_Length
DNA_String, DNA_Length=Cleanup(DNA_String)

def Count_Bases(DNA_String, DNA_Length):
    A_Count=C_Count=T_Count=G_Count=Unknown_Count=0

    for i in range(DNA_Length):
        if DNA_String[i].upper() == "A":
            A_Count+=1
        elif DNA_String[i].upper() == "C":
            C_Count+=1
        elif DNA_String[i].upper() == "T":
            T_Count+=1
        elif DNA_String[i].upper() == "G":
            G_Count+=1
        else:
            Unknown_Count+=1
    return A_Count, C_Count, T_Count, G_Count, Unknown_Count
A_Count, C_Count, T_Count, G_Count, Unknown_Count=Count_Bases(DNA_String, DNA_Length)

def GCPercentage(G_Count, C_Count, DNA_Length):
    GC_Percentage=((G_Count+C_Count)/DNA_Length)*100
    return GC_Percentage
GC_Percentage=GCPercentage(G_Count, C_Count, DNA_Length)

print(f"The length of the DNA string is: {DNA_Length}\nThe A count is: {A_Count}"
      f"\nThe C count is: {C_Count}\nThe T count is: {T_Count}\nThe G count is: {G_Count}"
      f"\nThe GC percentage is: {GC_Percentage}%\nThe count of unknowns is: {Unknown_Count}")
        