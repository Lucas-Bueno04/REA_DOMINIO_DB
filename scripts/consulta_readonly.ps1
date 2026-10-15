param([string]$Sql, [string]$OutCsv)
# Somente leitura: recusa qualquer coisa que nao seja SELECT
if ($Sql -notmatch '^\s*(SELECT|WITH)\b' -or $Sql -match '(?i)\b(INSERT|UPDATE|DELETE|MERGE|DROP|ALTER|CREATE|GRANT|REVOKE|TRUNCATE|CALL|EXEC)\b') { throw 'Somente SELECT permitido' }
$cn = New-Object System.Data.Odbc.OdbcConnection("DSN=Contabil;UID=$($env:DOM_UID);PWD=$($env:DOM_PWD)")
$cn.Open()
try {
    $tx = $cn.BeginTransaction([System.Data.IsolationLevel]::ReadUncommitted)
    $cmd = $cn.CreateCommand(); $cmd.Transaction = $tx; $cmd.CommandText = $Sql; $cmd.CommandTimeout = 300
    $da = New-Object System.Data.Odbc.OdbcDataAdapter($cmd)
    $dt = New-Object System.Data.DataTable
    [void]$da.Fill($dt)
    $tx.Rollback()
    if ($OutCsv) { $dt | Export-Csv -Path $OutCsv -NoTypeInformation -Encoding UTF8; "linhas: $($dt.Rows.Count) -> $OutCsv" } else { $dt }
} finally { $cn.Close() }
