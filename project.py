import os
import random
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def random_file(file):
    csv_file=[]
    for file1 in os.listdir(file):
        if file1.endswith(".csv"):
            csv_file.append(file1)
    if csv_file:
        random_csv_file =random.choice(csv_file) 
        file_result=os.path.join(file,random_csv_file)
        return file_result
    
def tamrin1(f):
        read=pd.read_csv(f)
        head_file=read.head(6)
        print(head_file)
        print('-'*200)
        print('Dataset Information: ''\n')
        print(head_file.info())
        print('-'*200)
        print('Missing data information: ''\n')
        nan=head_file.isnull().sum()
        print(nan)
        print('-'*200)
        print('')

        
def tamrin2(f):
    tail_file=pd.read_csv(f)
    tail_file=tail_file.tail(6)
    col_name=['Country_Region','Confirmed','Deaths','Recovered','Active']
    result2=tail_file[col_name].reset_index(drop=True)
    print(result2)
    print('-'*200)
    mean_C=tail_file['Confirmed'].mean()
    median_C=tail_file['Confirmed'].median()
    mode_C=tail_file['Confirmed'].mode()[0]
    std_C=tail_file['Confirmed'].std()
    mean_D=tail_file['Deaths'].mean()
    median_D=tail_file['Deaths'].median()
    mode_D=tail_file['Deaths'].mode()[0]
    std_D=tail_file['Deaths'].std()
    mean_R=tail_file['Recovered'].mean()
    median_R=tail_file['Recovered'].median()
    mode_R=tail_file['Recovered'].mode()[0]
    std_R=tail_file['Recovered'].std()
    mean_A=tail_file['Active'].mean()
    median_A=tail_file['Active'].median()
    mode_A=tail_file['Active'].mode()[0]
    std_A=tail_file['Active'].std()

    print(f"Confirmed column :\nMean:{mean_C}\nMedian:{median_C}\nMode:{mode_C}\nSTD:{std_C}\n")
    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")
    print(f"Recovered column :\nMean:{mean_R}\nMedian:{median_R}\nMode:{mode_R}\nSTD:{std_R}\n")
    print(f"Active column :\nMean:{mean_A}\nMedian:{median_A}\nMode:{mode_A}\nSTD:{std_A}\n")




def tamrin3(f):
    read=pd.read_csv(f,index_col='Country_Region')
    country_group=read.groupby(['Country_Region','Province_State']).agg(
        Confirmed=('Confirmed','sum'),
        Deaths=('Deaths','sum'),
        Recovered=('Recovered','sum'))
    print(country_group)
    print('-'*200)
    mean_C=country_group['Confirmed'].mean()
    median_C=country_group['Confirmed'].median()
    mode_C=country_group['Confirmed'].mode()[0]
    std_C=country_group['Confirmed'].std()
    mean_D=country_group['Deaths'].mean()
    median_D=country_group['Deaths'].median()
    mode_D=country_group['Deaths'].mode()[0]
    std_D=country_group['Deaths'].std()
    mean_R=country_group['Recovered'].mean()
    median_R=country_group['Recovered'].median()
    mode_R=country_group['Recovered'].mode()[0]
    std_R=country_group['Recovered'].std()

    
    print(f"Confirmed column :\nMean:{mean_C}\nMedian:{median_C}\nMode:{mode_C}\nSTD:{std_C}\n")
    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")
    print(f"Recovered column :\nMean:{mean_R}\nMedian:{median_R}\nMode:{mode_R}\nSTD:{std_R}\n")
   





def tamrin4(f):
    read=pd.read_csv(f)
    China_info=read[read['Country_Region']=='China'].reset_index(drop=True)
    name_col=['Province_State','Confirmed','Deaths','Recovered']
    print(China_info[name_col])
    print('-'*200)
    mean_C=China_info['Confirmed'].mean()
    median_C=China_info['Confirmed'].median()
    mode_C=China_info['Confirmed'].mode()[0]
    std_C=China_info['Confirmed'].std()
    mean_D=China_info['Deaths'].mean()
    median_D=China_info['Deaths'].median()
    mode_D=China_info['Deaths'].mode()[0]
    std_D=China_info['Deaths'].std()
    mean_R=China_info['Recovered'].mean()
    median_R=China_info['Recovered'].median()
    mode_R=China_info['Recovered'].mode()[0]
    std_R=China_info['Recovered'].std()

    
    print(f"Confirmed column :\nMean:{mean_C}\nMedian:{median_C}\nMode:{mode_C}\nSTD:{std_C}\n")
    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")
    print(f"Recovered column :\nMean:{mean_R}\nMedian:{median_R}\nMode:{mode_R}\nSTD:{std_R}\n")



