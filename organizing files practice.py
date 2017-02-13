import shutil, os

os.chdir(r'C:\Users\suryakislaya\Documents\GitHub\practice-experiments\1\3\3.1')
sourcePath = os.path.join(os.getcwd(),'3.1_.txt')
shutil.copy(sourcePath, 'C:\\Users\\suryakislaya\\Documents\\GitHub\\practice-experiments\\1\\2\\2.1\\2.1.1\\2.1.1.1')
#or we can use ->
#shutil.copy(sourcePath, '..\\..\\2\\2.1\\2.1.1\\2.1.1.1') -> because the current directory was set to 3.1 folder and we can give ..\\ to go back one folder
print(os.path.exists('..\\..\\3\\3backup'))
if os.path.exists('..\\..\\3\\3backup'):
    shutil.rmtree('..\\..\\3\\3backup')
else:
    shutil.copytree('..\\..\\3','..\\3backup' )
    
os.chdir(r'C:\Users\suryakislaya\Documents\GitHub\practice-experiments\1')

for folderName,subfolders,filenames in os.walk(os.getcwd()):
         print('The current Folder is ' + os.path.basename(folderName))

         for subfolder in subfolders:
             print('Subfolder of ' + os.path.basename(folderName) +': ' + subfolder)
         for filename in filenames:
             print('File Inside ' + os.path.basename(folderName)+ ': ' + filename)
         print('')

         
         
                                               
                                               
