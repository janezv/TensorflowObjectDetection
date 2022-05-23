import os

LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')

if not os.path.exists(LABELIMG_PATH):
    # to je namesto !mkdir {LABELIMG_PATH} --> torej ukazi se izvršujejo v CMD-ju
    cmd = "mkdir " + LABELIMG_PATH
    os.system(cmd)
    # Namesto !git clone https://github.com/tzutalin/labelImg {LABELIMG_PATH}; prvo zamenjaj aktivno mapo-->os.chdir(LABELIMG_PATH); nato naredi git clone
    os.chdir(LABELIMG_PATH)
    cmd = "git clone https://github.com/tzutalin/labelImg "
    os.system(cmd)
    # pojdi v labelimg in pogrbiši .git datoteko, ki je rezultat git clone
    os.chdir('labelImg')
    #os.system('rmdir /s /q .git')


if os.name == 'posix':
    os.system("make qt5py3")
if os.name == 'nt':
    # spodnji ukaz je za: !cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc
    # prvo zamenjaj aktivni direktori, nato nadaljuj z ukazi
    os.chdir(LABELIMG_PATH)
    os.system(
        "pyrcc5 -o libs/resources.py resources.qrc")
os.system("python labelImg.py")
