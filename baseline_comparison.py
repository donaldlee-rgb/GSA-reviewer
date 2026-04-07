class BaselineComparisonModule:
    def __init__(self, baseline):
        """
        Initialize the module with the baseline configuration.
        :param baseline: A dictionary containing the baseline configuration.
        """
        self.baseline = baseline

    def detect_deviations(self, incoming_contract):
        """
        Detect deviations in the incoming contract compared to the baseline.
        :param incoming_contract: A dictionary containing the incoming contract terms.
        :return: A list of deviations found.
        """
        deviations = []

        # Check deviations in each required field
        for field in self.baseline:
            if field not in incoming_contract:
                deviations.append(f"Missing field: {field}")
            elif incoming_contract[field] != self.baseline[field]:
                deviations.append(f"Deviation in {field}: Expected '{self.baseline[field]}', Found '{incoming_contract[field]}'")

        return deviations
