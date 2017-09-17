from lookback_data import LookbackDataEfficient


class InstrumentsLookbackData:
    def __init__(self, size, features, instrumentIds, times):
        self.__size = size
        self.__features = features
        self.__instrumentIds = instrumentIds
        self.__data = {}
        for feature in self.__features:
            self.__data[feature] = LookbackDataEfficient(size, instrumentIds, times)

    def addFeatureValueForAllInstruments(self, timeOfUpdate, featureKey, values):
        self.__data[featureKey].addData(timeOfUpdate, values)

    def getDataForFeatureForAllInstruments(self, featureKey):
        return self.__data[featureKey].getData()