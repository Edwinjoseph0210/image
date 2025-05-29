import cv2

# Read the image
input_path = input("Enter input image path: ")
output_path = input("Enter output image path: ")

img = cv2.imread(input_path)
if img is None:
    print("Could not open or find the image!")
    exit()

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite(output_path, gray_img)

print(f"Grayscale image saved as {output_path}")

# Optionally display the images
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
