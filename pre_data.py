import pandas as pd
import os 
import datetime
import time

#Generate new table headers in openCypher load format
map1 = {'creationDate':'creationDate:datetime',
'birthday':'birthday:datetime',
'length':'length:int',
'id':':ID',
'title':'title:string',
'firstName':'firstName:string',
'lastName':'lastName:string',
'gender':'gender:string',
'locationIP':'locationIP:string',
'browserUsed':'browserUsed:string',
'language':'language:string'       ,
'email':'email:string'       ,
'content':'content:string'       ,
'imageFile':'imageFile:string',
       'name':'name:string'
       ,'url':'url:string'
       ,'name_ID':'name_ID:string'
       ,'type':':LABEL'}


map2 = {'classYear':'classYear:int',
       'workFrom':'workFrom:int',
       'PersonId':':START_ID',
       'CompanyId':':END_ID',
       'UniversityId':':END_ID',
       'creationDate':'creationDate:datetime',
       'OrganisationId':':START_ID',
       'PlaceId':':END_ID',
       'Place1Id':':START_ID',
       'Place2Id':':END_ID',
        'TagId':':START_ID',
        'TagClassId':':END_ID',
        'TagClass1Id':':START_ID',
        'TagClass2Id':':END_ID',
        'creationDate':'creationDate:datetime',
        'START_ID':':START_ID',
        'END_ID':':END_ID'
        
       }

#Date to timestamp
format1 ="%Y-%m-%dT%H:%M:%S.%f+00:00"
f = lambda x:time.mktime(time.strptime(x, format1))
f1 = lambda x:i[0].split('_')[0]+'_'+x
f2 = lambda x:i[0].split('_')[2]+'_'+x


dynamic_vertex_list = []
dynamic_edge_list = []
for root,dirs,files in os.walk(r"/path/sf10/csv/bi/composite-projected-fk/initial_snapshot/dynamic/"):
    for file in files:

        if file[-3:] == 'csv':
            if '_' in root.split('/')[-1]:
                edge_type = root.split('/')[-1]
                path1 = os.path.join(root,file)
                print("edge_type")
                print(edge_type,path1)
                dynamic_edge_list.append([edge_type,path1])
            else:
                vertex_type = root.split('/')[-1]
                path2 = os.path.join(root,file)
                print("vertex_type")
                print(vertex_type,path2)
                dynamic_vertex_list.append([vertex_type,path2])







for i in dynamic_vertex_list:
    print(i[0],i[1])
    vertex_type = i[0]
    a = pd.read_csv(i[1],sep='|')
    a['name_ID']=a['id']
    new_name=[]
    for j in a.columns:
        new_name.append(map1[j])
    print(new_name)
    a.columns=new_name
    if 'creationDate:datetime' in new_name:
        a['creationDate1:float'] = a['creationDate:datetime'].apply(f)
        a['year:string']=pd.DatetimeIndex(a['creationDate:datetime']).year
        a['month:string']=pd.DatetimeIndex(a['creationDate:datetime']).month

    if i[0]=='Comment' or  i[0]=='Post':
        a[':LABEL']='Message'
    else:
        
        a[':LABEL']=i[0]
        
    a['name_ID:string']=a[':ID']
    a['name_ID:string']=a['name_ID:string'].astype('string')
    a[':ID'] = a[':LABEL'] +'_'+ a['name_ID:string']
    a.to_csv('new_data_sf10/%s.csv'%(i[0]+'_'+i[1].split('/')[-1].split('-')[1]),index=False,encoding='utf-8')

  

for i in dynamic_edge_list:
    print(i[0],i[1])
    vertex_type = i[0]
    a = pd.read_csv(i[1],sep='|')
    
    new_name=[]
    new_name1=[]
    for j in a.columns:
