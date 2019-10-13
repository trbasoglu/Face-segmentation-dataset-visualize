import matplotlib.pyplot as plt
import matplotlib.image as mpimg


xml_file = open("sampleset.xml")
org_img_path= ""
for line in xml_file.readlines():
    if line.startswith("<srcimg"):
        org_img_path=line.split('"')[1]
    if line.startswith("<labelimg"):
        org_img=mpimg.imread(org_img_path)
        filtered_img=mpimg.imread(line.split('"')[1])
        fig = plt.figure()
        a = fig.add_subplot(2, 2, 1,polar=False)
        org_img_plot = plt.imshow(org_img)
        a.set_title('Original')
        a.axis('off')
        a = fig.add_subplot(2, 2, 2)
        a.axis('off')
        a.set_title('Filtered')
        filtered_img_plot = plt.imshow(filtered_img)
        a = fig.add_subplot(2, 2, 3)
        a.set_title('Original+Filtered')
        a.axis('off')
        imgplot = plt.imshow(org_img+filtered_img[:,:,0:3])
        plt.show()
