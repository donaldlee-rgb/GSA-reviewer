import re
import json

class RedlineDetector:
    def __init__(self):
        self.changes = []

    def parse_tracked_changes(self, document):
        # Dummy implementation for tracked changes parsing
        pattern = r"(?P<change_type>[+-])(?P<content>.*?)"
        matches = re.finditer(pattern, document)
        for match in matches:
            change_type = match.group('change_type')
            content = match.group('content')
            self.changes.append((change_type, content))

    def extract_redline_metadata(self, change):
        # Dummy metadata extraction
        return {
            'author': 'unknown',
            'timestamp': '2026-04-07T18:49:48Z',
            'change_type': change[0]
        }

    def categorize_changes_by_risk(self):
        risk_categories = {'low': [], 'medium': [], 'high': []}
        for change in self.changes:
            risk_level = self.assess_risk(change)
            risk_categories[risk_level].append(change)
        return risk_categories

    def assess_risk(self, change):
        # Dummy risk assessment based on the content
        if 'important' in change[1]:
            return 'high'
        elif 'optional' in change[1]:
            return 'low'
        else:
            return 'medium'

    def get_redline_report(self):
        report = []
        for change in self.changes:
            metadata = self.extract_redline_metadata(change)
            report.append({
                'change': change,
                'metadata': metadata
            })
        return json.dumps(report, indent=4)

# Example Usage
if __name__ == '__main__':
    rd = RedlineDetector()
    example_document = "+ Addition of new clause\n- Removal of outdated information"
    rd.parse_tracked_changes(example_document)
    print(rd.get_redline_report())