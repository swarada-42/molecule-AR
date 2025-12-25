import cv2
import cv2.aruco as aruco

# Choose dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# Marker ID (any number 0–49)
marker_id = 7

# Marker size (pixels)
marker_size = 600

# Generate marker
marker_img = aruco.generateImageMarker(
    aruco_dict,
    marker_id,
    marker_size
)

# Save marker
cv2.imwrite("my_marker.png", marker_img)

print("✅ Marker created: my_marker.png")
