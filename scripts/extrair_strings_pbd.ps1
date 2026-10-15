param([string[]]$Files, [string]$Out, [int]$Min = 6)
$sb = New-Object System.Text.StringBuilder
foreach ($f in $Files) {
    $bytes = [System.IO.File]::ReadAllBytes($f)
    $name = [System.IO.Path]::GetFileName($f)
    # ASCII
    $ascii = [System.Text.Encoding]::GetEncoding(1252).GetString($bytes)
    foreach ($m in [regex]::Matches($ascii, "[\x20-\x7E\xC0-\xFF\t\r\n]{$Min,}")) { [void]$sb.AppendLine("$name`tA`t" + ($m.Value -replace "[\r\n\t]+", ' ')) }
    # UTF-16LE
    $u = [System.Text.Encoding]::Unicode.GetString($bytes)
    foreach ($m in [regex]::Matches($u, "[\x20-\x7E\xC0-\xFF\t\r\n]{$Min,}")) { [void]$sb.AppendLine("$name`tU`t" + ($m.Value -replace "[\r\n\t]+", ' ')) }
    $u2 = [System.Text.Encoding]::Unicode.GetString($bytes, 1, $bytes.Length - 1)
    foreach ($m in [regex]::Matches($u2, "[\x20-\x7E\xC0-\xFF\t\r\n]{$Min,}")) { [void]$sb.AppendLine("$name`tU`t" + ($m.Value -replace "[\r\n\t]+", ' ')) }
}
[System.IO.File]::WriteAllText($Out, $sb.ToString(), [System.Text.Encoding]::UTF8)
