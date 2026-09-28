from codeguard.main import main

def test_cli_missing_path(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["codeguard", "scan", "nonexistent.py"],
    )

    main()

    captured = capsys.readouterr()

    assert captured.out == "Error: Path not found: nonexistent.py\n"

def test_cli_summary(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["codeguard", "scan", "tests/vulnerable_example.py"],
    )

    main()

    captured = capsys.readouterr()

    assert "CodeGuard Security Report" in captured.out
    assert "Files scanned: 1" in captured.out
    assert "Findings: 1" in captured.out
    assert "HIGH: 1" in captured.out





