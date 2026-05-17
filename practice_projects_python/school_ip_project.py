import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the DataFrame
df = pd.read_csv('C:\\Users\\YUTHISH KRISHNA H\\OneDrive\\Documents\\test.csv', index_col='roll')
print(df)
z=1
while(z==1):
    print('''
    Type e  - Enter the details of students
    Type a  - Alter any specific mark of student
    Type an - Alter name of student
    Type d  - Delete the records of any particular student
    Type pl - Plot a line graph of particular column
    Type s  - Show the details of a student
    Type y  - To show the dataaframe
    ''')
    
    x = input('Enter the operation you need to perform: ').lower()
    
    if x == 'e':
        cont=1
        while(cont==1):
            df = pd.read_csv('C:\\Users\\YUTHISH KRISHNA H\\OneDrive\\Documents\\test.csv', index_col='roll')
            name = input('Enter the name of student: ')
            ip = int(input('Enter the marks secured in IP: '))
            maths = int(input('Enter the marks secured in Maths: '))
            physics = int(input('Enter the marks scored in Physics: '))
            chemistry = int(input('Enter the marks secured in Chemistry: '))
            english = int(input('Enter the marks secured in English: '))
            
            df.loc[len(df)+1] = [ name, ip, maths, physics, chemistry, english]
            
            
            df.to_csv('C:\\Users\\YUTHISH KRISHNA H\\OneDrive\\Documents\\test.csv')
            cont = int(input('Press 1 to continue or any other key to stop: '))
        print('succesfully updated')
        print(df)        
            
        
    elif x == 'a':
        roll = int(input('Enter the roll no: '))
        column = input('Enter the column name to change: ')
        new_value = int(input('Enter the new value: '))
        
        if(column==['ip','physics','chemistry','english','maths']):
            index = df[df.index == roll].index
            if(index.empty==False):
                df.loc[index, column] = new_value
                print('Changes made successfully.')
            else:
                print('Roll number not found.')
        else:
            print('invalid')
    
    elif x == 'an':
        roll = int(input('Enter the roll no: '))
        new_value = input('Enter the new name: ')
        
        index = df[df.index == roll].index
        if(index.empty==False):
                df.loc[index,'name'] = new_value
                print('Changes made successfully.')
        else:
                print('Roll number not found.')
                    
    
    elif x == 'd':
        roll = int(input('Enter the roll no to delete: '))
        index = df[df.index == roll].index
        if(index.empty==False):
            df.drop(index, inplace=True)
            print('Record deleted.')
        else:
            print('Roll number not found.')
    
    elif x == 'pl':
        column = input('Enter the column name to plot: ')
        x=np.arange(0,len(df))
        if(column in df.columns):
            plt.plot(x, df[column])
            plt.xlabel('Roll Number')
            plt.ylabel(column)
            plt.show()
        else:
            print('Invalid column name.')
    
    elif x == 's':
        roll = int(input('Enter the roll no to view: '))
        if(roll in df.index):
                print(df.loc[roll,:])
        else:
            print('Roll number not found.')
    
    elif x=='y' :
        print(df)       
    
    else:
        print('Invalid input.')
        
    z=int(input('enter 1 to continue :'))    
    
df.to_csv('C:\\Users\\YUTHISH KRISHNA H\\OneDrive\\Documents\\test.csv')
