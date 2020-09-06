with open('NameFile.txt','w+') as file:
    file.write('Obed Balogun Tolu')
    file.close()

def readFile(filename):
    names = {}
    with open(filename,'r+') as doc :
        file_content = doc.readline().split()
        names['Firstname'] = file_content[0]
        names['Surname'] = file_content[1]
        names['Middlename'] = file_content[2]
        doc.close()
        return names

print(readFile('NameFile.txt'))