def tamrin5(f):
    read=pd.read_csv(f)
    print(read.groupby('Country_Region')['Deaths'].sum().tail(10).reset_index())
    print('-'*200)
    mean_D=read.groupby('Country_Region')['Deaths'].sum().mean()
    median_D=read.groupby('Country_Region')['Deaths'].sum().median()
    mode_D=read.groupby('Country_Region')['Deaths'].sum().mode()[0]
    std_D=read.groupby('Country_Region')['Deaths'].sum().std()

    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")



def tamrin6(f):
    read=pd.read_csv(f)
    Recovered_zero=read[read['Recovered']==0].reset_index(drop=True)
    name_col=['Country_Region','Confirmed','Deaths','Recovered']
    print(Recovered_zero[name_col])
    print('-'*200)
    mean_C=Recovered_zero['Confirmed'].mean()
    median_C=Recovered_zero['Confirmed'].median()
    mode_C=Recovered_zero['Confirmed'].mode()[0]
    std_C=Recovered_zero['Confirmed'].std()
    mean_D=Recovered_zero['Deaths'].mean()
    median_D=Recovered_zero['Deaths'].median()
    mode_D=Recovered_zero['Deaths'].mode()[0]
    std_D=Recovered_zero['Deaths'].std()

    print(f"Confirmed column :\nMean:{mean_C}\nMedian:{median_C}\nMode:{mode_C}\nSTD:{std_C}\n")
    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")
  



def tamrin7(f):
    read=pd.read_csv(f)
    mean_C=read['Confirmed'].mean()
    median_C=read['Confirmed'].median()
    mode_C=read['Confirmed'].mode()[0]
    std_C=read['Confirmed'].std()
    mean_D=read['Deaths'].mean()
    median_D=read['Deaths'].median()
    mode_D=read['Deaths'].mode()[0]
    std_D=read['Deaths'].std()
    print(f"Confirmed column :\nMean:{mean_C}\nMedian:{median_C}\nMode:{mode_C}\nSTD:{std_C}\n")
    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")
    print('-'*200)
    read=read[read['Confirmed']!=0]
    read=read[read['Deaths']!=0]
    info=read[read['Confirmed']==read['Deaths']].reset_index(drop=True)
    name_col=['Country_Region','Confirmed','Deaths']
    print(info[name_col])
   

def tamrin8(f):
    read=pd.read_csv(f)
    mean_C=read['Confirmed'].mean()
    median_C=read['Confirmed'].median()
    mode_C=read['Confirmed'].mode()[0]
    std_C=read['Confirmed'].std()
    mean_R=read['Recovered'].mean()
    median_R=read['Recovered'].median()
    mode_R=read['Recovered'].mode()[0]
    std_R=read['Recovered'].std()
    print(f"Confirmed column :\nMean:{mean_C}\nMedian:{median_C}\nMode:{mode_C}\nSTD:{std_C}\n")
    print(f"Recovered column :\nMean:{mean_R}\nMedian:{median_R}\nMode:{mode_R}\nSTD:{std_R}\n")
    print('-'*200)
    read=read[read['Confirmed']!=0]
    read=read[read['Recovered']!=0]
    info=read[read['Confirmed']==read['Recovered']].reset_index(drop=True)
    name_col=['Country_Region','Confirmed','Recovered']
    print(info[name_col])


def tamrin9(f):
    read=pd.read_csv(f,index_col="Country_Region") 
    read.sort_values(['Last_Update','Confirmed','Deaths','Recovered'],na_position='last',ascending=False)
    name_col=['Last_Update','Confirmed','Deaths','Recovered']
    print('Dataset information:''\n')
    print(read[name_col].head(10))
    print('-'*200)
    mean_C=read['Confirmed'].head(10).mean()
    median_C=read['Confirmed'].head(10).median()
    mode_C=read['Confirmed'].head(10).mode()[0]
    std_C=read['Confirmed'].head(10).std()
    mean_D=read['Deaths'].head(10).mean()
    median_D=read['Deaths'].head(10).median()
    mode_D=read['Deaths'].head(10).mode()[0]
    std_D=read['Deaths'].head(10).std()
    mean_R=read['Recovered'].head(10).mean()
    median_R=read['Recovered'].head(10).median()
    mode_R=read['Recovered'].head(10).mode()[0]
    std_R=read['Recovered'].head(10).std()

    
    print(f"Confirmed column :\nMean:{mean_C}\nMedian:{median_C}\nMode:{mode_C}\nSTD:{std_C}\n")
    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")
    print(f"Recovered column :\nMean:{mean_R}\nMedian:{median_R}\nMode:{mode_R}\nSTD:{std_R}\n")
    
    
