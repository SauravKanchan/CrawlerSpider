'''
import os


# Each website you crawl is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.makedirs(directory)


# Create a queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        print("Creating file named " + queue)
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        print("Creating file named " + crawled)
        write_file(crawled, "")

#create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + "\n")


# Delete the content of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")

'''


import os





# Each website is a separate project (folder)

def create_project_dir(directory):

    if not os.path.exists(directory):

        print('Creating directory ' + directory)

        os.makedirs(directory)





# Create queue and crawled files (if not created)

def create_data_files(project_name, base_url):

    queue = os.path.join(project_name , 'queue.txt')

    crawled = os.path.join(project_name,"crawled.txt")
    youtube = os.path.join(project_name, 'youtube.txt')
    facebook = os.path.join(project_name, 'facebook.txt')
    others = os.path.join(project_name, 'others.txt')
    if not os.path.isfile(queue):

        write_file(queue, base_url)

    if not os.path.isfile(crawled):

        write_file(crawled, '')
''''
    if not os.path.isfile(youtube):
        write_file(youtube, '')
    if not os.path.isfile(facebook):
        write_file(facebook, '')
    if not os.path.isfile(others):
        write_file(others, '')
'''



# Create a new file

def write_file(path, data):

    with open(path, 'w') as f:

        f.write(data)





# Add data onto an existing file

def append_to_file(path, data):

    with open(path, 'a') as file:

        file.write(data + '\n')





# Delete the contents of a file

def delete_file_contents(path):

    open(path, 'w').close()





# Read a file and convert each line to set items

def file_to_set(file_name):

    results = set()

    with open(file_name, 'rt') as f:

        for line in f:

            results.add(line.replace('\n',''))

    return results





# Iterate through a set, each item will be a line in a file

def set_to_file(links, file_name):

    with open(file_name,"w") as f:

        for l in sorted(links):

            f.write(l+"\n")