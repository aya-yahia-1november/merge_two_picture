import cv2
sky_img=cv2.imread("sky.jpg",1)
gorm_img=cv2.imread("gorm.jpeg",1)
sky_img=cv2.resize(sky_img,[512,512])
gorm_img=cv2.resize(gorm_img,[512,512])
merge=cv2.addWeighted(sky_img,.6,gorm_img,.4,0) #gama Brightness of picture
cv2.imshow("frame",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()