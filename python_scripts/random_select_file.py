import os
import pdb
import sys
import numpy as np

def main(argv):
  pdb.set_trace() 
  source_path = argv[0]
  no_val_test = int(argv[1])
  dest_path = argv[2]
  ext = argv[3]
  list_src_files = os.listdir(source_path)
  list_audio_files = []

  for _file in list_src_files:
   if _file.find(ext)>0:
     list_audio_files.append(_file)
    
  no_of_files = len(list_audio_files)
  pdb.set_trace() 
  for i in xrange(no_val_test):
    
    rand_no = np.random.randint(no_of_files)
    file_name = list_audio_files[rand_no]
    #pos_1 = file_path.rfind('/')
    #pos_2 = file_path.rfind('.')
    #file_name = file_path[pos_1+1:]

    file_name_text = file_name.replace(ext,'txt')    
    dest_ext = dest_path + '/' + file_name
    dest_txt = dest_path + '/' + file_name_text
    file_ext = source_path + '/'+ file_name
    file_txt = source_path + '/'+ file_name.replace(ext,'txt')
    if os.path.isfile(file_ext):
      if os.path.isfile(file_txt):
        os.rename(file_ext, dest_ext)
        os.rename(file_txt, dest_txt)
    
    no_of_files = no_of_files - 1
    list_audio_files.remove(file_name)
  
  print 'Done !!!'     

if __name__=='__main__':
  main(sys.argv[1:])  
