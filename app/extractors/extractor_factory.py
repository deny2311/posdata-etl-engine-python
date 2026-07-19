from .zip_extractor import ZipExtractor


class ExtractorFactory:

    @staticmethod
    def create():

        #
        # sementara semua file adalah ZIP
        #

        return ZipExtractor()