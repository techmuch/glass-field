class Context:
    def __init__(self, team, opponent, blitz_probability=0.2):
        self.team = team
        self.opponent = opponent
        self.blitz_probability = blitz_probability

class SignalIntel:
    """
    Simulates Stage 0: Signal Intelligence (OSINT Ingestion).
    """
    @staticmethod
    def fetch_context(team, opponent):
        # Placeholder for actual LLM scraping / Market API integration
        # In the future, this will return dynamic data based on the match-up
        return Context(team=team, opponent=opponent, blitz_probability=0.65)