def tamrin10(f):
    read=pd.read_csv(f)
    read=read[read["Deaths"] > 150]
    name_col=['Active','Confirmed','Deaths','Recovered',"Country_Region"]
    new_df=read[name_col].head(10)

    mean_C=read['Confirmed'].mean()
    median_C=read['Confirmed'].median()
    mode_C=read['Confirmed'].mode()[0]
    std_C=read['Confirmed'].std()
    mean_D=read['Deaths'].mean()
    median_D=read['Deaths'].median()
    mode_D=read['Deaths'].mode()[0]
    std_D=read['Deaths'].std()
    mean_R=read['Recovered'].mean()
    median_R=read['Recovered'].median()
    mode_R=read['Recovered'].mode()[0]
    std_R=read['Recovered'].std()
    mean_A=read['Active'].mean()
    median_A=read['Active'].median()
    mode_A=read['Active'].mode()[0]
    std_A=read['Active'].std()

    print(f"Confirmed column :\nMean:{mean_C}\nMedian:{median_C}\nMode:{mode_C}\nSTD:{std_C}\n")
    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")
    print(f"Recovered column :\nMean:{mean_R}\nMedian:{median_R}\nMode:{mode_R}\nSTD:{std_R}\n")
    print(f"Active column :\nMean:{mean_A}\nMedian:{median_A}\nMode:{mode_A}\nSTD:{std_A}\n")




    plt.figure(figsize=(10,6))
    plt.title('Total Deaths (>150), Confirmed, Recovered, and Active Cases by Country',fontsize=8,color='black')
    plt.plot(new_df['Country_Region'],new_df['Deaths'])
    plt.plot(new_df['Country_Region'],new_df['Active'])
    plt.plot(new_df['Country_Region'],new_df['Confirmed'])
    plt.plot(new_df['Country_Region'],new_df['Recovered'])
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()



def tamrin11(f):
    read=pd.read_csv(f)
    country_group=read.groupby(['Country_Region'])
    US_group=country_group.get_group('US')
    stat_group=US_group.groupby(['Province_State'])
    sum_deaths_group=stat_group['Deaths'].agg(sum)
    
    mean_D=sum_deaths_group.mean()
    median_D=sum_deaths_group.median()
    mode_D=sum_deaths_group.mode()[0]
    std_D=sum_deaths_group.std()

    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")



    plt.figure(figsize=(12,6))
    plt.title('Stat wise deaths reported of COVID-19 in USA',fontsize=15,color='black')
    plt.bar(sum_deaths_group.index,sum_deaths_group.values,color='maroon',width=0.8)
    plt.ylabel('Deaths',fontsize=15)
    plt.xlabel('American states',fontsize=15)
    plt.xticks(rotation=90)
    plt.grid(alpha=0.2)

    plt.tight_layout()
    plt.show()





def tamrin12(f):
    read=pd.read_csv(f)
    country_group=read.groupby(['Country_Region'])
    US_group=country_group.get_group('US')
    stat_group=US_group.groupby(['Province_State'])
    sum_active_group=stat_group['Active'].agg(sum)

    mean_A= sum_active_group.mean()
    median_A= sum_active_group.median()
    mode_A= sum_active_group.mode()[0]
    std_A= sum_active_group.std()

    print(f"Active column :\nMean:{mean_A}\nMedian:{median_A}\nMode:{mode_A}\nSTD:{std_A}\n")



    plt.figure(figsize=(12,6))
    plt.title('Stat wise active reported of COVID-19 in USA',fontsize=15,color='black')
    plt.bar(sum_active_group.index,sum_active_group.values,color='skyblue',width=0.8)
    plt.ylabel('Active',fontsize=15)
    plt.xlabel('American states',fontsize=15)
    plt.xticks(rotation=90)
    plt.grid(alpha=0.2)

    plt.tight_layout()
    plt.show()






