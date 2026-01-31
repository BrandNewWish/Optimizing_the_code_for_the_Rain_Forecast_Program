import json
import os


class WeatherForecast:
    def __init__(self, filename= 'Weather_cache.json'):
        self.filename = filename
        self._cache = self._load()


    def _load(self):
        if not os.path.exists(self.filename):
            self._save_empty()
            return {}

        try:
            with open(self.filename) as f:
                return json.load(f)
        except json.JSONDecodeError:
            self._save_empty()
            return {}

    def _save_empty(self):
        with open(self.filename, "w") as f:
            json.dump({}, f, indent=4)

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self._cache, f, indent=4)


    def __setitem__(self, date, weather):
        self._cache[date] = weather
        self._save()


    def __getitem__(self, date):
        return self._cache[date]


    def __iter__(self):
        return iter(self._cache)


    def items(self):
        for date, weather in self._cache.items():
            yield date, weather



