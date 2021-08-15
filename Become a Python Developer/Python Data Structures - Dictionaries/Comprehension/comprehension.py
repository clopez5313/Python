sal_data_keys = ["Austin", "Portland", "Dallas","Atlanta"]
sal_data_values = [91185,110123, 89123, 112000]

sal_info = {}
print("#### Creating a dictionary without using comprehension")
for key, value in zip(sal_data_keys,sal_data_values):
	sal_info[key] = value
print (sal_info)
sal_info.clear()

#Using Dictionary Comprehension to popultate the dictionary
print("#### Creating a dictionary using comprehension")

sal_info = {sal_data_keys[i]:sal_data_values[i] for i in range(0,len(sal_data_keys))}
print(sal_info)
