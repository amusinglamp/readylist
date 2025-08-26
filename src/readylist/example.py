ExampleList = '''
nodes:
 - Ready To Rock
   * Guitar: guitar
   * Amp: ready
   * Pedals: ready
   * Cables: ready
   * Set List: ready

 - Guitar
   * Plugged in: not ready
   * Turned up: ready
   * Tuned: ready

'''

ExampleJson = """
{
    "name": "Root",
    "state": "EXPIRED"
    "valid_to": datetime(2024, 1, 1),
    "items": [
        {
            "name": "MSDN Membership",
            "state": "READY"
            "valid_to": datetime(2026, 1, 10),
            "items": []
        },
        {
            "name": "PC",
            "state": "READY"
            "valid_to": datetime(2025, 12, 20),
            "items": []
        }
    ]
}
"""
