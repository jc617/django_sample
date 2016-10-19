
# --- input -> request : method: request; data: script_name, script_number,

# post
# if post
# insert into table: script_name, script_id, modified_date 
# hash script_id
# find folder with hash_script_id
# save sql to folder with name f+modified_date

# input: script_name, script_id, created_date, modified_date, sql

import hashlib
import codecs
import os 
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
FILE_DIR = os.path.join(BASE_DIR, 'files')
FILE_FORMAT = "%Y_%m_%d_%H_%M_%S_%f"

def create_hash_folder(i):
	m = hashlib.sha224() 
	s = 'sql'+str(i) 

	folder_name = 'script_'+hashlib.sha224(s.encode()).hexdigest()	
	full_folder_path = os.path.join(FILE_DIR,folder_name)
	
	if not os.path.exists(full_folder_path):
		os.makedirs(full_folder_path) 
		print ('create folder: {} for input: {}'.format(full_folder_path, i))
	else:
		print ('already have folder for input: {}'.format(i))
	return full_folder_path

def find_hash_folder(i):	
	m = hashlib.sha224() 
	s = 'sql'+str(i) 

	folder_name = 'script_'+hashlib.sha224(s.encode()).hexdigest()	
	full_folder_path = os.path.join(FILE_DIR,folder_name)	 

	if os.path.exists(full_folder_path):
		print  ('Find folder for input: {}'.format(i))
		return full_folder_path
	else:
		print ('Could not find folder for input: {}'.format(i))
		return None

def post_file(id, sql, modified_date): 
	folder = create_hash_folder(id)	
	file_name = 'file_'+str(modified_date.strftime(FILE_FORMAT))+'.sql'	
	file_path = os.path.join(folder,file_name)

	with open(file_path, 'w') as sql_file:
		sql_file.write(sql)
	sql_file.close()

def get_file(id):
	folder = find_hash_folder(id)	
	if folder:
		files = sorted(os.listdir(folder))		
	else:
		print ('cannot find folder for {}'.format(id))
		# error
		return 
	if files:
		file_name = files[-1]
		with open(os.path.join(folder,file_name),'r') as sql:
			print ('id: {}, folder: {},file: {}, sql: {}'.format(id,folder,file_name,sql.read()))
		sql.close()
	else:
		print ('id: {}, folder: {}, no file!!!'.format(id, folder))
	 
		

# Start execution here!
if __name__ == '__main__':
	print("Starting job population script...")
	# post_file(1,'test_sql_111', datetime.datetime.now())
	# post_file(2,'test_sql_222', datetime.datetime.now())
	# post_file(3,'test_sql_333', datetime.datetime.now())
 # 	create_hash_folder(4)

 	get_file(1)
 	get_file(2)
 	get_file(3)
 	get_file(4)
  	get_file(5)
