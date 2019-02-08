import cv2
import matplotlib.pyplot as plt

class Shot:
    filename = ''
    contourArea: int
    image: any
    image_timestamp: any

    def FromFile(self, path: str):
        self = Shot()
        self.filename = path
        print('Open file: {}'.format(self.filename))
        self.image = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
        if len(self.image) == 0:
            raise ValueError('cant load: {}'.format(self.filename))
            
        self.image_timestamp = self.image[:22, :230]
        self.image[:22, :230] = 0
        
        return self

    def show_cv(self):
        cv2.imshow('shot.show_cv (press any key for close)', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_plt(self):
        plt.figure(figsize=(6, 4))
        plt.axis("off")
        #plt.title('shot.show_plt')
        plt.imshow(self.image, interpolation="bicubic")
        plt.show()