def tamrin13(f):
    read=pd.read_csv(f)
    country_group=read.groupby(['Country_Region'])
    US_group=country_group.get_group('US')
    state_group=US_group.groupby(['Province_State'])
    sum_active_group=state_group['Active'].agg(sum)
    sum_deaths_group=state_group['Deaths'].agg(sum)
    sum_confirmed_group=state_group['Confirmed'].agg(sum)
    sum_recovered_group=state_group['Recovered'].agg(sum)


    mean_C=sum_confirmed_group.mean()
    median_C=sum_confirmed_group.median()
    mode_C=sum_confirmed_group.mode()[0]
    std_C=sum_confirmed_group.std()
    mean_D=sum_deaths_group.mean()
    median_D=sum_deaths_group.median()
    mode_D=sum_deaths_group.mode()[0]
    std_D=sum_deaths_group.std()
    mean_R=sum_recovered_group.mean()
    median_R=sum_recovered_group.median()
    mode_R=sum_recovered_group.mode()[0]
    std_R=sum_recovered_group.std()
    mean_A=sum_active_group.mean()
    median_A=sum_active_group.median()
    mode_A=sum_active_group.mode()[0]
    std_A=sum_active_group.std()

    print(f"Confirmed column :\nMean:{mean_C}\nMedian:{median_C}\nMode:{mode_C}\nSTD:{std_C}\n")
    print(f"Deaths column :\nMean:{mean_D}\nMedian:{median_D}\nMode:{mode_D}\nSTD:{std_D}\n")
    print(f"Recovered column :\nMean:{mean_R}\nMedian:{median_R}\nMode:{mode_R}\nSTD:{std_R}\n")
    print(f"Active column :\nMean:{mean_A}\nMedian:{median_A}\nMode:{mode_A}\nSTD:{std_A}\n")

    x = np.arange(len(sum_active_group))

    plt.figure(figsize=(12, 6))
    plt.title('USA State-wise Combine Number of Confirmed, Deaths, Active, Recovered', fontsize=12, color='black')

    plt.bar(x - 1.5 * 0.2, sum_active_group, width=0.2, label='Active', color='yellow')
    plt.bar(x - 0.5 * 0.2, sum_deaths_group, width=0.2, label='Deaths', color='maroon')
    plt.bar(x + 0.5 * 0.2, sum_confirmed_group, width=0.2, label='Confirmed', color='blue')
    plt.bar(x + 1.5 * 0.2, sum_recovered_group, width=0.2, label='Recovered', color='green')

    plt.ylabel('Count', fontsize=12)
    plt.xlabel('Province/State', fontsize=12)
    plt.xticks(x, sum_active_group.index, rotation=90) 
    plt.grid(alpha=0.2)

    plt.legend(title='Case')

    plt.tight_layout()
    plt.show()




def tamrin14(f):
    df = pd.DataFrame()

    for file in os.listdir(f):
        if '2022' in file and file.endswith('.csv'):
            file_path = os.path.join(f, file)
            read = pd.read_csv(file_path)
            df = pd.concat([df, read])

    df['Date'] = pd.to_datetime(df['Last_Update']).dt.date
    df = df.groupby('Date')['Confirmed'].sum().reset_index()


    plt.figure(figsize=(12,6))
    plt.plot(df['Date'],df['Confirmed'],color = 'red')

    plt.show()

    






random_file("C:/Users/ASUS/Desktop/Covid19/")
# tamrin1(random_file("C:/Users/ASUS/Desktop/Covid19/"))               
# tamrin2(random_file("C:/Users/ASUS/Desktop/Covid19/"))               
# tamrin3(random_file("C:/Users/ASUS/Desktop/Covid19/"))               
# tamrin4(random_file("C:/Users/ASUS/Desktop/Covid19/"))               
# tamrin5(random_file("C:/Users/ASUS/Desktop/Covid19/"))               
# tamrin6(random_file("C:/Users/ASUS/Desktop/Covid19/"))               
# tamrin7(random_file("C:/Users/ASUS/Desktop/Covid19/"))               
# tamrin8(random_file("C:/Users/ASUS/Desktop/Covid19/"))               
# tamrin9(random_file("C:/Users/ASUS/Desktop/Covid19/"))              
# tamrin10(random_file("C:/Users/ASUS/Desktop/Covid19/"))              
# tamrin11(random_file("C:/Users/ASUS/Desktop/Covid19/"))              
# tamrin12(random_file("C:/Users/ASUS/Desktop/Covid19/"))              
# tamrin13(random_file("C:/Users/ASUS/Desktop/Covid19/"))              
# tamrin14("C:/Users/ASUS/Desktop/Covid19/")                           
