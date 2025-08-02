# fruit=[item1,item2]      #list data structure
# fruit=["Apple","Cherry","Banana?"]

Districts_of_Nepal= ["Kanchanpur","Kathmandu","Lalitpur","Kailali","Nepalgunj","Chitwan"]
print(Districts_of_Nepal[-1])   #lenght-1= [5]
print(Districts_of_Nepal[-2])   #lenght-2= [5]
print(Districts_of_Nepal[1])  

Districts_of_Nepal[1]="Baitadi"
print(Districts_of_Nepal[1])   
print(Districts_of_Nepal[0])   

Districts_of_Nepal.append("Mahendranagar")   #Added at the last of the list
print(Districts_of_Nepal[0])   
print(Districts_of_Nepal[-1])   


Districts_of_Nepal.extend(["AAAAAA","BBBBBB"])  #Added at the last of the list
print(Districts_of_Nepal)

Districts_of_Nepal.remove("Kanchanpur")
print(Districts_of_Nepal[0])