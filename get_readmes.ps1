# Get all subdirectories in the current directory
$subfolders = Get-ChildItem -Directory

foreach ($folder in $subfolders) {
    $readmePath = Join-Path -Path $folder.FullName -ChildPath "README.md"
    
    # Check if the README.md file already exists
    if (Test-Path -Path $readmePath) {
        Write-Host "README.md already exists in $($folder.FullName)"
        continue
    }

    # Parse the day number from the folder name
    if (-not ($folder.Name -match "^day_(\d{2}|\d{1})$")) {
        Write-Host "Folder name $($folder.Name) does not match the expected pattern"
        continue
    }

    $dayNumber = [int]$matches[1]
    Write-Host "Parsed day number: $dayNumber from folder name: $($folder.Name)"

    # Make an HTTP request to fetch the HTML content for the specific day

    # NOTE: To get the correct values for this request, open dev tools in your browser, inspect the network tab,
    #       request a page, then right click the request and copy as PowerShell. This will give you the headers and cookies.

    $session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
    $session.UserAgent = "GET_FROM_NETWORK_TAB"
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga", "GET_FROM_NETWORK_TAB", "/", ".adventofcode.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_gid", "GET_FROM_NETWORK_TAB", "/", ".adventofcode.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("session", "GET_FROM_NETWORK_TAB", "/", ".adventofcode.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga_MHSNPJKWC7", "GET_FROM_NETWORK_TAB", "/", ".adventofcode.com")))
    
    $response = Invoke-WebRequest -UseBasicParsing -Uri "https://adventofcode.com/2022/day/$dayNumber" `
    -WebSession $session `
    -Headers @{
    "authority"="adventofcode.com"
      "method"="GET"
      "path"="/2022/day/$dayNumber"
      "scheme"="https"
      "accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
      "accept-encoding"="gzip, deflate, br, zstd"
      "accept-language"="en-US,en;q=0.9"
      "priority"="u=0, i"
      "sec-ch-ua"="`"Chromium`";v=`"134`", `"Not:A-Brand`";v=`"24`", `"Google Chrome`";v=`"134`""
      "sec-ch-ua-mobile"="?0"
      "sec-ch-ua-platform"="`"Windows`""
      "sec-fetch-dest"="document"
      "sec-fetch-mode"="navigate"
      "sec-fetch-site"="none"
      "sec-fetch-user"="?1"
      "upgrade-insecure-requests"="1"
    }

    # Parse the HTML content and extract the article section with the CSS selector `.day-desc`
    if ($response.StatusCode -eq 200) {
        $html = $response.Content
        
        # Debug step
        # $responseHtmlPath = Join-Path -Path $folder.FullName -ChildPath "response.html"
        # $html | Out-File -FilePath $responseHtmlPath -Encoding UTF8

        # Load the HTML content into an XML document for parsing
        $startTag = '<article class="day-desc">'
        $endTag = '</article>'

        $startIndex = $html.IndexOf($startTag)
        $endIndex = $html.IndexOf($endTag)
        $startIndex2 = $html.IndexOf($startTag, $startIndex + 1)
        $endIndex2 = $html.IndexOf($endTag, $endIndex + 1)

        if ($startIndex -ne -1 -and $endIndex -ne -1) {
            Write-Host "Found the article section with class 'day-desc' for day $dayNumber"
            $startIndex += $startTag.Length
            $part1 = $html.Substring($startIndex, $endIndex - $startIndex).Trim()
            $part2 = $html.Substring($startIndex2, $endIndex2 - $startIndex2).Trim()
            $Content = $part1 + "`n`n" + $part2
        } else {
            Write-Host "Could not find the article section with class 'day-desc' for day $dayNumber"
            $Content = "This is the README for the folder '$($folder.Name)'"
        }

    } else {
        Write-Host "Failed to fetch content for day $dayNumber. Status Code: $($response.StatusCode)"
        $Content = "This is the README for the folder '$($folder.Name)'"
    }

    # Create the README.md file with a default message
    $Content | Out-File -FilePath $readmePath -Encoding UTF8
    Write-Host "Created README.md in $($folder.FullName)"
}