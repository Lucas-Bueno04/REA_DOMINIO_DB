param([string]$File, [string]$Needle, [int]$Blocks = 6)
# PowerBuilder PBD: blocos "DAT*" de 512 bytes = 'DAT*'(4) + proximo bloco(4) + tamanho(2) + dados(502)
$b = [System.IO.File]::ReadAllBytes($File)
$enc = [System.Text.Encoding]::GetEncoding(1252)
$text = $enc.GetString($b)
$idx = $text.IndexOf($Needle)
$seen = 0
while ($idx -ge 0 -and $seen -lt 3) {
    $blk = [int]([Math]::Floor($idx / 512) * 512)
    # localizar inicio do bloco DAT*
    while ($blk -gt 0 -and $enc.GetString($b, $blk, 4) -ne 'DAT*') { $blk -= 512 }
    $out = ''
    for ($i = 0; $i -lt $Blocks -and $blk -gt 0; $i++) {
        $next = [BitConverter]::ToInt32($b, $blk + 4)
        $len = [BitConverter]::ToUInt16($b, $blk + 8)
        $out += $enc.GetString($b, $blk + 10, [Math]::Min($len, 502))
        if ($next -le 0 -or $next -ge $b.Length) { break }
        $blk = $next
    }
    $start = $out.IndexOf($Needle)
    ($out.Substring([Math]::Max(0, $start - 50)) -replace '[\x00-\x1F]', ' ')
    '----'
    $seen++
    $idx = $text.IndexOf($Needle, $idx + 1)
}