#         new_name.append(map1[j])
        new_name.append(j)
    if len(new_name)==3:
        
        a.columns = ['creationDate:datetime',':START_ID',':END_ID']
        
        
        a[':START_ID'] = a[':START_ID'].astype('str')
        a[':END_ID'] = a[':END_ID'].astype('str')
        #Change post ,comment tag to message tag

        if i[0].split('_')[0] =='Comment' or  i[0].split('_')[0]=='Post':
            a[':START_ID'] = a[':START_ID'].apply(lambda x:'Message_'+x)
            
        else:
            a[':START_ID'] = a[':START_ID'].apply(f1)
            
        if i[0].split('_')[2] =='Comment' or  i[0].split('_')[2]=='Post':
            a[':END_ID'] = a[':END_ID'].apply(lambda x:'Message_'+x)
        else:
            a[':END_ID'] = a[':END_ID'].apply(f2)
        
        #Generate year and month attributes
        if 'creationDate' in new_name:
            a['creationDate1:float'] = a['creationDate:datetime'].apply(f)
            a['year:string']=pd.DatetimeIndex(a['creationDate:datetime']).year
            a['month:string']=pd.DatetimeIndex(a['creationDate:datetime']).month

        a[':TYPE'] = i[1].split('/')[-2].split('_')[1]
    else:
        for k in new_name:
            
            new_name1.append(map2[k])

        a.columns=new_name1
        if 'creationDate:datetime' in new_name1:
            a['creationDate1:float'] = a['creationDate:datetime'].apply(f)
            a['year:string']=pd.DatetimeIndex(a['creationDate:datetime']).year
            a['month:string']=pd.DatetimeIndex(a['creationDate:datetime']).month

        a[':START_ID'] = a[':START_ID'].astype('str')
        a[':END_ID'] = a[':END_ID'].astype('str')

        if i[0].split('_')[0] =='Comment' or  i[0].split('_')[0]=='Post':
            a[':START_ID'] = a[':START_ID'].apply(lambda x:'Message_'+x)
            
        else:
            a[':START_ID'] = a[':START_ID'].apply(f1)
            
        if i[0].split('_')[2] =='Comment' or  i[0].split('_')[2]=='Post':
            a[':END_ID'] = a[':END_ID'].apply(lambda x:'Message_'+x)
        else:
            a[':END_ID'] = a[':END_ID'].apply(f2)

            a[':TYPE'] = i[1].split('/')[-2].split('_')[1]
    
    a.to_csv('new_data_sf10/%s.csv'%(i[0]+'_'+i[1].split('/')[-1].split('-')[1]),index=False,encoding='utf-8')

  




#static vertex、edge list
static_vertex_list = []
static_edge_list = []
for root,dirs,files in os.walk(r"sf10/csv/bi/composite-projected-fk/initial_snapshot/static/"):
    for file in files:
    
        if file[-3:] == 'csv':
            if '_' in root.split('/')[-1]:
                edge_type = root.split('/')[-1]
                path1 = os.path.join(root,file)
                print("edge_type")
                print(edge_type,path1)
                static_edge_list.append([edge_type,path1])
            else:
                vertex_type = root.split('/')[-1]
                path2 = os.path.join(root,file)
                print("vertex_type")
                print(vertex_type,path2)
                static_vertex_list.append([vertex_type,path2])


#static vertex list
for i in static_vertex_list:
    print(i[0],i[1])
    vertex_type = i[0]
    a = pd.read_csv(i[1],sep='|')
    a['name_ID']=a['id']
    new_name=[]
    for j in a.columns:
        new_name.append(map1[j])
    print(new_name)
    a.columns=new_name
    if 'creationDate:datetime' in new_name:
        a['creationDate:datetime'] = a['creationDate:datetime'].apply(f)
    a['name_ID:string']=a[':ID']
    a[':LABEL']=i[0]

    a['name_ID:string']=a[':ID']
    a['name_ID:string']=a['name_ID:string'].astype('string')
    a[':ID'] = a[':LABEL'] +'_'+ a['name_ID:string']
    a.to_csv('new_data_sf10/%s.csv'%(i[0]+'_'+i[1].split('/')[-1].split('-')[1]),index=False,encoding='utf-8')

  

#static edge list
for i in static_edge_list:
    print(i[0],i[1])
    vertex_type = i[0]
    a = pd.read_csv(i[1],sep='|')
    
    new_name=[]
    new_name1=[]
    for j in a.columns:
