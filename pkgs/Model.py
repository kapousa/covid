import os
from keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
import numpy as np

class Model:

    def predict_covid(self, image_name):
        try:
            model = load_model('static/model/covid_vgg.h5')

            image_path = 'static/images/upload/{}'.format(image_name)
            img_width, img_height = 224, 224
            img = image.load_img(image_path, target_size=(img_width, img_height))
            x = image.img_to_array(img)
            img = np.expand_dims(x, axis=0)

            pred = model.predict(img)
            # print(pred)
            # print(np.argmax(pred, axis=1))

            if np.argmax(pred, axis=1)[0] == 1:
                print('Prediction: Non_Covid-19')
                plt.title('Prediction: Non_Covid-19')
            else:
                print('Prediction: Covid-19')
                plt.title('Prediction: Covid-19')
            plt.imshow(x / 255.)
            plt.savefig('static/images/results/plot_out.png')

            os.remove(image_path)

            return "1"

        except Exception as e:
            print(e)
            return "0"