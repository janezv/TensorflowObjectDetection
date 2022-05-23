import os

LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')

if not os.path.exists(LABELIMG_PATH):
    # Namesto !git clone https://github.com/tzutalin/labelImg {LABELIMG_PATH}; prvo zamenjaj aktivno mapo-->os.chdir(LABELIMG_PATH); nato naredi git clone
    os.chdir('Tensorflow')
    cmd = "git clone https://github.com/tzutalin/labelImg "
    os.system(cmd)
    # pojdi v labelimg in pogrbiši .git datoteko, ki je rezultat git clone
    os.chdir('labelImg')
    os.system('rmdir /s /q .git')
else:
    os.chdir(LABELIMG_PATH)


if os.name == 'posix':
    os.system("make qt5py3")
if os.name == 'nt':
    os.system(
        "pyrcc5 -o libs/resources.py resources.qrc")
    os.system("python labelImg.py")
