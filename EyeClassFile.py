class EyeClassDetails:
    __startingX = 0  # starting horizontal coordinate of frame
    __startingY = 0  # starting vertical coordinate of frame
    __endingX = 0  # ending horizontal coordinate of frame
    __endingY = 0  # ending vertical coordinate of frame
    __eyeType = ''  # left or rightor complete
    __eyeFrame = None

    def __init__(self, eyeFrame, eyeType, sX, sY, eX, eY):
        self.__eyeFrame = eyeFrame
        self.__eyeType = eyeType
        self.__startingX = sX
        self.__startingY = sY
        self.__endingX = eX
        self.__endingY = eY

    def getStartingXCoordinate(self):
        return self.__startingX

    def getStartingYCoordinate(self):
        return self.__startingY

    def getEndingXCoordinate(self):
        return self.__endingX

    def getEndingYCoordinate(self):
        return self.__endingY

    def getEyeType(self):
        return self.__eyeType

    def getEyeFrame(self):
        return self.__eyeFrame

class EyeClass:
    __leftEye = None
    __rightEye = None
    def __init__(self, leftEye, rightEye, ):
        self.__leftEye = leftEye
        self.__rightEye = rightEye

    def getLeftEye(self):
        return self.__leftEye
    def getRightEye(self):
        return self.__rightEye
