dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

merged_dict = dict1.copy() 
merged_dict.update(dict2)   

print(merged_dict)
sampleDict = {
    'class': {
        'student': {
            'name': 'Mike',
            'marks': {
                'physics': 70,
                'history': 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])
employees = ['Kelly', 'Emma']
defaults = {'designation': 'Developer', 'salary': 8000}
dict5 = {key: defaults for key in employees}
print(dict5)