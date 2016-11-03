import sys
import os
def main(argv):
    dir_path = argv[0]
    store_dir_path = argv [1] 
    list_files  = os.listdir(dir_path)
    count = 0
    str_1 = 'input/images'
    str_2 = '[say'
    str_3 = 'xxx' 
    print 'total len %d' % (len(list_files))
    count_1 = 0 
    while (count<len(list_files)):
        file_name = list_files[count]
	if 'txt' in file_name:
            file_read = open(dir_path+'/'+file_name,'rb')
            line = file_read.readline()
            #print line
            if line.startswith(str_1) or line.startswith(str_2) or line.startswith(str_3):
                audio_file  = file_name.replace('txt','wav')
                print file_name
                #print line 
                os.rename(dir_path+'/'+file_name,store_dir_path+'/'+file_name)
                os.rename(dir_path+'/'+audio_file,store_dir_path+'/'+audio_file)
                list_files.remove(file_name)
                list_files.remove(audio_file)  
                count_1 = count_1 + 1
                
            else:
                count = count + 1
        else:
            count = count + 1    
    print count_1                     
if __name__=='__main__':
    main(sys.argv[1:])        
