from references.ch06 import p0654_round_robin_scheduler as scheduler_mod


def test_round_robin_scheduler_interleaves_registered_tasks() -> None:
    # Arrange
    output: list[str] = []

    def task(name: str, count: int):
        for index in range(count):
            output.append(f"{name}{index}")
            yield

    scheduler = scheduler_mod.Scheduler()
    scheduler.add(task("A", 3))
    scheduler.add(task("B", 2))

    # Act
    scheduler.run()

    # Assert
    assert output == ["A0", "B0", "A1", "B1", "A2"]
