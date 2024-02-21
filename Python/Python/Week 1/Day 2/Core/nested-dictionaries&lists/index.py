x = [ [5,2,3], [15,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['andreas', 'Ronaldo', 'Rooney']
}
z = [ {'x': 30, 'y': 20}
      ]

def iterateDictionary(students):
    for dictionary in students:
    
        for key, value in dictionary.items():
            # Print the key and its associated value
            print(f"{key}: {value}")

# Example usage:
students = [
    {'first_name': 'Michael', 'last_name': 'Bryant'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    
]
iterateDictionary(students)
