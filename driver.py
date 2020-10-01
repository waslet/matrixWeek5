import logging
import wahoo
import numpy.matlib 
import numpy as np

def main():

    logging.basicConfig(filename='debug-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')

    logging.info('INFO: Program start')

    test1 = np.matrix("1,2;3,4")
    print("Test 1:")
    print("\nInput Matrix:")
    print(test1)
    print("\nOutput Matrix:")
    print(wahoo.wahoovian(test1))
    
    test2 = np.matrix("1,2")
    print("\nTest 2:")
    print("\nInput Matrix:")
    print(test2)
    print("\nOutput Matrix:")
    print(wahoo.wahoovian(test2))

    test3 = np.matrix("1,2,3;4,5,6;7,8,9")
    print("\nTest 3:")
    print("\nInput Matrix:")
    print(test3)
    print("\nOutput Matrix:")
    print(wahoo.wahoovian(test3))

    logging.info('INFO: Program end')

if __name__ == '__main__':
    main()
