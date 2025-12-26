import cv2
import cv2.aruco as aruco

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

for marker_id, name in [(1, "carbon"), (2, "oxygen"), (3, "co2")]:
    marker = aruco.generateImageMarker(aruco_dict, marker_id, 600)
    cv2.imwrite(f"{name}_marker.png", marker)

print("✅ Carbon, Oxygen, and CO2 markers created")
