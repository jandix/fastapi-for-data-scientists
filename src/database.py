import json
import os
from typing import Literal, TypedDict


class NutsStatisticUpdate(TypedDict):
    total_jobs: int | None
    total_jobs_per_10k: float | None


class NutsStatistic(TypedDict):
    nuts_id: str
    total_jobs: int
    total_jobs_per_10k: float


class Database:
    def __init__(self, dataset: Literal["small", "large"] = "small") -> None:
        if dataset == "large":
            with open(os.path.join(".", "regions.json"), mode="r") as fp:
                parsed_data = json.load(fp)
                self._data = [
                    {
                        "nuts_id": item["nuts_id"],
                        "total_jobs": item["total_jobs"],
                        "total_jobs_per_10k": item["total_jobs_per_10k"],
                    }
                    for item in parsed_data["data"]
                ]
        else:
            self._data = [
                {
                    "nuts_id": "DE111",
                    "total_jobs": 15503,
                    "total_jobs_per_10k": 356.6457858376909,
                },
                {
                    "nuts_id": "DE112",
                    "total_jobs": 4630,
                    "total_jobs_per_10k": 254.8016069561389,
                },
                {
                    "nuts_id": "DE113",
                    "total_jobs": 6119,
                    "total_jobs_per_10k": 275.45567905069305,
                },
                {
                    "nuts_id": "DE114",
                    "total_jobs": 2087,
                    "total_jobs_per_10k": 233.6307358192748,
                },
                {
                    "nuts_id": "DE115",
                    "total_jobs": 5507,
                    "total_jobs_per_10k": 261.6462762798432,
                },
            ]

    def list(self) -> list[NutsStatistic]:
        return self._data

    def get_by_id(self, id: str) -> NutsStatistic:
        return next((item for item in self._data if item["nuts_id"] == id), None)

    def create(self, data: NutsStatistic) -> NutsStatistic:
        self._data.append(data)
        return data

    def update(self, id: str, data: NutsStatisticUpdate) -> NutsStatistic:
        for item in self._data:
            if item["nuts_id"] == id:
                for key, value in data.items():
                    item[key] = value
                return item

    def delete(self, id: str) -> None:
        self._data = [item for item in self._data if item["nuts_id"] != id]
