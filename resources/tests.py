'''
Created on Sep 23, 2014

@author: cristopher
'''

class Tests(object):
    
    def testImage(self):
        from resources.managers import ImageManager
        from resources.managers import WindowManager
        ImageManager = ImageManager("images/horse.jpg")
        image = ImageManager.image
        
        window = WindowManager("Horse")        
        window.createWindow()
        window.show(image)
        
if __name__ == '__main__':
    tests = Tests()
    tests.testImage()
        
        
        