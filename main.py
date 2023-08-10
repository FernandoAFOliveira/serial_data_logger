from serial_data_logger.data_logger.file_manager import get_directory, get_filename
from serial_data_logger.settings_manager.settings_loader import default_directory
from serial_data_logger.data_logger.main_serial_logging import DataLogger
from multiprocessing import Queue
from serial_data_logger.connection_manager.serial_port_manager import establish_port_connection

if __name__ == "__main__":
    # Attempt to establish a connection to a serial port
    port = establish_port_connection()

    directory = get_directory(default_directory)
    default_filename = 'data_log.csv'
    filename_base = get_filename(default_filename)

    # Create a queue for communication (if necessary)
    queue = Queue(maxsize=1000)

    # Instantiate and start the DataLogger process
    logger = DataLogger(queue, port, directory, filename_base)
    logger.start()

    # If you have other processes or threads, you can start them here as well

    logger.join()

    # If you have other processes or threads, join them here as well
