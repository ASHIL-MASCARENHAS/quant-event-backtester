from .data_loader import DataLoader
from .data_cleaner import DataCleaner, MissingDataHandler
from .data_validator import DataValidator
from .data_aligner import DataAligner


class ETLPipeline:

    def __init__(self, data_dir: str):
        self.loader = DataLoader(data_dir)
        self.cleaner = DataCleaner()
        self.missing_handler = MissingDataHandler()
        self.validator = DataValidator()
        self.aligner = DataAligner()

    def run(self, file_path: str):

        # Step 1: Load
        df = self.loader.load(file_path)

        # Step 2: Clean
        df = self.cleaner.clean(df)

        # Step 3: Handle missing
        df = self.missing_handler.handle(df)

        # Step 4: Validate
        self.validator.validate(df)

        # Step 5: Align multi-asset data
        df = self.aligner.align(df)

        return df