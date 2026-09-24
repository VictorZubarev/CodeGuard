from codeguard.main import main

def test_cli_missing_path(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["codeguard", "scan", "nonexistent.py"],
    )

    main()

    captured = capsys.readouterr()

    assert captured.out == "Error: Path not found: nonexistent.py\n"