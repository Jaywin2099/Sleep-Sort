from threading import Thread
from time import sleep

data = [3, 1, 2]

def thread_function(data_list, data):
    # waits the magnitude of the data
    sleep(data)

    # adds it to list
    data_list.append(data)
    
def sleepSort(data):
    print('sorting...')

    sortedData = []
    threads = []

    # creates and stores threads for each data point
    for i in data:
        thread = Thread(target=thread_function, args=(sortedData, i))
        thread.start()
        threads.append(thread)

    # waits for all threads to finish running
    for thread in threads:
        thread.join()

    # deep copies sortedData back into data
    for i in range(len(data)):
        data[i] = sortedData[i]

    # also returns data
    return data

# main function
if __name__ == '__main__':
    print('data:' + str(data))
    print('calling sleep sort on data list')
    sleepSort(data)
    print('sorted data:' + str(data))