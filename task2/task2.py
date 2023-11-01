from math import sqrt
from sys import argv

script, circle_file, points_file = argv

points = []

with open(circle_file, "r") as circle_f:
	center = circle_f.readline().strip()
	rad = circle_f.readline().strip()
	circle_x, circle_y = center.split(" ")
	circle_x = float(circle_x)
	circle_y = float(circle_y)
	rad = float(rad)

with open(points_file, "r") as points_f:
	for line in points_f:

		point_x, point_y = line.strip().split(" ")
		point_x = float(point_x)
		point_y = float(point_y)
		points_tuple = (point_x, point_y)
		points.append(points_tuple)

for tuple in points:
	distance = sqrt((tuple[0] - circle_x)**2 + (tuple[1] - circle_y)**2 )

	if distance > rad:
		print(2)
	elif distance == rad:
		print(0)
	elif distance < rad:
		print(1)
	
	
	