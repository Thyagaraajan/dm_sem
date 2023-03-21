import pandas as pd
from math import log2
import copy

df = pd.read_csv('play_tennis.csv')

Final_ans=[]

def intial(df):
  input={}
  output={}
  attributes=df.columns.tolist()
  attributes.remove('day')
  attributes.remove('play')
  for j in range(1,len(attributes)+1):
    List=[]
    for i in range(0,len(df)):
      ele=df.iloc[i,j]
      List.append(ele)
    input[attributes[j-1]]=List

  List=[]
  for i in range(0,len(df)):
    List.append(df.iloc[i,len(attributes)+1])
  
  output['play']=List
  Parameter=[]
  Parameter.append(input)
  Parameter.append(output)
  Parameter.append(attributes)
  return Parameter

def helper(inputDict,attributes,level):
  returnList=[]
  returnList.append(attributes[level])
  value=inputDict[attributes[level]]
  unique_values=set(value)
  unique_list=list(unique_values)
  returnList.append(unique_list)
  return returnList

def check_mixed(attribute,attribute_value,inputDict,outputDict):
  List=inputDict[attribute]
  #print(List)
  countYes=0
  countNo=0
  for i in range(0,len(List)):
    if List[i] == attribute_value:
      if outputDict['play'][i]=='Yes':
        countYes=countYes+1
      elif outputDict['play'][i]=='No':
        countNo=countNo+1
  #pure yes
  if countNo == 0:
    return 1
  #pure no
  elif countYes == 0:
    return -1
  #mixed
  else:
    return 0
  
  
def filterData(df,value,attribute):
  #print(df)
  all_attributes=df.columns.tolist()
  col_index=0;
  #print(all_attributes)
  for a in range(0,len(all_attributes)):
    if all_attributes[a] == attribute:
      col_index=a
      break;

  index=[]
  total_index=[]
  delete_index=[]
  for i in range(0,len(df)):
    total_index.append(i)
    if(df.iloc[i,col_index]==value):
      index.append(i)
  
  #print(index)
  #print(total_index)
  for i in total_index:
    if not i in index:
      delete_index.append(i)
  #print(delete_index)
  new_df=df.drop(delete_index)
  new_df.set_axis(range(len(new_df)), inplace=True)
  lisCol=[]
  lisCol.append(attribute)
  new_df_1=new_df.drop(attribute,axis=1)
  #print(new_df_1)
  return new_df_1

def recur(df,level,path,attributes):
  Intial_Parameters=intial(df)
  inputDict=Intial_Parameters[0]
  outputDict=Intial_Parameters[1]
  List=helper(inputDict,attributes,level)
  path.append(List[0])
  for i in List[1]:
    path.append(i)
    flag=check_mixed(attributes[level],i,inputDict,outputDict)
    if flag==1:
      print(path,end=" ")
      print('Yes')
    
    elif flag==-1:
      print(path,end=" ")
      print('No')

    else:
      new_df=filterData(df,i,attributes[level])
      recur(new_df,level+1,path,attributes)
    path.pop()
  path.pop()
  
Intial_Parameters=intial(df)
#inputDict=Intial_Parameters[0]
#outputDict=Intial_Parameters[1]
attributes=Intial_Parameters[2]
#print(helper(inputDict,attributes,0))
#print(check_mixed('outlook','Overcast',inputDict,outputDict))
recur(df,0,[],attributes)


