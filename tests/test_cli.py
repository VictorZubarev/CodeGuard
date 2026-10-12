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
    assert "CRITICAL: 1" in captured.out

def test_cli_severity_filter(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "codeguard",
            "scan",
            "tests/vulnerable_example.py",
            "--severity",
            "HIGH",
        ],
    )

    main()

    captured = capsys.readouterr()

    assert "CodeGuard Security Report" in captured.out
    assert "Findings: 1" in captured.out
    assert "[CRITICAL] CG001" in captured.out
    assert "CRITICAL: 1" in captured.out

def test_cli_severity_filter_excludes_lower_severity(
    capsys,
    monkeypatch,
    tmp_path,
):
    test_file = tmp_path / "example.py"
    test_file.write_text(
        "import hashlib\n"
        "password = 'example-password'\n"
        "hashlib.md5(b'data')\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "codeguard",
            "scan",
            str(test_file),
            "--severity",
            "HIGH",
        ],
    )

    main()

    captured = capsys.readouterr()

    assert "[HIGH] CG005" in captured.out
    assert "[MEDIUM] CG008" not in captured.out
    assert "Findings: 1" in captured.out
    assert "HIGH: 1" in captured.out