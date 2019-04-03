from src.detector import detect_faces
from src.utils import show_bboxes
from PIL import Image
import cv2
import os

import sys

def main():


        cap = cv2.VideoCapture('/home/admin/face_detection/dataset/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.mp4')

        mog = cv2.createBackgroundSubtractorMOG2(1,55)





        while(1):






            ret, frame = cap.read()

            if (ret==False):
                break


            if (i%5):
                i += 1
                continue

            j=str(i)

            cv2.imwrite('image/' + j + '.jpg',frame)





            #image = Image.open('images/test3.jpg')

            image1 = Image.open('image/' + j + '.jpg')

            path = 'image/' + j + '.jpg'

            bounding_boxes, landmarks = detect_faces(image1)


            #image = show_bboxes(image, bounding_boxes, landmarks)

            image2 = show_bboxes(image1, bounding_boxes, landmarks)

            a=0


            for b in bounding_boxes:
                a = 1
                break


            if a:

                fgmask = mog.apply(frame,1)



                dilate = cv2.dilate(fgmask, (21, 21), iterations=1)



                (cnts, _) = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



                ee = open('chayi/' + j + ' chayi' + '.txt', 'a')

                for c in cnts:


                    c_area = cv2.contourArea(c)

                    if (c_area > 3000):



                        cc = str(c_area)

                        ee.write(cc+'\n')




                        f = open('txt'+ p + '/' + j +'.txt', 'a')
                        for b in bounding_boxes:

                            x = ((b[0]+b[2])/2)/(image1.size[0])

                            y = (0.5*b[1] + 0.5*b[3])/(image1.size[1])

                            w = ((b[2] - b[0])*1.0)/(image1.size[0])

                            h = ((b[3] - b[1])*1.0)/(image1.size[1])

                            x = str(x)


                            y = str(y)


                            w = str(w)


                            h = str(h)





                            f.write('0 '+x+' '+y+' '+w+' '+h+'\n')


                            z = int(j)



                            image1.save('dataset'+ p +'/' + j + '.jpg')


                        break



            #image.show()

            #image1.show()




            i+=1


        #image3 = Image.open('image/55.jpg')

        #print(image3.size)




if __name__ == "__main__":
    main()