#         new_name.append(map2[j])
        new_name.append(j)
    if len(new_name)==3:
        if 'creationDate:datetime' in new_name:
            a['creationDate:datetime'] = a['creationDate:datetime'].apply(f)
            a.columns = ['creationDate:datetime',':START_ID',':END_ID']
            
        a[':START_ID'] = a[':START_ID'].astype('str')
        a[':END_ID'] = a[':END_ID'].astype('str')

        if i[0].split('_')[0] =='Comment' or  i[0].split('_')[0]=='Post':
            a[':START_ID'] = a[':START_ID'].apply(lambda x:'Message_'+x)
            
        else:
            a[':START_ID'] = a[':START_ID'].apply(f1)
            
        if i[0].split('_')[2]=='Comment' or  i[0].split('_')[2]=='Post':
            a[':END_ID'] = a[':END_ID'].apply(lambda x:'Message_'+x)
        else:
            a[':END_ID'] = a[':END_ID'].apply(f2)

        a[':TYPE'] = i[1].split('/')[-2].split('_')[1]
    else:
        for k in new_name:
            new_name1.append(map2[k])
        if 'creationDate:datetime' in new_name1:
            a['creationDate:datetime'] = a['creationDate:datetime'].apply(f)
        a.columns=new_name1
        a[':START_ID'] = a[':START_ID'].astype('str')
        a[':END_ID'] = a[':END_ID'].astype('str')

        if i[0].split('_')[0] =='Comment' or  i[0].split('_')[0]=='Post':
            a[':START_ID'] = a[':START_ID'].apply(lambda x:'Message_'+x)
            
        else:
            a[':START_ID'] = a[':START_ID'].apply(f1)
            
        if i[0].split('_')[2] =='Comment' or  i[0].split('_')[2]=='Post':
            a[':END_ID'] = a[':END_ID'].apply(lambda x:'Message_'+x)
        else:
            a[':END_ID'] = a[':END_ID'].apply(f2)

        a[':TYPE'] = i[1].split('/')[-2].split('_')[1]
    

    
    a.to_csv('new_data_sf10/%s.csv'%(i[0]+'_'+i[1].split('/')[-1].split('-')[1]),index=False,encoding='utf-8')


#The Place file format differs from other documents in that it includes multiple label tags, which need to be handled separately
a = pd.read_csv('/path/static/Place/part-00000-a3197cb7-c39f-4266-b693-9c1b3a4a740f-c000.csv',sep='|')
a['id']=a['id'].astype('str')
a['name_id']=a['id']
a['id']=a['type']+'_'+a['id']
a.columns=[':ID','name:string','url:string',':LABEL','name_id:string']
a.to_csv('new_data_sf10/Place_00000.csv',index=False)

#Processing of Place-related documents
a = pd.read_csv('sf10/csv/bi/composite-projected-fk/initial_snapshot/static/Place/part-00000-a3197cb7-c39f-4266-b693-9c1b3a4a740f-c000.csv',sep='|')
b = pd.read_csv('sf10/csv/bi/composite-projected-fk/initial_snapshot/static/Organisation_isLocatedIn_Place/part-00000-8b79eaba-8cfd-4b1b-9187-d2496d62f404-c000.csv',sep='|')
a0 = pd.read_csv('sf10/csv/bi/composite-projected-fk/initial_snapshot/static/Place_isPartOf_Place/part-00000-3444edd7-a1fe-4f70-b208-fe37a1efe192-c000.csv',sep='|')
a1 = pd.read_csv('sf10/csv/bi/composite-projected-fk/initial_snapshot/dynamic/Person_workAt_Company/part-00000-65041523-753a-4213-a466-26db2b709e37-c000.csv',sep='|')

c = pd.merge(a,b,left_on='id',right_on='PlaceId',how='inner')

c['PlaceId'] = c['PlaceId'].astype('str')
c['PlaceId']=c['type']+'_'+c['PlaceId']
c['OrganisationId'] = c['OrganisationId'].astype('str')
c['OrganisationId']=c['OrganisationId'].apply(lambda x:'Organisation_'+x)
c[':TYPE']='isLocatedIn'
c = c[['OrganisationId','PlaceId',':TYPE']]
c.columns=[':START_ID',':END_ID',':TYPE']
c.to_csv('new_data/Organisation_isLocatedIn_Place_00000.csv',index=False)

d = pd.merge(a,a0,left_on='id',right_on='Place1Id',how='inner')
d1 = pd.merge(a,d,left_on='id',right_on='Place2Id',how='inner')
d1['Place1Id']=d1['Place1Id'].astype('str')
d1['Place2Id']=d1['Place2Id'].astype('str')
d1['Place1Id']=d1['type_y']+'_'+d1['Place1Id']
d1['Place2Id']=d1['type_x']+'_'+d1['Place2Id']
d1[':TYPE']='isPartOf'
d1 = d1[['Place1Id','Place2Id',':TYPE']]
d1.columns=[':START_ID',':END_ID',':TYPE']
d1.to_csv('new_data/Place_isPartOf_Place_00000.csv',index=False)

a0 = pd.read_csv('new_data/Person_workAt_Company_00000.csv')
a0[':END_ID'] = a0[':END_ID'].apply(lambda x:'Organisation_'+x.split('_')[1])
a0.to_csv('new_data/Person_workAt_Company_00000.csv',index=False)

a1 = pd.read_csv('new_data/Person_studyAt_University_00000.csv')
a1[':END_ID'] = a1[':END_ID'].apply(lambda x:'Organisation_'+x.split('_')[1])
a1.to_csv('new_data/Person_studyAt_University_00000.csv',index=False)