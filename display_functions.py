
from get_functions import * 


def color_pair_to_string(major_color, minor_color):
  return f'{major_color}  |  {minor_color}'

def color_code_manual():
  print("-------------------------------------")
  print("MAJOR COLORS|MINOR COLORS|Pair Number")
  print("-------------------------------------")
  for major_color in MAJOR_COLORS:
    for minor_color in MINOR_COLORS:
      print(color_pair_to_string(major_color,minor_color),"|",get_pair_number_from_color(major_color,minor_color))
    print("-------------------------------------")
