class uniVariate():
    def quanQual(p_dataset): #This function is used to separate quantitative and qualitative columns from the given dataset
        p_Qual=[]
        p_Quan=[]
        for columnName in p_dataset.columns:
            #print(columnName)
            if(p_dataset[columnName].dtypes == 'O'):
                #print("Qual")
                p_Qual.append(columnName)
            else:
                #print("Quan")
                p_Quan.append(columnName)  
        return p_Quan, p_Qual # function can return 'n' number of values