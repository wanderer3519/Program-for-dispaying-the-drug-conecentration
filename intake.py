import pandas as pd

'''
    All the codes used in this file can be found at the following webpage
    https://www.digitalocean.com/community/tutorials/pandas-read_excel-reading-excel-file-in-python
    
    Here, pandas, a popular python library is used to read inputs from an excel sheet.
    After reading the input, it also gets the data specified in the coloumns to a hashmap.

    As an exercise, I have calculated the averages of the data present in specific coloums of the sheet.
'''
xlsheet = './Test_input.xlsx'

def read_input(xlsheet: str):
    df = 0 # random init to avoid errors
    df = pd.read_excel(xlsheet) # reads the entire sheet (by default the first sheet)

    ''' prints the entire sheet '''
    # print(df) 

    ''' prints the coloumns '''
    # print(df.columns.ravel()) 

    ''' gets a list representation of the elements in the specified coloumn '''
    # print(df['population'].tolist())

    input_data: dict[str, list] = {}

    # converting xlsheet into a hashmap
    for col_name in df.columns.ravel():
        input_data[col_name] = df[col_name].tolist()

    return input_data


'''
    Get a value of current for a given time input.
    This one has two styles of implementation.
    Any one of the styles discussed below will do fine.
'''
def current(xlsheet: str, time: int) -> float:
    
    temp: dict[str, list] = read_input(xlsheet)
    time_list: list[int] = temp['Time(s)']
    current_list: list[float] = temp['Current(mA)']

    ''' One type of implementation '''
    '''
        index: int = time_list.index(time)  
        retval: float = current_list[index]
    '''

    ''' Or else, map each of the values in "Time(s)" to "Current(mA)" '''
    
    hashMap: dict[int, float] = {time_list[i] : current_list[i] for i in range(len(time_list))}
    retval: float = hashMap[time]

    return retval

def voltage_current(xlsheet: str, out_file: str):
    data = read_input(xlsheet=xlsheet)
    data.pop("Time(s)")
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Write DataFrame to Excel
    df.to_excel(out_file, index=False)
    
    print("Data has been written to", out_file)

# sheet = './Test_input.xlsx'
# outfile = "./test.xlsx"
# voltage_current(sheet, outfile)

def avg_current(xlsheet: str) -> int:
    data = read_input(xlsheet=xlsheet)
    currents = data['Current(mA)']
    len_curr = len(currents)
    sum_curr = sum(currents)

    avg_curr = sum_curr / len_curr
    avg_curr = round(avg_curr, 3)
    return avg_curr

# sheet = './Test_input.xlsx'
# avg_curr = avg_current(sheet)
# print(avg_curr)


    

'''
dict = {#i : #i for i in range(len(current))}

sum = 0
i = 0
for key in dict:
    if(dict[key] == v):
       sum += key
        i += 1
avgSum = sum / i  
'''
