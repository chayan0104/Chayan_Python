from loguru import logger
# for ini file
import configparser
config = configparser.ConfigParser()  # Creating object
config.read(r"C:\Users\Satyam\Desktop\Chayan_Python\10_configfile_handling\ini_config\config_file.ini")

# for json file 
# import json
# with open("C:\Users\Satyam\Desktop\Chayan_Python\10_configfile_handling\ini_config\config_file.ini","r") as f:
# config = json.load(f)

brick_cost = config["raw_material"]["brick"]  #every value will be come as string by default
# logger.info(brick_cost)

# ---------------------------------------------------------------------------

def surface_cal(length, width, height):
    surface_area = 2 * (length * width + length * height + width * height)
    return surface_area

brick_surface_area=surface_cal(20,10,10)
wall_surface_area=surface_cal(1000,500,500)

total_bricks= wall_surface_area/brick_surface_area
print(f"Total bricks needed is {total_bricks} and cost is {total_bricks*float(brick_cost)} rs")



