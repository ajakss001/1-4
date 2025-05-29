sites = [
    "ssssswww",
    "https://www.illuziorficial.com/",
    "htt://wholelottaswag.ru",
    "https://gpt-chatbot.ru",
]

filtered = [s for s in sites if s.startswith("htt://")]
print(filtered)