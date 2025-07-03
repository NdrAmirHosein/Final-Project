class phase4:
    def __init__(self, national_code, license_date, neg_scores, license_issue_date, score=None):
        self.national_code = national_code
        self.license_issue_date = license_issue_date
        self.license_date_int = license_date
        self.neg_scores = neg_scores
        self.score = score