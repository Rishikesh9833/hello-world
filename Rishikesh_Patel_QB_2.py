# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:44:59 2019

@author: admin
"""
unique_list = [] 
# function to get unique values 
def unique(list1): 
  
    # intilize a null list 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for y in unique_list: 
        print (y), 
      
# function to get unique values 
def MaxNum(listNum): 
    # intilize a null list 
    max_num = 0;
      
    # traverse for all elements 
    for x in listNum: 
        # check if exists in unique_list or not 
        if float(x) > max_num: 
            max_num = float(x)
    
    # print list 
    print (max_num), 

def SumNum(listNum): 
    # intilize a null list 
    Sum_num = 0;
      
    # traverse for all elements 
    for x in listNum: 
            Sum_num = Sum_num + float(x)
    
    # print list 
    print (Sum_num), 


lst = [ "-122.23,37.88,41.0,880.0,129.0,322.0,126.0,8.3252,452600.0,NEAR BAY",
"-122.22,37.86,21.0,7099.0,1106.0,2401.0,1138.0,8.3014,358500.0,NEAR BAY",
"-122.24,37.85,52.0,1467.0,190.0,496.0,177.0,7.2574,352100.0,NEAR BAY",
"-122.25,37.85,52.0,1274.0,235.0,558.0,219.0,5.6431,341300.0,NEAR BAY",
"-122.25,37.85,52.0,1627.0,280.0,565.0,259.0,3.8462,342200.0,NEAR BAY",
"-122.25,37.85,52.0,919.0,213.0,413.0,193.0,4.0368,269700.0,NEAR BAY",
"-122.25,37.84,52.0,2535.0,489.0,1094.0,514.0,3.6591,299200.0,NEAR BAY",
"-122.25,37.84,52.0,3104.0,687.0,1157.0,647.0,3.12,241400.0,NEAR BAY",
"-122.26,37.84,42.0,2555.0,665.0,1206.0,595.0,2.0804,226700.0,NEAR BAY",
"-122.25,37.84,52.0,3549.0,707.0,1551.0,714.0,3.6912,261100.0,NEAR BAY",
"-122.26,37.85,52.0,2202.0,434.0,910.0,402.0,3.2031,281500.0,NEAR BAY",
"-118.46,34.16,16.0,4590.0,1200.0,2195.0,1139.0,3.8273,334900.0,<1H OCEAN",
"-118.47,34.15,7.0,6306.0,1473.0,2381.0,1299.0,4.642,457300.0,<1H OCEAN",
"-118.47,34.16,30.0,3823.0,740.0,1449.0,612.0,4.6,392500.0,<1H OCEAN",
"-118.47,34.15,43.0,804.0,117.0,267.0,110.0,8.2269,500001.0,<1H OCEAN",
"-118.48,34.15,31.0,2536.0,429.0,990.0,424.0,5.4591,495500.0,<1H OCEAN",
"-118.48,34.16,30.0,3507.0,536.0,1427.0,525.0,6.7082,500001.0,<1H OCEAN",
"-118.48,34.14,31.0,9320.0,1143.0,2980.0,1109.0,10.3599,500001.0,<1H OCEAN",
"-118.46,34.14,34.0,5264.0,771.0,1738.0,753.0,8.8115,500001.0,<1H OCEAN",
"-118.47,34.14,36.0,2873.0,420.0,850.0,379.0,8.153,500001.0,<1H OCEAN",
"-118.47,34.14,34.0,3646.0,610.0,1390.0,607.0,7.629,500001.0,<1H OCEAN",
"-118.43,34.14,44.0,1693.0,239.0,498.0,216.0,10.9237,500001.0,<1H OCEAN",
"-118.43,34.13,37.0,4400.0,695.0,1521.0,666.0,8.2954,500001.0,<1H OCEAN",
"-118.45,34.14,33.0,1741.0,274.0,588.0,267.0,7.9625,490800.0,<1H OCEAN",
"-118.35,34.15,52.0,1680.0,238.0,493.0,211.0,9.042,500001.0,<1H OCEAN",
"-118.36,34.15,41.0,3545.0,698.0,1221.0,651.0,4.3,500001.0,<1H OCEAN",
"-118.36,34.15,34.0,3659.0,921.0,1338.0,835.0,3.6202,366100.0,<1H OCEAN",
"-118.37,34.15,23.0,4604.0,1319.0,2391.0,1227.0,3.1373,263100.0,<1H OCEAN",
"-117.21,32.85,15.0,2593.0,521.0,901.0,456.0,4.2065,277800.0,NEAR OCEAN",
"-117.21,32.85,26.0,2012.0,315.0,872.0,335.0,5.4067,277500.0,NEAR OCEAN",
"-117.24,32.83,18.0,3109.0,501.0,949.0,368.0,7.4351,445700.0,NEAR OCEAN",
"-117.25,32.82,19.0,5255.0,762.0,1773.0,725.0,7.8013,474000.0,NEAR OCEAN",
"-117.25,32.82,23.0,6139.0,826.0,2036.0,807.0,9.5245,500001.0,NEAR OCEAN",
"-117.26,32.83,24.0,1663.0,199.0,578.0,187.0,10.7721,500001.0,NEAR OCEAN",
"-117.26,32.82,34.0,5846.0,785.0,1817.0,747.0,8.496,500001.0,NEAR OCEAN",
"-117.27,32.83,35.0,1420.0,193.0,469.0,177.0,8.0639,500001.0,NEAR OCEAN",
"-117.29,32.92,25.0,2355.0,381.0,823.0,358.0,6.8322,500001.0,NEAR OCEAN",
"-117.25,32.86,30.0,1670.0,219.0,606.0,202.0,12.4429,500001.0,NEAR OCEAN",
"-117.25,32.86,25.0,2911.0,533.0,1137.0,499.0,5.1023,500001.0,NEAR OCEAN",
"-117.25,32.86,27.0,2530.0,469.0,594.0,326.0,7.2821,500001.0,NEAR OCEAN",
"-120.69,37.59,27.0,1170.0,227.0,660.0,222.0,2.3906,81800.0,INLAND",
"-120.76,37.61,30.0,816.0,159.0,531.0,147.0,3.2604,87900.0,INLAND",
"-120.8,37.61,30.0,918.0,154.0,469.0,139.0,3.9688,175000.0,INLAND",
"-120.76,37.58,35.0,1395.0,264.0,756.0,253.0,3.6181,178600.0,INLAND",
"-120.83,37.58,30.0,1527.0,256.0,757.0,240.0,3.6629,171400.0,INLAND",
"-120.85,37.57,27.0,819.0,157.0,451.0,150.0,3.4934,193800.0,INLAND",
"-120.88,37.57,22.0,1440.0,267.0,774.0,249.0,3.9821,204300.0,INLAND",
"-120.87,37.62,30.0,455.0,70.0,220.0,69.0,4.8958,142500.0,INLAND",
"-120.87,37.6,32.0,4579.0,914.0,2742.0,856.0,2.6619,86200.0,INLAND",
"-120.86,37.6,25.0,1178.0,206.0,709.0,214.0,4.5625,133600.0,INLAND"]

lst2=['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value','ocean_proximity']

ocean_proximity=[]
for x in lst:
    y=x.split(",")
    ocean_proximity.append(y[9])
    
unique(ocean_proximity) 

housing_median_age_NEAR_BAY=[]
housing_median_age_1H_OCEAN=[]
housing_median_age_NEAR_OCEAN=[]
housing_median_age_INLAND=[]
total_bedrooms_NEAR_BAY=[]
total_bedrooms_1H_OCEAN=[]
total_bedrooms_NEAR_OCEAN=[]
total_bedrooms_INLAND=[]

for x in lst:
    y=x.split(",")
    print (y[9])
    if y[9] == "NEAR BAY":
        housing_median_age_NEAR_BAY.append(y[2])
        total_bedrooms_NEAR_BAY.append(y[4])
    elif y[9] == "<1H OCEAN":
        housing_median_age_1H_OCEAN.append(y[2])
        total_bedrooms_1H_OCEAN.append(y[4])
    elif y[9] == "NEAR OCEAN":
        housing_median_age_NEAR_OCEAN.append(y[2])
        total_bedrooms_NEAR_OCEAN.append(y[4])
    elif y[9] == "INLAND":
        housing_median_age_INLAND.append(y[2])
        total_bedrooms_INLAND.append(y[4])
        
print(total_bedrooms_INLAND)
max_housing_median_age_NEARBAY =MaxNum(housing_median_age_NEAR_BAY)
sum_housing_median_age_NEARBAY=SumNum(housing_median_age_NEAR_BAY)
max_total_bedrooms_NEARBAY =MaxNum(total_bedrooms_NEAR_BAY)
sum_total_bedrooms_NEARBAY=SumNum(total_bedrooms_NEAR_BAY)

result={'NEAR BAY':{'max':{'housing_median_age':max_housing_median_age_NEARBAY,'total_bedrooms':max_total_bedrooms_NEARBAY},'sum':{'housing_median_age':sum_housing_median_age_NEARBAY,'total_bedrooms':sum_total_bedrooms_NEARBAY}}}
print(result)


