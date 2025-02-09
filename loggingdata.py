import logging as lg

# Set up basic configuration for lg
lg.basicConfig(level=lg.DEBUG,  # Log messages at this level and higher will be logged
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example log messages at different levels
lg.debug("This is a debug message.")
lg.info("This is an info message.")
lg.warning("This is a warning message.")
lg.error("This is an error message.")
lg.critical("This is a critical message.")
