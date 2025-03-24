$url = "https://steamcommunity.com/workshop/filedetails/?id=450814997"
$result = Invoke-WebRequest -Uri $url

# Regex, der alle <div class="detailsStatRight">...</div> findet.
# Mit Singleline-Option, damit auch Zeilenumbrüche im Inhalt passen.
$regex = [regex]::new('<div\s+class="detailsStatRight">\s*(?<content>.*?)\s*</div>', [System.Text.RegularExpressions.RegexOptions]::Singleline)

$matches = $regex.Matches($result.Content)
if ($matches.Count -gt 0) {
    foreach ($match in $matches) {
        Write-Host "Gefunden: " $match.Groups["content"].Value
    }
}
else {
    Write-Warning "Keine passenden Elemente gefunden."
}
