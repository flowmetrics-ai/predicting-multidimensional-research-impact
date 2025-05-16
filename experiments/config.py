models = [
    "gpt-3.5-turbo",
    "gpt-4o",
    "gpt-4o-mini",
    "claude-3-7-sonnet-20250219",
    "claude-3-5-haiku-20241022",
    "open-mixtral-8x22b",
    "deepseek-chat"
]

impact_stages = ["reach", "engagement", "feedback", "influence", "outcome"]

stage_order = {s: i for i, s in enumerate(impact_stages)}