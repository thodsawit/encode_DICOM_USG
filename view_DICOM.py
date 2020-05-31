import pydicom
import cv2
import os
import matplotlib.pyplot as plt


DICOM_dir = '/Users/thodsawit/PycharmProjects/LIRADS_USG/codes/utilities/encode_DICOM/dcm_mod'

files = []
for r, d, f in os.walk(DICOM_dir):
    for file in f:
        if '.dcm' in file or '00000' in file:
            files.append(os.path.join(r, file))

print("We have total : " + str(len(files)) + " files")



for f in files:
    ds = pydicom.dcmread(f)

    record = ['']*37
    record[0] = f
    try: record[2] = str(ds.InstanceNumber)
    except: None
    try: record[3] = str(ds.AccessionNumber)
    except: None
    try: record[4] = str(ds.PatientID)
    except: None
    try: record[5] = str(ds.StudyDate)
    except: None
    try: record[6] = str(ds.StudyTime)
    except: None

    record[27] = 'DICOM'
    try: record[28] = str(ds.SOPClassUID)
    except: None
    try: record[29] = str(ds.SOPInstanceUID)
    except: None
    try: record[30] = str(ds.Manufacturer)
    except: None
    try: record[31] = str(ds.InstitutionName)
    except: None
    try: record[32] = str(ds.StudyDescription)
    except: None
    try: record[33] = str(ds.ManufacturerModelName)
    except: None
    try: record[34] = str(ds.PatientBirthDate)
    except: None
    try: record[35] = str(ds.PatientSex)
    except: None
    try: record[36] = str(ds.DeviceSerialNumber)
    except: None
    try: record[37] = str(ds.TransducerData[0])
    except: None

    for e in record:
        if e != '':
            print(e)

    try:
        img = ds.pixel_array
        """
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        """
        plt.figure()
        plt.imshow(img, cmap='gray')
        plt.show()

    except:
        None

